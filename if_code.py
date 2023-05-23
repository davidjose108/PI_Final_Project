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