# Udacity - Programming from data science - Introduction to Python
# Modifications required for Version Control Lesson

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv', 'new york': 'new_york_city.csv', 'washington': 'washington.csv' }

def get_filters():
    """ Asks user to specify a city, month, and day to analyze.
    Returns:
    (str) city - name of the city to analyze
    (str) month - name of the month to filter by, or "all" to apply no month filter
    (str) day - name of the day of week to filter by, or "all" to apply no day filter """
    print('\nHello! Let\'s explore some US bikeshare data!')
    # Validating city
    while True:
        city = input('Would you like to see data from Chicago, New York, or Washington? ')
        if city.lower() not in CITY_DATA:
            print('*** ERROR: Not a valid city. Please check spelling and input again.')
        else:
            break
    # Validating month
    while True:
        month = input('Which month? January, February, March, April, May, June, or All? ')
        if month.lower() not in ('january' , 'february' , 'march' , 'april' , 'may' , 'june' , 'all'):
            print('*** ERROR: Not a valid month. Please check spelling and input again.')
        else:
            break
    # Validating day
    while True:
        day = input('Which day of the week? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or All? ')
        if day.lower() not in ('monday' , 'tuesday' , 'wednesday' , 'thursday' , 'friday' , 'saturday' , 'sunday' , 'all'):
            print('*** ERROR: Not a valid day of the week.')
        else:
            break
    return city, month, day

def load_data(city, month, day):
    """ Loads data for the specified city and filters by month and day if applicable.
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
        Returns:
        df - Pandas DataFrame containing city data filtered by month and day"""
    # Reading file and assigning data frames
    df = pd.read_csv(CITY_DATA[city.lower()])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    if month.lower() != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month.lower()) + 1
        df = df[df['month'] == month]
    if day.lower() != 'all':
        df = df[df['day'] == day.title()]
    return df

def time_stats(df):
    """#1 Popular times of travel (i.e., occurs most often in the start time)"""
    print('\nPopular times of travel...')
    start_time = time.time()
    # Calculating popular times of travel
    print('Most common month:\n', [df['month'].mode()])
    print('Most common day of week:\n', [df['day'].mode()])
    print('Most common hour of day:\n', [df['hour'].mode()])
    print("This took %s seconds." % (time.time() - start_time))

def station_stats(df):
    """#2 Popular stations and trip"""
    print('\nPopular stations and trip...')
    start_time = time.time()
    #Calculating popular stattions and trips
    print('Most common start station:\n', [df['Start Station'].mode()])
    print('Most common end station:\n', [df['End Station'].mode()])
    # Concatenating 'Start and End stations in variable'
    most_frequent_combo = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print('Most common trip from start to end:\n', most_frequent_combo)
    print("This took %s seconds." % (time.time() - start_time))

def trip_duration_stats(df):
    """#3 Trip duration"""
    print('\nTrip durationn...')
    start_time = time.time()
    # Calculating trip durations
    print('Total travel time:\n', [df['Trip Duration'].sum()])
    print('Average travel time:\n', [df['Trip Duration'].mean()])
    print("This took %s seconds." % (time.time() - start_time))

def user_stats(df, city):
    """#4 User info"""
    print('\nUser info"...')
    start_time = time.time()
    # Calculating user infroamtion
    print('Counts of each user type:\n', df['User Type'].value_counts())
    # Gender and birth date are not available for Washington
    if city.lower() != 'washington':
        #genders = df['Gender'].value_counts()
        print('\nCounts of each gender:\n', df['Gender'].value_counts())
        print('\nEarliest birth year:', int(df['Birth Year'].min()))
        print('Most recent birth year: ', int(df['Birth Year'].max()))
        print('Most common: ', int(df['Birth Year'].mode()))
    print('This took %s seconds.' % (time.time() - start_time))

def ind_trip(df):
    """ #5 individual trip display """
    i = 0
    j = 1
    while True:
        # Loop to validate if the user wants to continue displaying trip details
        ind_trip = input('\nWould you like to see individual trip details? Enter (yes) to continue or (no) to finish? ')
        if ind_trip.lower() == 'yes':
            print(df.iloc[ (i * 5) : (j * 5) , 3:])
            # I selected only to display from the 3rd column to the end
            # if only wanted to select the start and end stations the last parameter should be 4:5] instead of 3:]
            i = i + 1
            j = j + 1
        elif ind_trip.lower() == 'no':
            break
        else:
            print('*** ERROR: Not a valid answer')

def main():
    # Main funciton that will call the aboe mentioned Functions
    city, month, day = get_filters()
    df = load_data(city, month, day)
    time_stats(df)
    station_stats(df)
    trip_duration_stats(df)
    user_stats(df, city)
    ind_trip(df)


while True:
    # While loop to validate program iteration
    start = input('\nWould you like to start? Enter (yes) to continue or (no) to finish? ')
    if start.lower() == 'yes':
        main()
    elif start.lower() == 'no':
        break
    else:
        print('*** ERROR: Not a valid answer')

print ('\nThank you.....have a nice day!!!')
