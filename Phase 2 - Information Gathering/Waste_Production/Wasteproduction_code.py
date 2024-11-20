import pandas as pd
import os

# Directory of ISPRA files
directory = "C:/Users/pelle/Desktop/Magistrale secondo anno/Knowledge Graph Engineering/KGE-git/KGE-Project-Tourism-Waste-Management-in-Trentino/Phase 2 - Information Gathering/Waste_Production/Raw data" 

# Initialize an empty DataFrame to hold the merged data for all years
Waste_Production = pd.DataFrame()

columns = [
    "Comune", "Istat", "Dato riferito a", "Frazione organica (t)", 
    "Ing. misti a recupero (t)", "Carta e cartone (t)", "Altro RD (t)", 
    "Legno (t)", "Metallo (t)", "Plastica (t)", "RAEE (t)", "Selettiva (t)", 
    "Tessili (t)", "Vetro (t)", "Rifiuti da costruzione e demolizione (t)", 
    "Pulizia Stradale a Recupero (t)"
]

for year in range(2014, 2023):

    file_Tren = os.path.join(directory, f"Anno_{year}-04022_RDFrazioniComunale.csv")
    
    if os.path.exists(file_Tren):
        df_Tren = pd.read_csv(file_Tren, delimiter=';', decimal=',', header=0, index_col=None).reset_index()
        df_Tren.columns=columns
        print(df_Tren.head())
        exit(1)
        df_Tren['Anno'] = year #create column with year
        Waste_Production = pd.concat([Waste_Production, df_Tren], ignore_index=True)
    
    else:
        print(f"Warning: {file_Tren} does not exist.")

Waste_Production=Waste_Production.dropna(axis=1, how='all')

# Specify the path and name for the output CSV file
#output_path = "Waste_Production.csv"
print(Waste_Production)
# Save the DataFrame to a CSV file
#Waste_Production.to_csv(output_path, index=False)


