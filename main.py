# Class = Python Intermediate Course_Spring 2023
# Student = David Garrido de Sousa
# Project = Data Plan Adjustment

#The purporse of this project is to automatize the mobile data plan adjustment in a big company according to the data consumption pf each user of the last three months. 

import pandas as pd
import statistics 


data_plan_list = [8000000, 10000000, 12000000, 15000000, 20000000, 30000000, 50000000]
df_month1 = input('Please enter file path for month 1 to be analyzed: ')
df_month2 = input('Please enter file path for month 2 to be analyzed: ')
df_month3 = input('Please enter file path for month 3 to be analyzed: ')

def file_to_DF(file,number_of_month):
    # Convert file into a dataframe
    df = pd.read_excel(file)

    # Rewriting the df with the important rows 
    df_bookeddata = df.loc[df["Product description"] == "INFO ZU IHREM DATENVOLUMEN DES ABRECHNUNGSMONATS IM INLAND VERTRAGLICH VEREINBARTES DATENVOLUMEN"]

    # Keeping the columns that are important
    df_bookeddata = df_bookeddata.filter(["Period", "Phone number", "Userid", "Volume in KiB"])

    # Renaming the columns/ inplace: Makes changes in original Data Frame if True.
    df_bookeddata.rename(columns={'Volume in KiB': 'Booked Data Volume'}, inplace = True)

    df_useddata= df.loc[df["Product description"] == "INFO ZU IHREM DATENVOLUMEN DES ABRECHNUNGSMONATS IM INLAND VERBRAUCHTES DATENVOLUMEN MIT HOHER GESCHWINDIGKEIT"]
    df_useddata = df_useddata.filter(["Phone number", "Volume in KiB"])
    df_useddata.rename(columns={'Volume in KiB': 'Used Data Volume'}, inplace = True)

    # Merging the data frames 
    df_month = pd.merge(df_bookeddata, df_useddata, on='Phone number')

    if number_of_month != 1:
        df_month = df_month.filter(["Phone number", "Booked Data Volume", "Used Data Volume"])

    df_month.rename(columns={'Booked Data Volume': f'Booked Data Volume for Month {number_of_month}','Used Data Volume': f'Used Data Volume for Month {number_of_month}' }, inplace = True)

    return df_month 


#Calling up the functions

df_month1=file_to_DF(df_month1,1)

df_month2=file_to_DF(df_month2,2)

df_month3=file_to_DF(df_month3,3)

df_final=pd.merge(pd.merge(df_month1,df_month2,on='Phone number'),df_month3,on='Phone number')

# Creating new columns 
data_cons_avrg_column = []
data_cons_std_column = []
data_adjustment = []

# Iterating over the Data Frame 
for i in df_final.index:
    data_consumption = [float(df_final.loc[i,"Used Data Volume for Month 1"]), float(df_final.loc[i,"Used Data Volume for Month 2"]), float(df_final.loc[i,"Used Data Volume for Month 3"])]
    data_consumption_average = statistics.mean(data_consumption)
    data_cons_avrg_column.append(data_consumption_average)
    data_consumption_stdv = statistics.stdev(data_consumption)
    data_cons_std_column.append(data_consumption_stdv)
    data_plan = [df_final.loc[i,"Booked Data Volume for Month 1"], df_final.loc[i,"Booked Data Volume for Month 2"], df_final.loc[i,"Booked Data Volume for Month 3"]]
    data_plan_average = statistics.mean(data_plan)
    
    def new_data_plan(y):
        closest = min(data_plan_list, key=lambda x: abs(x-y))
        return closest 

    discrepancy = data_consumption_average - data_plan_average

    if df_final.loc[i,"Booked Data Volume for Month 1"] != df_final.loc[i,"Booked Data Volume for Month 2"] or df_final.loc[i,"Booked Data Volume for Month 1"] != df_final.loc[i,"Booked Data Volume for Month 3"]:
        data_adjustment.append('It is not possible to propose a data plan adjustment. The data plan has been changed in the last three months.')
    else:
        if data_consumption_stdv >= 5000000.00:
            data_adjustment.append('It is not possible to propose a data plan adjustment. \nThere is too much difference between the data consumption.')
        else:
            if -10000000 < (data_consumption_average - data_plan_average) < 10000000:
                data_adjustment.append('It is not necessary to propose a data plan adjustment. \nThe current data plan and data consumption are too close. ')
            else:
                data_adjustment.append(f'The proposed data plan for this phone number is: {new_data_plan(data_consumption_average)} KiB')

df_final['Data Consumption Average'] = data_cons_avrg_column 
df_final['Data Consumption Standard Deviation'] = data_cons_std_column
df_final['Data Adjustment'] = data_adjustment

df_final.to_excel("Data Adjustment.xlsx")  
