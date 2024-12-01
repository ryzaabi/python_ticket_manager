from datetime import datetime, timedelta

def calculate_expiry(validity):
    """
    Calculate the expiry date based on a validity string (e.g., "1 day", "2 months").
    
    Args:
        validity (str): The validity period in the format "<number> <unit>".
    
    Returns:
        str: Expiry date as a formatted string (YYYY-MM-DD HH:MM:SS).
        str: Error message if validity is invalid.
    """
    # Parse the validity string
    validity_parts = validity.split()
    if len(validity_parts) != 2 or not validity_parts[0].isdigit():
        return None, "Invalid validity format. Use '<number> <unit>' (e.g., '1 day', '2 months')."

    number = int(validity_parts[0])
    unit = validity_parts[1].lower()

    # Calculate the expiry date based on the unit
    expiry_date = datetime.now()
    if unit in ["day", "days"]:
        expiry_date += timedelta(days=number)
    elif unit in ["month", "months"]:
        expiry_date += timedelta(days=number * 30)  # Approximate a month as 30 days
    elif unit in ["year", "years"]:
        expiry_date += timedelta(days=number * 365)  # Approximate a year as 365 days
    else:
        return None, "Invalid unit. Use 'days', 'months', or 'years'."

    return expiry_date.strftime("%Y-%m-%d %H:%M:%S"), None
