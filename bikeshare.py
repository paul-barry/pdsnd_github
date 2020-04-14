import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
validCities = ['chicago','new york city','washington']

validMonths = ['all','january','february','march','april',
               'may','june','july','august','september','october',
               'november','december']

validDays = ['all','monday','tuesday','wednesday','thursday',
             'friday','saturday','sunday']


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
    city = ""
    while True:
        try:
            city = input("Enter valid city name (chicago, new york city, washington):")
            if (city.lower() in validCities):
                break
            else:
                print("Invalid city name of <{}>".format(city))
        except :
            print("Invalid city name of <{}>".format(city))

    # get user input for month (all, january, february, ... , june)
    month = ""
    while True:
        try:
            month = input("Enter valid month (e.g. all, january, february, etc.):")
            if (month.lower() in validMonths):
                break
            else:
                print("Invalid Month of <",month,">")
        except:
            print("Invalid Month of <",month,">")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = ""
    while True:
        try:
            day = input("Enter valid day of week (e.g. all, monday, tuesday, etc.):")
            if (day in validDays):
                break
            else:
                print("Invalid day of <{}>".format(day))
        except:
            print("Invalid day of <{}>".format(day))

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
    df['day_of_week'] = df['Start Time'].dt.weekday_name
 
       # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.capitalize()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel.

    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    Returns
    -------
    None.    
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("Most common month      :",validMonths[df['month'].mode()[0]].capitalize())


    # TO DO: display the most common day of week
    print("Most common day of week:",df['day_of_week'].mode()[0].capitalize())

    # TO DO: display the most common start hour
    print("Most common start hour :",df['Start Time'].dt.hour.mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip.

    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    Returns
    -------
    None.    
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("Most commonly used start station:",df['Start Station'].mode()[0])


    # TO DO: display most commonly used end station
    print("Most commonly used end station  :",df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print("Most common combination of start and end stations:",' , '.join(str(i) for i in df.groupby(['Start Station','End Station']).size().idxmax()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.

    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    Returns
    -------
    None.    
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time:',df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('Mean travel time:',df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users.
 
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    Returns
    -------
    None.   
    
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts by user types:\n',df['User Type'].value_counts().reset_index())


    # TO DO: Display counts of gender
    if 'Gender' in df:
        print('\nCounts by gender:\n',df['Gender'].value_counts().reset_index())
    else:
        print('\nGender does not exist for this US bikeshare data.')


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print("\nEarliest Birth year:",df['Birth Year'].min(axis=0))
        print("Most recent Birth year:",df['Birth Year'].max(axis=0))
        print("Most common year of birth:",df['Birth Year'].mode()[0])
    else:
        print('\nBirth Year does exist for this US bikeshare data.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def chunkrawdata(df):
    """Display raw data if requested by the user

    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    Returns
    -------
    None.   
    """
       #https://towardsdatascience.com/how-to-show-all-columns-rows-of-a-pandas-dataframe-c49d4507fcf
    pd.set_option('display.max_columns', None)
    
    # track place in raw data
    currentRow = 0
    while True:
        keepgoing = input('\nWould you like to see raw data? Enter yes or no.\n')
        if keepgoing.lower() != 'yes':
            break
        else:
            print(df[currentRow:currentRow+5])
            currentRow += 5
            
       
            


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        chunkrawdata(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
          main()
