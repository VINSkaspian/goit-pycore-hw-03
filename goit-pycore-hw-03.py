from datetime import datetime 
     
def get_days_from_today(date):
    """
    Calculates the number of days between a given date and the current date.

    Parameters:
    date (str): A date in the format 'YYYY-MM-DD', for example, '2020-10-09'.
    
    Returns:
    int: The number of days between the current date and the given date. Negative if the date is in the future.
    
    Exceptions:
    ValueError: If the input date is in an invalid format.
    """     
    try:
        # Transform line to date
        target_date = datetime.strptime(date, '%Y-%m-%d').date()
        # Get the current date
        today = datetime.today().date()
        # Calculate the difference
        delta = today - target_date
        return delta.days
    except ValueError:
        raise ValueError("Date must be in format 'YYYY-MM-DD'")


