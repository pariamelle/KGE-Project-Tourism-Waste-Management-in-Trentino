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

# Translating to English categories and columns 
old_cat_names = ["Frazione organica (t)", "Ing. misti a recupero(t)","Carta e cartone (t)",
                "Altro RD (t)","Legno (t)","Metallo (t)","Plastica (t)","RAEE (t)","Selettiva (t)",
                "Tessili (t)","Vetro (t)","Rifiuti da costruzione e demolizione (t)",
                "Pulizia Stradale a Recupero (t)"]
new_cat_names = ['Organic Fraction (t)', 'Mixed Materials for Recovery (t)',
             'Paper and Cardboard (t)', 'Other Separate Collection (t)',
             'Wood (t)', 'Metal (t)', 'Plastic (t)', 
             'Waste Electrical and Electronic Equipment (t)',
             'Selective Collection (t)', 'Textiles (t)', 'Glass (t)',
             'Construction and Demolition Waste (t)', 
             'Street Cleaning Waste for Recovery (t)']
# Create a mapping dictionary from old to new category names
category_mapping = dict(zip(old_cat_names, new_cat_names))
# Replace old category names with new ones in the 'Waste type' column
df_cleaned['Waste type'] = df_cleaned['Waste type'].replace(category_mapping)


new_col_names = ['Municipality', 'ref: ISTAT']
old_col_names = ["Comune", "Istat"]
# Create a mapping dictionary for columns
column_mapping = dict(zip(old_col_names, new_col_names))
# Rename columns in the DataFrame
df_cleaned.rename(columns=column_mapping, inplace=True)

# Creating a new column for categories codes
categories = ['1', None, '2', '10', '8', '4', '5', '7', None, '6', '3', '9', None]
new_cat_mapping = dict(zip(new_cat_names, categories))
df_cleaned['category'] = df_cleaned['Waste type'].map(new_cat_mapping)

# Specify the path and name for the output CSV file
output_path = "Waste_Production.csv"
# Save the DataFrame to a CSV file
df_cleaned.to_csv(output_path, index=False)