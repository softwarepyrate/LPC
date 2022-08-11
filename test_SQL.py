# Import these two modules to test the codes
import datebase_process
import fee

# Test to read number plate and return fee
# test_number_plate = "test2"  # Or please test "test3"
# test_datatime = datebase_process.export_entry_datetime(test_number_plate)
# print(test_datatime)
#
# test_fee = fee.fee_calculation(test_datatime)
#
# print(test_fee)

# Test new nuber plate
# test_number_plate_2 = "test4"
#
# mysql.save_entry_datetime(test_number_plate_2)
#
# test_datatime = datebase_process.export_entry_datetime(test_number_plate_2)
#
# print(test_datatime)
#
# test_fee = fee.fee_calculation(test_datatime)
# #
# print(test_fee)

test_numberplate = "test3"
text_exit = datebase_process.save_datetime(test_numberplate, 0)[1]

print(text_exit)

test_entry = datebase_process.export_entry_datetime(test_numberplate)

test_fee = fee.fee_calculation(test_entry, text_exit)

print(test_fee)
