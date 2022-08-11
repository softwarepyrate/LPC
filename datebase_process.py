from datetime import datetime

import mysql.connector
from mysql.connector import Error
from tabulate import tabulate

# mysql database details
USER_NAME = 'digitek'
USER_PASSWORD = 'paper168@'
HOST_NAME = '171.22.109.45'
DATABASE_NAME = 'digitek_csu2022'


# Create database connection
def db_connection(user_name, user_password, host_name, database_name):
    """
    Create MySql database connection
    :param user_name: db's user name
    :param user_password: db's login password
    :param host_name: db's host address
    :param database_name: db name
    :return: database connection for generating cursor
    """

    connection = None

    try:
        connection = mysql.connector.connect(
            user=user_name,
            password=user_password,
            host=host_name,
            database=database_name)

    except Error as error_message:
        print(f"Error: '{error_message}'")

    return connection


# Connect to the database and generate cursor for the functions below
test_connect = db_connection(USER_NAME, USER_PASSWORD, HOST_NAME, DATABASE_NAME)


# This function is to ask user input a date to generate a report
def export_report(calendar_date):
    """
    Export .txt file for selected date's report with details of ID, vehicle's number plate, entry and exit time
    :param calendar_date: String, User selected date
    :return: String, Result to be displayed in GUI
    """
    # Instantiate MySql database cursor
    test_cursor = test_connect.cursor()
    # SQL execution
    test_cursor.execute("SELECT * FROM Test WHERE Entry_Time LIKE %s", ("%" + calendar_date + "%",))

    # Result from query
    carpark_report = test_cursor.fetchall()

    # Result is empty
    if test_cursor.rowcount == 0:

        result_text = "Sorry, no record found. Please try different date."

    else:

        # Generate timestamp and filename for the report
        filename_timestamp = datetime.now().strftime("%Y%m%d%H%M")

        filename = calendar_date + '-report_' + filename_timestamp + '.txt'

        # Save the report by using external package - tabulate
        with open(filename, 'w') as f:
            f.write(
                tabulate(carpark_report, headers=['ID', 'Number Plate', 'Entry Time', 'Exit Time'], tablefmt='psql'))

        # Display message
        result_text = "Report [" + filename + "] generated"

    # Close the cursor
    test_cursor.close()

    return result_text


# This function is to save the number plate into database
def save_datetime(number_plate, direction):
    """
    Create system local timestamp and save it into table's entry or exit time
    :param number_plate: String, vehicle's number plate reading
    :param direction: Integer - 1 for entry and 0 for exit
    :return: Timestamp string for direction 1, Timestamp string and Python Datatime object for direction 0
    """

    # Get the current date time
    entry_datetime = datetime.now()

    # Format the datatime object
    formatted_datetime = entry_datetime.strftime('%Y-%m-%d %H:%M:%S')
    test_cursor = test_connect.cursor()
    if direction == 1:
        test_cursor.execute('INSERT INTO Test(Number, Entry_Time) VALUES (%s, %s)',
                            (number_plate, formatted_datetime))

        # Save the execution
        test_connect.commit()

        # Feedback in Python
        print("Number plate" + number_plate + " 's entry time has been saved into database")

        return formatted_datetime

    else:
        test_cursor.execute('UPDATE Test SET Exit_Time = %s WHERE Number = %s',
                            (formatted_datetime, number_plate))

        # Save the execution
        test_connect.commit()

        # Feedback in Python
        print("Number plate " + number_plate + "'s exit time has been saved into database")

        # Create Python Datetime object
        exit_datatime = datetime.strptime(formatted_datetime, '%Y-%m-%d %H:%M:%S')

        return formatted_datetime, exit_datatime

    # Close the cursor
    test_cursor.close()


# This function is to export the number plate's entry date and time
def export_entry_datetime(number_plate):
    """
    Output the vehicle entry time for calculating the parking fee in module fee.py
    :param number_plate: String, vehicle's number plate reading
    :return: Python Datatime object for calculation
    """
    test_cursor = test_connect.cursor()
    # Execute the statement
    test_cursor.execute("SELECT Entry_Time FROM Test WHERE Number = %s", (number_plate,))

    # Get the output from query
    test_str = str(test_cursor.fetchone())

    # Striped unnecessary characters
    new_string = test_str[2:21]

    # Create Python datatime object
    created_date = datetime.strptime(new_string, '%Y-%m-%d %H:%M:%S')

    # Close the cursor
    test_cursor.close()

    return created_date
