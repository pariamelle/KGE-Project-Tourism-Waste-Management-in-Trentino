import pandas as pd
import numpy as np
import geopandas as gpd

# DATA LOADING
gdf = gpd.read_file("C:/Users/pelle/Desktop/Magistrale secondo anno/Knowledge Graph Engineering/KGE-git/KGE-Project-Tourism-Waste-Management-in-Trentino/Phase 2 - Information Gathering/Municipality/Raw data/Trento_MunicipalityBorders.geojson") # use your path 
df_population = pd.read_csv("C:/Users/pelle/Desktop/Magistrale secondo anno/Knowledge Graph Engineering/KGE-git/KGE-Project-Tourism-Waste-Management-in-Trentino/Phase 2 - Information Gathering/Municipality/Raw data/Pop_Trento2024.csv") # use your path

# DATA CLEANING
# Usefull tags
istat_geojson = "ref:ISTAT"  # ISTAT code column in GeoJSON
istat_csv = "Codice comune"  # ISTAT code column in CSV
population_column = "Totale" 

# keeping only essential columns
df_population = df_population[[istat_csv,population_column]]

# Converting ISTAT codes in string for key usage
df_population[istat_csv] = df_population[istat_csv].astype(str)
# Remove leading zeros from istat_geojson column in gdf
gdf[istat_geojson] = gdf[istat_geojson].astype(str).str.lstrip('0')

#gdf[istat_geojson]=gdf[istat_geojson].astype(str)

#Merge the two dataset
gdf_new = gdf.merge(df_population[[istat_csv, population_column]],
                left_on=istat_geojson,
                right_on=istat_csv,
                how="left")

gdf_new = gdf_new.drop(columns=[istat_csv])

gdf_new.rename(columns={population_column: "Popolazione Totale"}, inplace=True)

# Select only the relevant columns: 'name', 'Popolazione Totale', 'ref:ISTAT', 'geometry'
columns_to_keep = ['name', 'Popolazione Totale', 'ref:ISTAT', 'geometry']
filtered_gdf = gdf_new[columns_to_keep]

# Save the new updated file
output_file = "Municipality"
filtered_gdf.to_file(output_file, driver="GeoJSON")