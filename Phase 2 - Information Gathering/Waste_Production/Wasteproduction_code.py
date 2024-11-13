import pandas as pd
import os

# Directory of ISPRA files
directory = "Raw data" 

# Initialize an empty DataFrame to hold the merged data for all years
Waste_Production = pd.DataFrame()


for year in range(2014, 2023):

    file_Tren = os.path.join(directory, f"Anno_{year}-04022_RDFrazioniComunale.csv")
    
    if os.path.exists(file_Tren):
        df_Tren = pd.read_csv(file_Tren, delimiter=';', header=1)
        df_Tren['Anno'] = year #create column with year
        Waste_Production = pd.concat([Waste_Production, df_Tren], ignore_index=True)
    
    else:
        print(f"Warning: {file_Tren} does not exist.")

Waste_Production=Waste_Production.dropna(axis=1, how='all')

# Specify the path and name for the output CSV file
output_path = "Waste_Production.csv"

# Save the DataFrame to a CSV file
Waste_Production.to_csv(output_path, index=False)


