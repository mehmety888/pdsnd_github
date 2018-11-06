import time
import pandas as pd

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
    months = ['all','january', 'february', 'march', 'april', 'may', 'june','july','august','september','october','november','december',]
    days=['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while (True):
        city=input("Enter one of the cities to analyze: chicago, new york city or washington\n").lower()
        if city in CITY_DATA:
            print("So you want to analyze: {}".format(city))
            break
        else:
            print("We have no bikeshare data for that city\nPlease pick one of the cities: chicago, new york city, washington")
            print('-'*40)
    # TO DO: get user input for month (all, january, february, ... , june)
    while (True):
        month=input("Enter the name or number of a month to filter. ex:january,4 ... if you don't want to filter; write 'all'\n").lower()
        if month in months:
           print("So you want to filter data by: {}".format(month))
           break
        else:
            try:
                month=int(month)
                if 1<=month<=12:
                    month=months[month]
                    print("So you want to filter data by: {}".format(month))
                    break
                else:
                    print("It is not a month. Please write a month name in Gregorian Calendar!")
                    print('-'*40)
            except:
                print("It is not a month. Please write a month name in Gregorian Calendar!")
                print('-'*40)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while (True):
        day=input("Enter the name or number of a day of week to analyze ex:monday,2 ... if you don't want to filter; write 'all'\n").lower()
        if day in days:
           print("So you want to filter data by: {}".format(day))
           break
        else:
            try:
                day=int(day)
                if 1<=day<=7:
                    day=days[day]
                    print("So you want to filter data by: {}".format(day))
                    break
                else:
                    print("It is not a day. Please write a week day in English!")
                    print('-'*40)
            except:
                print("It is not a day. Please write a week day in English!")
                print('-'*40)

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] =df['Start Time'].dt.weekday_name
    df['hour'] =df['Start Time'].dt.hour
    # filter by month
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june','july','august','september','october','november','december']
        month = months.index(month)+1

        # filter by month to create the new dataframe
        df = df[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    months = ['january', 'february', 'march', 'april', 'may', 'june','july','august','september','october','november','december']
    # TO DO: display the most common month
    print("Most frequent month is: {}".format(months[df['month'].mode()[0]].title()))

    # TO DO: display the most common day of week
    print("Most frequent day of week is: {}".format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    print("Most frequent hour is: {}".format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("Most frequent start station is: {}".format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print("Most frequent end station is: {}".format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    # I get the idea about idxmax() from: https://www.reddit.com/r/learnpython/comments/5j8h4x/pandas_groupby_to_get_max_occurrences_of_value/
    station_combination=df.groupby(['Start Station','End Station']).count().idxmax()
    print("Most frequent combination of start station and end station trip is: {0} , {1}".format(station_combination[0][0],station_combination[0][1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time: {}'.format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('Mean travel time: {}'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('User counts are :\n{}'.format(df['User Type'].value_counts()))

    try:
    # TO DO: Display counts of gender
        print('Gender counts are :\n{}'.format(df['Gender'].value_counts()))
    # TO DO: Display earliest, most recent, and most common year of birth
        print('\nEarliest year of birth: {}'.format(df['Birth Year'].min()))
        print('\nMost recent year of birth: {}'.format(df['Birth Year'].max()))
        print('\nMost common year of birth: {}'.format(df['Birth Year'].mode()[0]))
    except:
        print ('\nNo gender and birth data are provided for Washington')
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

        # Displays five lines of data if the user specifies that they would like to.
        # After displaying five lines, ask the user if they would like to see five more,
        # continuing asking until they say stop.

        count_row = 0
        while(True):
            rawdata = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n')
            if rawdata.lower() == 'yes' and count_row + 6 < len(df.index) :
                print(df[count_row:count_row+6])
                count_row=count_row+6
            else:
                if rawdata.lower() == 'no':
                    break
                else:
                    print('Enter yes or no.\n')

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
