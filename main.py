# Class = Python Intermediate Course_Spring 2023
# Student = David Garrido de Sousa
# Project = Data Plan Adjustment

#The purporse of this project is to automatize the mobile data plan adjustment in a big compnay 
#according to the data consumption of the last three months. 



 
import pandas as pd

df = pd.read_csv(r'')
df = df.filter(["Period", "Phone number", "Userid", "Volume in KiB", "Product description"])


class User():
    def __init__(self, Phone_number, Userid, Volume_in_KiB_used_Month1, Volume_in_KiB_booked_Month1, Volume_in_KiB_used_Month2, Volume_in_KiB_booked_Month2, Volume_in_KiB_used_Month3, Volume_in_KiB_booked_Month3):
        self.Phone_number=Phone_number
        self.Userid=Userid
        self.Volume_in_KiB_used = Volume_in_KiB_used
        self.Volume_in_KiB_booked = Volume_in_KiB_booke
    
user1 = User()

val = df._get_value(2, 'Phone number')
print(val)
    
df_usedvolume= df.loc[df["Product description"] == "INFO ZU IHREM DATENVOLUMEN DES ABRECHNUNGSMONATS IM INLAND VERBRAUCHTES DATENVOLUMEN MIT HOHER GESCHWINDIGKEIT"]

vol = df_usedvolume._get_value(1, 'Volume in KiB')
print(vol)

df_bookedvolume = df.loc[df["Product description"] == "INFO ZU IHREM DATENVOLUMEN DES ABRECHNUNGSMONATS IM INLAND VERTRAGLICH VEREINBARTES DATENVOLUMEN"]
vbl = df_bookedvolume._get_value(0, 'Volume in KiB')

print(vbl)
