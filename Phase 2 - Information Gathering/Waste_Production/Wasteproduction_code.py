import pandas as pd
import os

# Directory of ISPRA files
directory = "Raw data" 

# Initialize an empty DataFrame to hold the merged data for all years
Waste_Production = pd.DataFrame()


for year in range(2014, 2023):

    file_Tren = os.path.join(directory, f"Anno_{year}-04022_RDFrazioniComunale.csv")
    
    if os.path.exists(file_Tren):
        df_Tren = pd.read_csv(file_Tren, delimiter=';', decimal=',', header=0).reset_index()
        print(df_Tren.head())
        df_Tren['Anno'] = year #create column with year
        Waste_Production = pd.concat([Waste_Production, df_Tren], ignore_index=True)
    
    else:
        print(f"Warning: {file_Tren} does not exist.")


# Changing the dataframe from large format into long format 
Waste_Production_melted = pd.melt(
    Waste_Production,
    id_vars=["Comune", "Istat"],
    value_vars=["Frazione organica (t)", "Ing. misti a recupero(t)","Carta e cartone (t)",
                "Altro RD (t)","Legno (t)","Metallo (t)","Plastica (t)","RAEE (t)","Selettiva (t)",
                "Tessili (t)","Vetro (t)","Rifiuti da costruzione e demolizione (t)",
                "Pulizia Stradale a Recupero (t)"],
    var_name="Waste type",
    value_name="Quantity"
)


#getting rid of NaN
df_cleaned = Waste_Production_melted.dropna(subset=["Quantity"])

print(df_cleaned)
# Specify the path and name for the output CSV file
output_path = "Waste_Production.csv"
# Save the DataFrame to a CSV file
df_cleaned.to_csv(output_path, index=False)


