'''
Created on Jan 9, 2016

@author: Jesu
'''

import re 
import csv
import pandas as pd
import json

def column_counts(df,columns):
    """
    This function displays the count of each value under passed columns
    :param df: dataframe object for the input csv file
    :param columns: list variable containing the column name in header to get the counts
    :return: None
    """
    for column in columns:
        print("\nThe sorted individual counts from the column \"%s\":" %column)
        print(df[column].value_counts())
        print("The count of Null value is %d\n" %(df[column].isnull().sum()))
        print("*"*50)

def group_by_product_situation(df):
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
    Analysing auto close rows
    :param df_autoclose:
    :return:
    """
    print(df_autoclose)

def user_requests(df_userrequest):
    """
    Analysing user requests
    :param df_userrequest:
    :return:
    """
    print(df_userrequest)

def quick_analysis(df):
    print(df.loc[~(df["short_description"].str.contains('AMQ DLQ') | df["short_description"].str.contains('AMQ BR0') | df["short_description"].str.contains('STORE')),"short_description"].value_counts())

def read_analysis_csv(input_filename):
    """
    Analyzing the csv file and calling different functions
    :param input_filename: input csv file to analysis
    :return:
    """
    df=pd.read_csv(input_filename)
    quick_analysis(df)
    #input_json=dict(json.loads(open('Middleware_analyse.json').read()))
    #print(input_json("name"))
    #    column_counts(df,["opened_by","closed_by","u_business_service","u_situation","state"])
    #    group_by_product_situation(df)
    #auto_close_analysis(df[df.closed_by.isin(['Netcool Integration','Opalis Admin'])])
    #    user_requests(df[df.opened_by.isin(['Netcool Integration','Opalis Admin'])==False])


if __name__ == '__main__':

    input_filename="incident (3).csv"
    print("The input file is \t%s\n "  %input_filename)
    read_analysis_csv(input_filename)