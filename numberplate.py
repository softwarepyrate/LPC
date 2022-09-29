# -----------------------------------------------------------
# v1.1-290922: Add Exceptions handler
#
#
#
#
# -----------------------------------------------------------


import os

import cv2
import easyocr
import numpy as np
import tensorflow as tf
from object_detection.builders import model_builder
from object_detection.utils import config_util
from object_detection.utils import label_map_util

# Setup Paths

CUSTOM_MODEL_NAME = 'my_ssd_mobnet'
LABEL_MAP_NAME = 'label_map.pbtxt'

paths = {

    'SCRIPTS_PATH': os.path.join('Tensorflow', 'scripts'),
    'ANNOTATION_PATH': os.path.join('Tensorflow', 'workspace', 'annotations'),
    'loaded_image_PATH': os.path.join('Tensorflow', 'workspace', 'loaded_images'),
    'CHECKPOINT_PATH': os.path.join('Tensorflow', 'workspace', 'models', CUSTOM_MODEL_NAME),
    # 'OUTPUT_PATH': os.path.join('Tensorflow', 'workspace','models',CUSTOM_MODEL_NAME, 'export'),

}

files = {
    'PIPELINE_CONFIG': os.path.join('Tensorflow', 'workspace', 'models', CUSTOM_MODEL_NAME, 'pipeline.config'),
    'LABELMAP': os.path.join(paths['ANNOTATION_PATH'], LABEL_MAP_NAME)
}


# for path in paths.values():
# if not os.path.exists(path):
# if os.name == 'posix':
# get_ipython().system('mkdir -p {path}')
# if os.name == 'nt':
# get_ipython().system('mkdir {path}')


# Load Train Model From Checkpoint

def numberplate_recognition(loaded_image):
    # Load pipeline config and build a detection model
    configs = config_util.get_configs_from_pipeline_file(files['PIPELINE_CONFIG'])
    detection_model = model_builder.build(model_config=configs['model'], is_training=False)

    # Restore checkpoint
    ckpt = tf.compat.v2.train.Checkpoint(model=detection_model)
    ckpt.restore(os.path.join(paths['CHECKPOINT_PATH'], 'ckpt-11')).expect_partial()

    # Detect from an loaded_image

    def detect_fn(loaded_image):
        loaded_image, shapes = detection_model.preprocess(loaded_image)
        prediction_dict = detection_model.predict(loaded_image, shapes)
        detections = detection_model.postprocess(prediction_dict, shapes)
        return detections

    category_index = label_map_util.create_category_index_from_labelmap(files['LABELMAP'])

    # test_loaded_image = askopenfilename()

    img = cv2.imread(loaded_image)
    # img = cv2.imread(test_loaded_image)
    # img = cv2.imread(loaded_image_PATH)
    loaded_image_np = np.array(img)
    input_tensor = tf.convert_to_tensor(np.expand_dims(loaded_image_np, 0), dtype=tf.float32)
    detections = detect_fn(input_tensor)

    num_detections = int(detections.pop('num_detections'))
    detections = {key: value[0, :num_detections].numpy()
                  for key, value in detections.items()}
    detections['num_detections'] = num_detections

    # detection_classes should be ints.
    detections['detection_classes'] = detections['detection_classes'].astype(np.int64)

    label_id_offset = 1
    loaded_image_np_with_detections = loaded_image_np.copy()
    detection_threshold = 0.7

    loaded_image = loaded_image_np_with_detections
    scores = list(filter(lambda x: x > detection_threshold, detections['detection_scores']))
    boxes = detections['detection_boxes'][:len(scores)]
    classes = detections['detection_classes'][:len(scores)]

    width = loaded_image.shape[1]
    height = loaded_image.shape[0]

    # Apply ROI filtering and OCR
    for idx, box in enumerate(boxes):
        # print(box)
        roi = box * [height, width, height, width]
        # print(roi)
        region = loaded_image[int(roi[0]):int(roi[2]), int(roi[1]):int(roi[3])]
        reader = easyocr.Reader(['en'])
        ocr_result = reader.readtext(region)
        # print(ocr_result)
        # plt.imshow(cv2.cvtColor(region, cv2.COLOR_BGR2RGB))

    # for result in ocr_result:
    # #print(np.sum(np.subtract(result[0][2],result[0][1])))
    # #print(result[1])
    
    # updated this value from 0.06 for better detection results
    region_threshold = 0.06

    def filter_text(region, ocr_result, region_threshold):
        rectangle_size = region.shape[0] * region.shape[1]

        plate = []
        for result in ocr_result:
            length = np.sum(np.subtract(result[0][1], result[0][0]))
            height = np.sum(np.subtract(result[0][2], result[0][1]))

            if length * height / rectangle_size > region_threshold:
                plate.append(result[1])
        return plate

    def ocr_it(loaded_image, detections, detection_threshold, region_threshold):

        # Scores, boxes and classes above threhold
        scores = list(filter(lambda x: x > detection_threshold, detections['detection_scores']))
        boxes = detections['detection_boxes'][:len(scores)]
        classes = detections['detection_classes'][:len(scores)]

        # Full loaded_image dimensions
        width = loaded_image.shape[1]
        height = loaded_image.shape[0]

        # Apply ROI filtering and OCR
        for idx, box in enumerate(boxes):
            roi = box * [height, width, height, width]
            region = loaded_image[int(roi[0]):int(roi[2]), int(roi[1]):int(roi[3])]
            reader = easyocr.Reader(['en'])
            ocr_result = reader.readtext(region)

            text = filter_text(region, ocr_result, region_threshold)

            # plt.imshow(cv2.cvtColor(region, cv2.COLOR_BGR2RGB))
            # plt.show()
            # print(text)
            return text, region

    # Error code with Exclamation mark that is not allowed in number plate
    error_code = "!error"

    # Check to ensure capture the number plate region
    try:
        text, region = ocr_it(loaded_image_np_with_detections, detections, detection_threshold, region_threshold)

    except TypeError as err:
        print("Error: {0}".format(err))
        return error_code

    # Check to ensure it is string
    try:
        final_numberplate = text[0]

    except IndexError as err:
        print("Error: {0}".format(err))
        return error_code

    # Remove potential incorrect character
    disallowed_characters = ",'.-_[]"

    for character in disallowed_characters:
        final_numberplate = final_numberplate.replace(character, "")

    # Remove white space and convert all to upper case letter
    final_numberplate = final_numberplate.replace(" ", "")
    final_numberplate = final_numberplate.upper()

    # print(final_numberplate)
    return final_numberplate
