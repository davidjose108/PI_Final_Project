# Class = Python Intermediate Course_Spring 2023
# Student = David Garrido de Sousa
# Project = Data Plan Adjustment

#The purporse of this project is to automatize the mobile data plan adjustment in a big compnay 
#according to the data consumption of the last three months. 

#Import of the necessary libraries

import statistics

#Input of the data plan 

data_plan_1 = int(input('Enter data plan first month: '))
data_plan_2 = int(input('Enter data plan second month: '))
data_plan_3 = int(input('Enter data plan third month: '))
data_plan = [data_plan_1, data_plan_2, data_plan_3]
data_plan_average = statistics.mean(data_plan)

#Input of the data consumption

data_consumption_1 = float(input('Enter data consumption for the first month: '))
data_consumption_2 = float(input('Enter data consumption for the second month: '))
data_consumption_3 = float(input('Enter data consumption for the third month: '))
data_consumption = [data_consumption_1, data_consumption_2, data_consumption_3]
data_consumption_stdv = statistics.stdev(data_consumption)
data_consumption_average = statistics.mean(data_consumption)

# Defining a function for proposing a new data plan

def new_data_plan(y):
    data_plan_list = [8, 10, 12, 15, 20, 30, 50]
    closest = min(data_plan_list, key=lambda x: abs(x-y))
    return closest 


discrepancy = data_consumption_average - data_plan_average
print(discrepancy)

if data_plan_1 != data_plan_2 or data_plan_1 != data_plan_3:
    print ('It is not possible to propose a data plan adjustment. \nThe data plan has been changed in the last three months.')
else:
    if data_consumption_stdv >= 5.00:
        print ('It is not possible to propose a data plan adjustment. \nThere is too much difference between the data consumption.')
    else:
        if -10 < (data_consumption_average - data_plan_average) < 10:
            print ('It is not necessary to propose a data plan adjustment. \nThe current data plan and data consumption are too close. ')
        else:
            print (f'The proposed data plan for this phone number is: {new_data_plan(data_consumption_average)} GB')

 
import pandas as pd

df = pd.read_csv(r'')
df = df.filter(["Period", "Phone number", "Userid", "Volume in KiB", "Product description"])


class User():
    def __init__(self, Period, Phone_number, Userid, Volume_in_KiB_used, Volume_in_KiB_booked):
        self.Phone_number=Phone_number
        self.Userid=Userid
        self.Volume_in_KiB_used = Volume_in_KiB_used
        self.Volume_in_KiB_booked = Volume_in_KiB_booked
        self.Period = Period
    
user1 = User()

val = df._get_value(2, 'Phone number')
print(val)
    
df_usedvolume= df.loc[df["Product description"] == "INFO ZU IHREM DATENVOLUMEN DES ABRECHNUNGSMONATS IM INLAND VERBRAUCHTES DATENVOLUMEN MIT HOHER GESCHWINDIGKEIT"]

vol = df_usedvolume._get_value(1, 'Volume in KiB')
print(vol)

df_bookedvolume = df.loc[df["Product description"] == "INFO ZU IHREM DATENVOLUMEN DES ABRECHNUNGSMONATS IM INLAND VERTRAGLICH VEREINBARTES DATENVOLUMEN"]
vbl = df_bookedvolume._get_value(0, 'Volume in KiB')

print(vbl)
