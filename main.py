# Class = Python Intermediate Course_Spring 2023
# Student = David Garrido de Sousa
# Project = Data Plan Adjustment

#The purporse of this project is to automatize the mobile data plan adjustment in a big company according to the data consumption pf each user of the last three months. 


import pandas as pd
import statistics 

def CSV_to_DF(file):
# Convert file into a dataframe
    df = pd.read_csv(file)

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
    return df_month

def filter_DF(a):
    a = a.filter(["Phone number", "Booked Data Volume", "Used Data Volume"])
    return a 

def rename_DF(a,b):
    a.rename(columns={'Booked Data Volume': f'Booked Data Volume for Month {b}','Used Data Volume': f'Used Data Volume for Month {b}' }, inplace = True)
    return a 

df_month1 = CSV_to_DF(r'C:\Users\v-davidgarr\Documents\Data Adjustment_Python Project\Data_Volume_042023.csv')
rename_DF(df_month1,1)

df_month2 = CSV_to_DF(r'C:\Users\v-davidgarr\Documents\Data Adjustment_Python Project\Data_Volume_032023.csv')
df_month2=filter_DF(df_month2)
rename_DF(df_month2,2)

df_month3 = CSV_to_DF(r'C:\Users\v-davidgarr\Documents\Data Adjustment_Python Project\Data_Volume_022023.csv')
df_month3=filter_DF(df_month3)
rename_DF(df_month3,3)

df_final=pd.merge(pd.merge(df_month1,df_month2,on='Phone number'),df_month3,on='Phone number')

# Iterating over the Data Frame 

for i in df_final.index:
    data_consumption = [float(df_final.loc[i,"Used Data Volume for Month 1"]), float(df_final.loc[i,"Used Data Volume for Month 2"]), float(df_final.loc[i,"Used Data Volume for Month 3"])]
   # print (data_consumption)
    data_consumption_average = statistics.mean(data_consumption)
    #print (data_consumption)
    data_consumption_stdv = statistics.stdev(data_consumption)
    #print(data_consumption_stdv)
    data_plan = [df_final.loc[i,"Booked Data Volume for Month 1"], df_final.loc[i,"Booked Data Volume for Month 2"], df_final.loc[i,"Booked Data Volume for Month 3"]]
    data_plan_average = statistics.mean(data_plan)
    #print (data_plan)
    def new_data_plan(y):
        data_plan_list = [8, 10, 12, 15, 20, 30, 50]
        closest = min(data_plan_list, key=lambda x: abs(x-y))
        return closest 

    discrepancy = data_consumption_average - data_plan_average

    if df_final.loc[i,"Booked Data Volume for Month 1"] != df_final.loc[i,"Used Data Volume for Month 2"] or df_final.loc[i,"Booked Data Volume for Month 1"] != df_final.loc[i,"Used Data Volume for Month 3"]:
        a = 1 #print ('It is not possible to propose a data plan adjustment. \nThe data plan has been changed in the last three months.')
    else:
        if data_consumption_stdv >= 5.00:
            a = 1 # print ('It is not possible to propose a data plan adjustment. \nThere is too much difference between the data consumption.')
        else:
            if -10 < (data_consumption_average - data_plan_average) < 10:
                a = 1 #print ('It is not necessary to propose a data plan adjustment. \nThe current data plan and data consumption are too close. ')
            else:
                print (f'The proposed data plan for this phone number is: {new_data_plan(data_consumption)} GB')


