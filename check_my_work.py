def format_temperature(temp):
    value = int(temp)
    return f"{value} °C"

print(format_temperature("23"))


#     """Takes a temperature and returns it in string format with the degrees
#         and Celcius symbols.

#     Args:
#         temp: A string representing a temperature.
#     Returns:
#         A string contain the temperature and "degrees Celcius."
#     """
# # provide a temperature 
# # show that temperature back as a string ""
# # the temperature variable is going to be a string that is a temperature (23)
# # and i need to show it like 23 degreed celcius


def convert_date(iso_string):

#provide an ISO string format 
#convert it into human-readable format
#show it as a human-readable format

    """Converts an ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string. DD/MM/YYY
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
