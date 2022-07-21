#Created by Jasonfmj.
#This script is used to Remove Duplicates on an excel .xlsx spreadsheet.

import pandas as pd
theFile = input("Please enter full path and file to remove duplicates: ")
theOutput = input("Please enter full path where you want to save the output file: ")
data = pd.read_excel(r"{}".format(theFile))
data.drop_duplicates(inplace=True)
data.to_excel(r"{}".format(theOutput) + "\output.xlsx")
