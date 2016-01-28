'''
Created on Jan 9, 2016

@author: Jesu
'''

import re 
import csv
import pandas as pd

def column_counts(df,columns):
    for column in columns:
        print(df[column].value_counts())
        print(df[column].isnull().sum())
        print("*"*50)

def group_by_prdouct_situation(df):
    group_prod_sit=df['u_situation'].groupby(df['u_business_service'])
    print(list(group_prod_sit)[1])
 #   print(group_prod_sit.describe())

def read_analysis_csv(input_filename):
    df=pd.read_csv(input_filename)
#    column_counts(df,["opened_by","closed_by","u_business_service","u_situation","state"])
    group_by_prdouct_situation(df)

if __name__ == '__main__':

    input_filename="incident_working.csv"
    print("The input file is \t%s\n "  %input_filename)

    read_analysis_csv(input_filename)