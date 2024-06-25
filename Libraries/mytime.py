from datetime import datetime, timedelta


def get_formatted_time():
    # Get the current time
    current_time = datetime.now()
    # Format the time as a string
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_time


def has_a_second_passed(old_time):
    # Get the current time
    current_time = datetime.now()
    # Calculate the time difference
    difference = current_time - old_time
    # Check if at least three seconds have passed
    return difference >= timedelta(seconds=1)
