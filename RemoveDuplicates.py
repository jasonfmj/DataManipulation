import pandas as pd
theFile = input("Please enter full path and file to remove duplicates: ")
theOutput = input("Please enter full path where you want to save the output file: ")
data = pd.read_excel(r"{}".format(theFile))
data.drop_duplicates(['app_name', 'application_categories', 'company_name', 'email', 'file_name', 'release_name', 'release_number', 'username'], keep="first", inplace=True)
data.to_excel(r"{}".format(theOutput) + "\output.xlsx")
