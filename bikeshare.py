import time
import pandas as pd
import numpy as np
# numpy has not been used.
# all of the user input and calculated data will be printed to show the user his inputs and results.
# all user input will be converted into lower for standardization.  
# all the data output will be displayed in a good looking format for a better readability.

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
        
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    # cities from dict are printed to show options for the user.          
    print('You can analyze the following city\'s:')
    for ct,cc in CITY_DATA.items():
        print('   {}'.format(ct))
        
    # pre-define city as an empty string for the upcoming while loop.    
    city = str( )
    
    # while-loop to ask for the users choice of city from the list.
    # if the user input does not fit the citylist he will get a notification and has to repeat his input.      
    while True:
        city = input('Which city do you want to analyze?: ').lower()
        if city not in CITY_DATA.keys():
            print('\nWrong Input!\n')
            continue
        else:
            break
       
                          
    # creating a list for months and days including all.
    # pre-define month and day as an empty string for the upcoming while loop.
    # if the user input does not fit the month and day data he will get a notification and has to repeat his input.
    MONTH_DATA = ['all','january','february','march','april','may','june']
    DAY_DATA = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    month = str()
    day = str()
    
    # get user input for month (all, january, february, ... , june)
    # months are printed to show options for the user including 'all'.
    while month not in MONTH_DATA:
        print('\nWhich month do you want to analyze? ')
        for mo in MONTH_DATA:
                print('   {}'.format(mo))        
        month = input('Please select a filter from the list: ').lower()
        if month not in MONTH_DATA:
            print('\nIWrong Input!\n')
        else:
            break
    
    # get user input for day of week (all, monday, tuesday, ... sunday)
    # days are printed to show options for the user including 'all'.
    while day not in DAY_DATA:
        print('\nWhich day do you want to analyze?: ')
        for da in DAY_DATA:
                print('   {}'.format(da))        
        day = input('Please select a filter from the list: ').lower()
        if day not in DAY_DATA:
            print('\nWrong Input!\n')
        else:
            break
    
    # print the selected filters for confirmation to the user.
    print('You selected: ')
    print(city)
    print(month)
    print(day)
    
    
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
    # load csv data for the selected city by user.
    df = pd.read_csv(CITY_DATA[city])

    # create columns for start time, month and day of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day of week'] = df['Start Time'].dt.day_name()

    # if filtered by month
    if month != 'all':
        months = ['january','february','march','april','may','june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # if filtered by day
    if day != 'all':
        df = df[df['day of week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # display the most common month
    c_month = df['month'].mode()[0]
    print('\nMost common month as number:')
    print(c_month)

    # display the most common day of week
    c_day = df['day of week'].mode()[0]
    print('\nMost common day of week:')
    print(c_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    c_hour = df['hour'].mode()[0]
    print('\nMost common start hour:')
    print(c_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    c_start = df['Start Station'].mode()[0]
    print('\nMost common start station:')
    print(c_start)

    # display most commonly used end station
    c_end = df['End Station'].mode()[0]
    print('\nMost common end station:')
    print(c_end)

    # display most frequent combination of start station and end station trip
    df['Combination'] = df['Start Station'] + ' - ' + df['End Station']
    comb_start_end = df['Combination'].mode()[0]
    print('\nMost frequent combination of start and end station:')
    print(comb_start_end)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    ttt = df['Trip Duration'].sum()
    print('\nTotal travel time:')
    print(ttt)

    # display mean travel time
    mtt = df['Trip Duration'].mean()
    print('\nMean travel time:')
    print(mtt)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    # displayed by Subscriber or Customer
    user_types = df['User Type'].value_counts()
    print('\n',user_types)

    # Display counts of gender
    # displayed by Male or Female
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print('\n',gender)
    else:
        print('\nNo information about gender available.')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest = df['Birth Year'].min()
        print('\nEarliest year of birth:')
        print(earliest)
        recent = df['Birth Year'].max()
        print('\nRecent year of birth:')
        print(recent)
        common_birth_year = df['Birth Year'].mode()[0]
        print('\nMost common year of birth:')
        print(common_birth_year)
        
    else:
        print('\nNo information about birth year available.')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    """
    Asks user if he would like to display 5 rows of raw data from his filters.
    User has the option to display more raw data or continue.
    """
    # pre-define answer options, raw_data1 and a counter for upcoming while loop.
    # creating a list for months and days including all.
    # pre-define month and day as an empty string for the upcoming while loop.
    # if the user input does not fit the month and day data he will get a notification and has to repeat his input.
    Choices = ['yes','no']
    raw_data1 = str()
    row_count = 0
    
    # while loops to check if the user wants to display raw data and if he wants to repeat that.
    while raw_data1 not in Choices:
        raw_data1 = input('\nLike to see 5 rows of the raw data?  yes / no :\n').lower()
        if raw_data1 == 'yes':
            print(df.head())
        elif raw_data1 not in Choices:
            print('\nWrong Input!\n')
              
     
    while raw_data1 == 'yes':
        raw_data2 = input('Like to see 5 more rows of raw data?  yes / no :\n').lower()
        row_count += 5
        if raw_data2 == 'yes':
            print(df[row_count:row_count+5])
        elif raw_data2 == 'no':
            break
        elif raw_data2 not in Choices:
            print('\nWrong Input!\n')
    

    print('-'*40)
        

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nLike to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
