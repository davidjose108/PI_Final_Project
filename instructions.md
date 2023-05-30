# Instructions of step by step for the Data Plan Adjustment 

1.- Prepare the data 

a.- Filter BOOKED DATA PLAN
      From the data base (2023xx_xxxxxx_details_DTAG_MOB_xxxxxxxxx), filter the PRODUCT DESCRIPTION with INFO ZU IHREM DATENVOLUMEN DES ABRECHNUNGSMONATS IM INLAND VERTRAGLICH VEREINBARTES DATENVOLUMEN)
b.- Create a new file with the following columns:
      Phone number, Userid, BOOKED DATA PLAN Month 1      
c.- Filter USED DATA VOLUME 
      From the data base (2023xx_xxxxxx_details_DTAG_MOB_xxxxxxxxx), filter the INFO ZU IHREM DATENVOLUMEN DES ABRECHNUNGSMONATS IM INLAND VERBRAUCHTES DATENVOLUMEN MIT HOHER GESCHWINDIGKEIT)
      Copy the Description column with the UserID
d.- Using VLOOKUP, match the USED DATA VOLUME Month 1 with the columns copied before. 
e.- Open data base for Month 2 and Month 3. Repeat steps a, c, d with the original file. 

2.- Check BOOKED DATA column values of each month. IF different, STOP. If same values are in every month, PROCEED. 

3.- Get average and typical deviation from USED DATA VOLUME. IF typical deviation USED DATA VOLUME under 0.05 




    

