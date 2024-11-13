import pandas as pd
import numpy as np
import geopandas as gpd

# DATA LOADING
gdf = gpd.read_file("Raw data/Trento_MunicipalityBorders.geojson") # use your path 
df_population = pd.read_csv("Raw data/Pop_Trento2024.csv") # use your path

# DATA CLEANING
# Usefull tags
istat_geojson = "ref:ISTAT"  # ISTAT code column in GeoJSON
istat_csv = "Codice comune"  # ISTAT code column in CSV
population_column = "Totale"        # Column Name of Total population 

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

print(gdf_new[population_column])

# Save the new updated file
output_file = "Municipality_tab"
gdf_new.to_file(output_file, driver="GeoJSON")