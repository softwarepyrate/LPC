import datetime
import math

# This is constant hourly rate for calculation
HOURLY_RATE = 8


# This function to calculate the fee
def fee_calculation(entry_datetime, exit_datetime):
    """
    Create MySql database connection
    :param entry_datetime: Vehicle entry time - Python Datatime object
    :param exit_datetime: Vehicle exit time - Python Datatime object
    :return: Int, parking fee
    """

    # Calculate the time difference
    delta = exit_datetime - entry_datetime

    # Convert to actual hours
    parking_actual_hours = delta.total_seconds() / (60 * 60)

    # This is the charge hours
    charge_hours = math.ceil(parking_actual_hours)

    # Calculate the fee
    parking_fee = HOURLY_RATE * charge_hours

    return parking_fee
