import csv
from pprint import pprint
def get_country_column(file_name):
    """
    This function takes a filename as input and returns a list of countries
    Args:
        file_name: string
    Returns:
        list
    """
    #countries = []

    file = open(file_name,"r")
    reader = csv.reader(file)
    countries = []
        # Process each row
    for row in list(reader)[1:]:
            # Extract the country from the row
        country = row[3]

            # Add the country to the list if it's not already present
        if country not in countries:
            countries.append(country)

    return countries

file_name = 'data.csv'
countries = get_country_column(file_name)
print(countries)