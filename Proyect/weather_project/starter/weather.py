import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):

    date=datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")

    new_date=date.strftime("%A %d %B %Y")
    return new_date
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    # code
    #return iso_string






def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    
    temp=round((float(temp_in_farenheit)-32)*5/9,1)
    
    return (temp)

def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    sum_value=0

    for value in weather_data:
        sum_value += float(value)
    
    mean = sum_value/len(weather_data)

    return (mean)


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    list=[]

    with open(csv_file) as csv_1:
       csv_out = csv.reader(csv_1) 
       next(csv_out)
       for rows in csv_out: 
           if len(rows) != 0:
            list.append([rows[0],int(rows[1]),int(rows[2])])
    
    return (list)


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    if len(weather_data) == 0:
        return()

    value = float(weather_data[0])
    position = 0

    for index, weather in enumerate(weather_data):
        if float(weather) <= value:
            value= float(weather)
            position = index

    return(value, position)



def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    if len(weather_data) == 0:
        return()

    value = float(weather_data[0])
    position = 0

    for index, weather in enumerate(weather_data):
        if float(weather) >= value:
            value= float(weather)
            position = index

    return(value, position)


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
#     5 Day Overview
#   The lowest temperature will be 9.4°C, and will occur on Friday 02 July 2021.
#   The highest temperature will be 20.0°C, and will occur on Saturday 03 July 2021.
#   The average low this week is 12.2°C.
#   The average high this week is 17.8°C.


    Number_of_days=0
    Min_Value=[]
    Date_value=[]
    Max_Value=[]


    for rows in weather_data: 
        if len(rows) != 0:
            Number_of_days = Number_of_days + 1
            Min_Value.append(rows[1])
            Date_value.append(str(rows[0]))
            Max_Value.append(rows[2])
    
    min_temperature,min_position = find_min(Min_Value)
    min_tempe_celcius = convert_f_to_c(min_temperature)
    occur_date_min = convert_date(Date_value[min_position])
    max_temperature,max_position = find_max(Max_Value)
    max_tempe_celcius = convert_f_to_c(max_temperature)
    occur_date_max = convert_date(Date_value[max_position])
    mean_low = calculate_mean(Min_Value)
    mean_low__tempe_celcius = convert_f_to_c(mean_low)
    mean_high = calculate_mean(Max_Value)
    mean_high__tempe_celcius = convert_f_to_c(mean_high)

    summary=""
    summary+=f"{Number_of_days} Day Overview\n"
    summary+=f"  The lowest temperature will be {format_temperature(min_tempe_celcius)}, and will occur on {occur_date_min}.\n"
    summary+=f"  The highest temperature will be {format_temperature(max_tempe_celcius)}, and will occur on {occur_date_max}.\n"
    summary+=f"  The average low this week is {format_temperature(mean_low__tempe_celcius)}.\n"
    summary+=f"  The average high this week is {format_temperature(mean_high__tempe_celcius)}.\n"

    return summary


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    summary = ""

    for rows in weather_data: 
            summary+= f"---- {convert_date(rows[0])} ----\n"
            summary+= f"  Minimum Temperature: {format_temperature(convert_f_to_c(int(rows[1])))}\n "
            summary+= f" Maximum Temperature: {format_temperature(convert_f_to_c(int(rows[2])))}\n"
            summary+= f"\n"
           
    return summary
