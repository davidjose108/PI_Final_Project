# Class = Python Intermediate Course_Spring 2023
# Student = David Garrido de Sousa
# Project = Data Plan Adjustment

#The purporse of this project is to automatize the mobile data plan adjustment in a big company according to the data consumption pf each user of the last three months. 


# Convert file into a dataframe
import pandas as pd

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

df_month1 = CSV_to_DF(r'C:\Users\v-davidgarr\Documents\Data Adjustment_Python Project\Data_Volume_042023.csv')
print (df_month1)
df_month2 = CSV_to_DF(r'C:\Users\v-davidgarr\Documents\Data Adjustment_Python Project\Data_Volume_032023.csv')
print(df_month2)
