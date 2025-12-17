import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    # Step 1: Convert the ISO datetime string into a datetime object
    # Example input: "2024-02-29T07:00:00+08:00"
    d = datetime.fromisoformat(iso_string)

    # Step 2: Format the datetime into "Weekday DD Month YYYY"
    # %A = weekday name, %d = day (2 digits), %B = full month name, %Y = 4-digit year
    return d.strftime("%A %d %B %Y")

print (convert_date("2024-02-29T07:00:00+08:00"))



def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    temp_in_fahrenheit = float(temp_in_fahrenheit)
    celsius_temp = (temp_in_fahrenheit - 32) * (5/9)
    return round(celsius_temp, 1)
print (convert_f_to_c(106))



#Celsius (°C) = (Fahrenheit (°F) - 32) × 1.8.


def calculate_mean(weather_data):
    weather_data = [float(value) for value in weather_data]
    count = len (weather_data)
    mean_value = sum (weather_data) / (count)
    return (mean_value)

print (calculate_mean([10, 42.3 ,87 , 76.4, 23]))

""""
    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """



def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    data = []
    with open(csv_file, encoding="utf-8") as example_one:
        reader = csv.reader(example_one)

        next(reader)  # dont look at the header row

        for row in reader: # if the row is empty, the just skip it
            if not row:
                continue

            date = row[0]
            min_temp = int(row[1])
            max_temp = int(row[2])

            data.append([date, min_temp, max_temp])

    return data

rows = load_data_from_csv("tests/data/example_one.csv")
print(rows)
        


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers (as numbers or strings).

    Returns:
        The minimum value (as a float) and its position in the list.
        In case of multiple matches, returns the index of the last example.
        For an empty list, returns ().
    """

    # If the list is empty, return an empty tuple
    if not weather_data:
        return ()

    # Start by assuming the first value is the minimum
    min_value = float(weather_data[0])
    min_index = 0

    # Loop through the list using the index
    for i in range(len(weather_data)):
        value = float(weather_data[i])

        # Use <= so that if the same min appears again,
        # we update to the most recent (last) index
        if value <= min_value:
            min_value = value
            min_index = i

    return min_value, min_index
print(find_min([10, 4, 6, 4, 2, 8, 2]))



def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
        # If the list is empty, return an empty tuple
    if not weather_data:
        return ()

    # Start by assuming the first value is the minimum
    max_value = float(weather_data[0])
    min_index = 0

    # Loop through the list using the index
    for i in range(len(weather_data)):
        value = float(weather_data[i])

        # Use >= so that if the same min appears again,
        # we update to the most recent (last) index
        if value >= max_value:
            max_value = value
            min_index = i

    return max_value, min_index
print (find_max([10, 4, 6, 4, 10, 8, 2]))


def generate_summary(weather_data):
    if not weather_data:
        return ""
# Locate the minimum and maximum temperatures within the list of weather data by indicating where they fall within each list for each day. 
    num_days = len(weather_data)
    min_temps_f = [day[1] for day in weather_data]
    max_temps_f = [day[2] for day in weather_data]

# Find the overall minimum and maximum of all the minimum and maximum temperatures, by using the find_min and find_max functions we created before
    overall_min_f, index_min = find_min(min_temps_f)
    overall_max_f, index_max = find_max(max_temps_f)

# The temperatures are all in farenheit by default, and so we need to convert the overall mins and maxs to celcius
    overall_min_c = convert_f_to_c(overall_min_f)
    overall_max_c = convert_f_to_c(overall_max_f)

# Get the corresponding dates which are in ISO format and convert them to human-readable strings like what we did before
    date_min = convert_date(weather_data[index_min][0])
    date_max = convert_date(weather_data[index_max][0])

 # Convert all min and max temperatures to Celsius for averaging
    min_temps_c = [convert_f_to_c(t) for t in min_temps_f]
    max_temps_c = [convert_f_to_c(t) for t in max_temps_f]

 # Calculate the average low and high in Celsius
    avg_min_c = calculate_mean(min_temps_c)
    avg_max_c = calculate_mean(max_temps_c)

# Round the averages to 1 decimal place to match the style of convert_f_to_c
    avg_min_c = round(avg_min_c, 1)
    avg_max_c = round(avg_max_c, 1)

# Build the lines of the summary text
    lines = [
        f"{num_days} Day Overview",
        f"  The lowest temperature will be {format_temperature(overall_min_c)}, and will occur on {date_min}.",
        f"  The highest temperature will be {format_temperature(overall_max_c)}, and will occur on {date_max}.",
        f"  The average low this week is {format_temperature(avg_min_c)}.",
        f"  The average high this week is {format_temperature(avg_max_c)}.",
        "",  # blank line at the end
    ]

    # Join all the lines together into a single multi-line string
    return "\n".join(lines)

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of
                      weather data in the form:
                      [iso_date_string, min_temp_f, max_temp_f]
    Returns:
        A string containing the daily summary information.
    """

    # If there is no data, just return an empty string
    if not weather_data:
        return ""

    lines = []

    # Go through each day one by one
    for day in weather_data:
        iso_date = day[0]
        min_temp_f = day[1]
        max_temp_f = day[2]

        # Convert the date into a nice human-readable form
        date_str = convert_date(iso_date)

        # Convert min and max temperatures from Fahrenheit to Celsius
        min_temp_c = convert_f_to_c(min_temp_f)
        max_temp_c = convert_f_to_c(max_temp_f)

        # Header line with four dashes and spaces: ---- Friday 02 July 2021 ----
        lines.append(f"---- {date_str} ----")

        # Two spaces before 'Minimum' and 'Maximum'
        lines.append(f"  Minimum Temperature: {format_temperature(min_temp_c)}")
        lines.append(f"  Maximum Temperature: {format_temperature(max_temp_c)}")

        # Blank line after each day's block
        lines.append("")

    # Join everything into one big string AND add one extra newline
    # so the whole summary ends with a blank line
    return "\n".join(lines) + "\n"
