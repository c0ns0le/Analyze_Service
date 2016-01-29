'''
Created on Jan 9, 2016

@author: Jesu
'''

import re 
import csv
import pandas as pd

def column_counts(df,columns):
    """
    This function displays the count of each value under passed columns
    :param df: dataframe object for the input csv file
    :param columns: list variable containing the column name in header to get the counts
    :return: None
    """
    for column in columns:
        print(df[column].value_counts())
        print(df[column].isnull().sum())
        print("*"*50)

def group_by_prdouct_situation(df):
    """
    Trying to group by Product and situation fields
    :param df: dataframe object for the input csv file
    :return: None
    """
    group_prod_sit=df['u_situation'].groupby(df['u_business_service'])
    print(list(group_prod_sit)[1])
 #   print(group_prod_sit.describe())

def auto_close_analysis(df_autoclose):
    """
    Alanysing auto close rows
    :param df_autoclose:
    :return:
    """
    print(df_autoclose)

def read_analysis_csv(input_filename):
    """
    Analyzing the csv file and calling different functions
    :param input_filename: input csv file to analysis
    :return:
    """
    df=pd.read_csv(input_filename)
#    column_counts(df,["opened_by","closed_by","u_business_service","u_situation","state"])
#    group_by_prdouct_situation(df)
    auto_close_analysis(df[df.closed_by.isin(['Netcool Integration','Opalis Admin'])])

if __name__ == '__main__':

    input_filename="incident_working.csv"
    print("The input file is \t%s\n "  %input_filename)
    read_analysis_csv(input_filename)