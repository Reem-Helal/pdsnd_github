Basic Data Exploration with Pandas on Bikeshare Data:
Date Created
February 18th, 2025

Project Title
Bikeshare Data Analysis
The program interacts with the user to specify the data to analyze.  It prompts the user for the following information:

City: (Chicago, New York City, or Washington)
Month: (e.g., January, February, ..., June, or "all")
Day of Week: (e.g., Monday, Tuesday, ..., Sunday, or "all")
After receiving this input, the program asks if the user wants to view 5 lines of the raw data.  Based on the user's responses, the program calculates and displays the following descriptive statistics:

Most popular month
Most popular day of the week
Most popular hour of the day
Most popular start station
Most popular end station
Most popular combination of start and end stations
Total trip duration
Average trip duration
Counts of user types
Counts of user genders (if available in the dataset)
Oldest user's age (if available in the dataset)
Youngest user's age (if available in the dataset)
Most common birth year (if available in the dataset)
Finally, the program asks the user if they would like to restart the analysis or exit.

Requirements
Python 3.6 or above
pandas
numpy
time
Project Data
The project uses the following datasets, provided by Udacity and located in the data/ directory:

chicago.csv: Bikeshare data for Chicago.
new_york_city.csv: Bikeshare data for New York City.
washington.csv: Bikeshare data for Washington D.C. Note: The Washington dataset does not include "Gender" or "Birth Year" information.
