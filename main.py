# Class = Python Intermediate Course_Spring 2023
# Student = David Garrido de Sousa
# Project = Data Plan Adjustment

#The purporse of this project is to automatize the mobile data plan adjustment in a big company according to the data consumption pf each user of the last three months. 


# Convert file into a dataframe
df = pd.read_csv(r'C:\Users\v-davidgarr\Documents\Data_Volume_042023.csv')

# Rewriting the df with the important rows 
df_bookeddata_month1 = df.loc[df["Product description"] == "INFO ZU IHREM DATENVOLUMEN DES ABRECHNUNGSMONATS IM INLAND VERTRAGLICH VEREINBARTES DATENVOLUMEN"]

# Keeping the columns that are important
df_bookeddata_month1 = df_bookeddata_month1.filter(["Period", "Phone number", "Userid", "Volume in KiB"])

# Renaming the columns/ inplace: Makes changes in original Data Frame if True.
df_bookeddata_month1.rename(columns={'Volume in KiB': 'Booked Data Volume for Month 1'}, inplace = True)

df_useddata_month1= df.loc[df["Product description"] == "INFO ZU IHREM DATENVOLUMEN DES ABRECHNUNGSMONATS IM INLAND VERBRAUCHTES DATENVOLUMEN MIT HOHER GESCHWINDIGKEIT"]
df_useddata_month1 = df_useddata_month1.filter(["Phone number", "Volume in KiB"])
df_useddata_month1.rename(columns={'Volume in KiB': 'Used Data Volume for Month 1'}, inplace = True)

# Merging the data frames 

df_month1 = pd.merge(df_bookeddata_month1, df_useddata_month1, on='Phone number')
print(df_month1)
