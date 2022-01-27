import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

import os


# Thank you, Ryan Orsinger
def get_db_url(db_name):

    # import direct credentials
    from env import host, user, password

    # use credentials
    return f'mysql+pymysql://{user}:{password}@{host}/{db_name}'



def get_logs():

    # define url 
    url = get_db_url('curriculum_logs')

    # define sql query
    sql = '''
    SELECT * 
    FROM logs
    LEFT JOIN cohorts on logs.cohort_id = cohorts.id
    '''

    # set up if-conditional to see if a .csv is cached
    if os.path.isfile('curriculum_logs.csv'):

        # read .csv into pandas dataframe
        df = pd.read_csv('curriculum_logs.csv', index_col = 0)

    else:

        # use pandas's read_sql function to retrieve data from codeup db
        df = pd.read_sql(sql, url)

        # cache data
        df.to_csv('curriculum_logs.csv')
    
    return df

def prep_logs():

    #load data
    df = get_logs()

    #concatenate date and time
    df['date_time'] = df.date + ' ' + df.time

    # set date to datetime object using pandas
    df.date_time = pd.to_datetime(df.date_time, format = '%Y-%m-%d %H:%M:%S')

    # set index to datetime object created
    df = df.set_index('date_time')

    # convert date/ time columns to datetime objects
    df.start_date = pd.to_datetime(df.start_date)
    df.end_date = pd.to_datetime(df.end_date)
    df.created_at = pd.to_datetime(df.created_at)
    df.updated_at = pd.to_datetime(df.updated_at)

    # create column called program that declares what program the student is in
    df['program'] = df.program_id.map({1.0: 'Full-Stack PHP',
                                   2.0: 'Full-Stack Java',
                                   3.0: 'Data Science',
                                   4.0: 'Front-End'
                                  }
                                 )

    # create column that designates whether or not a user_id is staff
    df['is_staff'] = df.name == 'staff'

    # set a list of unneeded columns
    extra = ['id', 'slack', 'deleted_at', 'date', 'time']

    # drop these columns
    df = df.drop(columns = extra)

    return df