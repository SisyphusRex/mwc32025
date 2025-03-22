import csv
import sys
from geopy.distance import geodesic


def read_csv(filename,mode_type):
    """Reads csv file and puts the data into an array of arrays."""
    results = []
    with open(filename,mode = mode_type) as file:
        csvfile = csv.reader(file)
        for row in csvfile:
            results.append(row)
    return results
def prompt_user_to_read_csv():
    """Prompts user at CMD line for file name and mode"""
    try:
        filename= sys.argv[1]
        mode_type = sys.argv[2]
    except Exception:
        print("Missing arguments.")
        return 0
    zip_information = read_csv(filename,mode_type)
    print(zip_information)   


def calculate_distance_between_two_zipcodes(zip_array,coords1,coords2): 
    """Calculates the distance between two given zip codes. Coords 1 and 2 must be tuples. """
    distance = geodesic(coords1,coords2).miles

    return distance




if __name__ == '__main__':
    prompt_user_to_read_csv()
