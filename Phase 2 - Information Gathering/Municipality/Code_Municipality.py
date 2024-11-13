import pandas as pd
import numpy as np
import geopandas as gpd

# DATA LOADING
#gdf = gpd.read_file("Raw data/Trento_MunicipalityBorders.geojson")
#df_population = pd.read_csv("Raw data/Pop_Trento2024.csv")
gdf = gpd.read_file("C:/Users/pelle/Desktop/Magistrale secondo anno/Knowledge Graph Engineering/KGE-git/KGE-Project-Tourism-Waste-Management-in-Trentino/Phase 2 - Information Gathering/Municipality/Raw data/Trento_MunicipalityBorders.geojson")
df_population = pd.read_csv("C:/Users/pelle/Desktop/Magistrale secondo anno/Knowledge Graph Engineering/KGE-git/KGE-Project-Tourism-Waste-Management-in-Trentino/Phase 2 - Information Gathering/Municipality/Raw data/Pop_Trento2024.csv")

# DATA CLEANING
# Usefull tags
istat_geojson = "ref:ISTAT"  # ISTAT code column in GeoJSON
istat_csv = "Codice comune"  # ISTAT code column in CSV
population_column = "Totale"        # Column Name of Total population 

# keeping only essential columns
df_population = df_population[[istat_csv,population_column]]

# Converting ISTAT codes in string for key usage
df_population[istat_csv] = df_population[istat_csv].astype(str)
gdf[istat_geojson]=gdf[istat_geojson].astype(str)

#gdf = gdf.merge(df_population[[istat_csv, population_column]],
 #               left_on=istat_geojson,
  #              right_on=istat_csv,
   #             how="left")

#gdf = gdf.drop(columns=[istat_csv])

# Salva il file GeoJSON aggiornato con la colonna della popolazione
#output_file = "../Municipality_Table/Municipality_final"

# Save the DataFrame to a CSV file
#gdf.to_file(output_file, driver="GeoJSON")