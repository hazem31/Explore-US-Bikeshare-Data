import time
import pandas as pd
import numpy as np
import datetime as dt
import click

CITY_DATA = {'chicago': 'chicago.csv',
             'new york': 'new_york_city.csv',
             'washington': 'washington.csv'}

months = ['january', 'february', 'march', 'april', 'may', 'june']

weekdays = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday',
            'saturday']


def get_input():
    while True:
        city = input("Would you like to see data for Chicago, New York, or Washington? ")
        city = city.lower()
        if CITY_DATA.get(city):
            break
    while True:

        day_or_month = input("Would you like to filter the data by month, day, or not at all? ")
        if day_or_month == "month" or day_or_month == "day" or day_or_month == "not at all":
            break
    
    if day_or_month == "month" :
        while True:
            month = input("Which month - January, February, March, April, May, or June? ")
            month = month.lower()
            if month in months:
                break
        return city,month
    elif day_or_month == "day" :
        while True:
            day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday")
            day = day.lower()
            if day in weekdays:
                break
        return city,day
    else:
        return city,None


def load_data(city, filter):
    
    
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df["Start Time"])


    df['month'] = df["Start Time"].dt.month
    df['day_of_week'] = df["Start Time"].dt.weekday_name


    if filter:
        if filter in months:
            month = months.index(filter) + 1
            df = df[df["month"] == month]
        else:
            df = df[df["day"] == filter.title()]
    
    return df 
    
    
def check_end():
    con = None
    while True:
        con = input("Restart ? type 'yes' or 'no' ")
        con = con.lower()
        if con == "yes" or con == "no":
            break
    return con

def calculate_stat(df):
    print()
    print(f"most common month { months[df['month'].mode()[0]-1] } ")
    print()
    print(f"most common day {df['day_of_week'].mode()[0] }")
    print()
    print(f"most common hour of day {str(df['Start Time'].dt.hour.mode()[0] )}")
    print()
    v = df["Start Station"] + '-' + df["End Station"]
    print(f"most common start station {df['Start Station'].mode()[0]}")
    print()
    print(f"most common end station {df['End Station'].mode()[0]}")
    print()
    print(f"most common end station { v.mode()[0]}")
    print()
    print(f"total travel time { str(df['Trip Duration'].sum())}")
    print()
    print(f"average travel time {str(df['Trip Duration'].mean())}")
    print()
    print("counts for each user type")
    print(df["User Type"].value_counts())

    print()
    if "Gender" in df.columns:
        print("counts for each Gender")
        print(df["Gender"].value_counts())
    print()
    
    if "Birth Year" in df.columns:
        print(f"earliest year of birth {str(df['Birth Year'].min())}")
        print()
        print(f"most recent year of birth {str(df['Birth Year'].max())}")
        print()
        print(f"most comon year of birth {str(df['Birth Year'].mode()[0])}")
        print()


def main():
    while True:
        city , filter = get_input()
        df = load_data(city,filter)
        
        calculate_stat(df)
        
        stat = check_end()
        if stat == "no":
            break

if __name__ == '__main__':
    main()
