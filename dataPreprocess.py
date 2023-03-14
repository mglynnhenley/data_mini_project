import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

geometries_data_set = pd.read_csv('data/geometries.csv')
residential_data_set = geometries_data_set[geometries_data_set.unit_usage == "RESIDENTIAL"]
residential_area_data_set = residential_data_set[residential_data_set.entity_type == "area"]
residential_area_data_set_grouped_by_site_id = residential_area_data_set.groupby('building_id')["apartment_id"].count()
residential_area_data_set_grouped_by_site_id.to_csv('residential_area_data_set_grouped_by_site_id.csv')

locations_ratings_data_set = pd.read_csv('data/location_ratings.csv')
location_ratings_social_demographic = locations_ratings_data_set[["building_id", "location_rating_NASE_W_DOM"]]
location_ratings_social_demographic.to_csv('building_id_location_ratings_data_set.csv', index=False)

simulationDataSet = pd.read_csv('data/simulations.csv')
simulationDataSetResidential = simulationDataSet[simulationDataSet.unit_usage == "RESIDENTIAL"]
simulationDataSetResidentialAreaGroupedBySiteID = simulationDataSetResidential.groupby('building_id')["sun_201803211200_mean"].mean()



gibuildingsWithRatingsAndApartments = pd.merge(location_ratings_social_demographic, simulationDataSetResidentialAreaGroupedBySiteID, on="building_id")

buildingsWithRatingsAndApartments.to_csv('ratings', index=False)