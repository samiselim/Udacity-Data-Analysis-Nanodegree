import time
import pandas as pd
import numpy as np
from statistics import mode

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june']

def get_filters():
    
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Enter the city : (chicago, new york city, washington) --> ').lower()
    while True:
            if city == 'chicago' or city == 'new york city' or city == 'washington':
                break;
            else:
                city = input('-- Please Enter valid City Name -- \nEnter the City : (chicago, new york city, washington) --> ').lower()

        # get user input for month (all, january, february, ... , june)
    month = input('Select the month (all, january, february, ... , june)  : ').lower()

        # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Select the day (all, monday, tuesday, ... sunday) : ').lower()

    print('-'*40)
    return city, month, day



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        
        month  = months.index(month) + 1
        df = df[df['month'] == month]


    if day != 'all':
        df = df[df['day'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('\nThe most common month : {}'.format(months[df['month'].mode()[0]-1]))

    # TO DO: display the most common day of week
    print('\nThe most common day of week : {}'.format(df['day'].mode()[0]))

    # TO DO: display the most common start hour
    print('\nThe most common strat hour : {}'.format((df['Start Time'].dt.hour).mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('\nThe most common used start station : {}'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('\nThe most common used end station {}'.format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    Src_Dis_list = []
    
    for i in range(len(df['Start Station'])):
        Src_Dis_list.append((df.iloc[i,4] , df.iloc[i,5]))
        
        
    print('\nThe most frequent combination of start station and end station trip : {}'.format(mode(Src_Dis_list)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('\ntotal travel time : {}'.format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('\nAverage travel time : {}'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\nCounts of user types {}'.format(df['User Type'].value_counts()))
    # TO DO: Display counts of gender
    try:
        print('\nCounts of gender {}'.format(df['Gender'].value_counts()))

        # TO DO: Display earliest, most recent, and most common year of birth
        print('\nEarliest Birth Year : {}'.format(df['Birth Year'].min()))

        print('\nMost Recent Birth Year : {}'.format(df['Birth Year'].max()))

        print('\nMost common Birth Year : {}'.format(df['Birth Year'].mode()))
    except:
        print('There is no information about Gender and Birth Year')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        start = -5
        end = 0
        while True:
            raw_d = input('Do you Need to display the first 5 raw data ?! say yes or no ').lower()
            if raw_d == 'yes':
                start = start + 5
                end = end + 5
                print(df[start:end])
            else:
                break;

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        


if __name__ == "__main__":
	main()
