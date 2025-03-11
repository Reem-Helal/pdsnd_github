import time
import pandas as pd
import numpy as np


CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
    """Prompt the user to input filters for city, month, and day of the week.

    Returns:
        city (str): The city selected for analysis (chicago, new york city, or washington).
        month (str): The month selected for analysis (January to June, or 'none' for no month filter).
        day (str): The day of the week selected for analysis (Monday to Sunday, or 'none' for no day filter).
    """
    print('Greetings! Let\'s dive into some US bikeshare data!')

    cities = ['chicago', 'new york city', 'washington']
    while True:
        city = input("\nWhich city do you want to analyze? (Chicago, New York City, Washington)\n").strip().lower()
        if city in cities:
            break
        print("\nPlease provide a valid city name.")

    months = ['january', 'february', 'march', 'april', 'may', 'june', 'none']
    while True:
        month = input("\nWhich month would you like to analyze? (January to June)? Type 'None' for no month filter\n").strip().lower()
        if month in months:
            break
        print("\nPlease provide a valid month.")

    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'none']
    while True:
        day = input("\nWhich day of the week do you want to analyze? (Monday to Sunday)? Type 'None' for no day filter\n").strip().lower()
        if day in days:
            break
        print("\nPlease provide a valid day.")

    print('-' * 40)
    return city, month, day

def load_data(city, month, day):
    """Load and filter the bikeshare data based on the user inputs (city, month, day).

    Args:
        city (str): The city for which to load the data.
        month (str): The month to filter the data (e.g., 'january', 'none').
        day (str): The day of the week to filter the data (e.g., 'monday', 'none').

    Returns:
        df (DataFrame): A pandas DataFrame containing the filtered bikeshare data.
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()

    if month != 'none':
        months_list = ['january', 'february', 'march', 'april', 'may', 'june']
        month_index = months_list.index(month) + 1
        df = df[df['month'] == month_index]

    if day != 'none':
        df = df[df['day_of_week'] == day]

    return df

def time_stats(df, month, day):
    """Display statistics on the most frequent times of travel (month, day, hour).

    Args:
        df (DataFrame): A pandas DataFrame containing the filtered bikeshare data.
        month (str): The month selected for analysis.
        day (str): The day of the week selected for analysis.
    """
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    if month == 'none':
        popular_month = df['month'].mode()[0]
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        print("The most popular month is", months[popular_month - 1])

    if day == 'none':
        popular_day = df['day_of_week'].mode()[0]
        print("The most popular day is", popular_day.title())

    df['Start Hour'] = df['Start Time'].dt.hour
    popular_hour = df['Start Hour'].mode()[0]
    print("The most popular start hour is {}:00 hrs".format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def station_stats(df):
    """Display statistics on the most popular stations and trip routes.

    Args:
        df (DataFrame): A pandas DataFrame containing the filtered bikeshare data.
    """
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    most_common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is {}".format(most_common_start_station))

    most_common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is {}".format(most_common_end_station))

    df['route'] = df['Start Station'] + " to " + df['End Station']
    most_frequent_route = df['route'].mode()[0]
    print("The most frequent combination of stations is {} ".format(most_frequent_route))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def trip_duration_stats(df):
    """Display statistics on the total and average trip duration.

    Args:
        df (DataFrame): A pandas DataFrame containing the filtered bikeshare data.
    """
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_duration = df['Trip Duration'].sum()
    hours, remaining_seconds = divmod(total_duration, 3600)
    minutes, seconds = divmod(remaining_seconds, 60)
    print("Total trip duration: {} hour(s) {} minute(s) {} second(s)".format(hours, minutes, seconds))

    average_duration = round(df['Trip Duration'].mean())
    avg_minutes, avg_seconds = divmod(average_duration, 60)
    if avg_minutes >= 60:
        avg_hours, avg_minutes = divmod(avg_minutes, 60)
        print("Average trip duration: {} hour(s) {} minute(s) {} second(s)".format(avg_hours, avg_minutes, avg_seconds))
    else:
        print("Average trip duration: {} minute(s) {} second(s)".format(avg_minutes, avg_seconds))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def user_stats(df, city):
    """Display statistics on bikeshare users, including user type, gender, and birth year.

    Args:
        df (DataFrame): A pandas DataFrame containing the filtered bikeshare data.
        city (str): The city selected for analysis, used to filter gender and birth year information.
    """
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_types_count = df['User Type'].value_counts().to_dict()
    print("User type counts:\n", user_types_count)

    if city in ['chicago', 'new york city']:
        gender_count = df['Gender'].value_counts().to_dict()
        print("\nGender counts:\n", gender_count)

        earliest_birth_year = int(df['Birth Year'].min())
        print("\nThe oldest user was born in the year", earliest_birth_year)
        most_recent_birth_year = int(df['Birth Year'].max())
        print("The youngest user was born in the year", most_recent_birth_year)
        common_birth_year = int(df['Birth Year'].mode()[0])
        print("Most users were born in the year", common_birth_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def display_data(df):
    """Display 5 rows of raw data at a time based on user input.

    Args:
        df (DataFrame): A pandas DataFrame containing the filtered bikeshare data.
    """
    start_index = 0
    user_input = input('Would you like to display 5 rows of raw data? ').lower()
    while user_input in ['yes', 'y', 'yep', 'yea'] and start_index + 5 < df.shape[0]:
        print(df.iloc[start_index:start_index + 5])
        start_index += 5
        user_input = input('Would you like to display another 5 rows of raw data? ').lower()

def main():
    """Main function to orchestrate the bikeshare data analysis process.

    Loops through the process of getting user input, loading the data, calculating stats, 
    and displaying results. Optionally restarts the analysis based on user input.
    """
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)

        restart_choice = input('\nWould you like to restart? Enter yes or no.\n').strip().lower()
        if restart_choice != 'yes':
            break

if __name__ == "__main__":
    main()