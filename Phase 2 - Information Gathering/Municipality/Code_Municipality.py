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
population_column = "Totale" 

# keeping only essential columns
df_population = df_population[[istat_csv,population_column]]

# Converting ISTAT codes in string for key usage
df_population[istat_csv] = df_population[istat_csv].astype(str)
# Remove leading zeros from istat_geojson column in gdf
gdf[istat_geojson] = gdf[istat_geojson].astype(str).str.lstrip('0')


#Merge the two dataset
gdf_new = gdf.merge(df_population[[istat_csv, population_column]],
                left_on=istat_geojson,
                right_on=istat_csv,
                how="left")

gdf_new = gdf_new.drop(columns=[istat_csv])



columns_to_keep = ['name', 'Totale', 'ref:ISTAT', 'geometry']
filtered_gdf = gdf_new[columns_to_keep]
filtered_gdf.rename(columns={population_column: "population"}, inplace=True)

# Save the new updated file
output_file = "Municipality"
# filtered_gdf.to_csv(output_file, driver="GeoJSON")
#TO BE CHANGED