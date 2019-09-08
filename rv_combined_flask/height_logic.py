import pandas as pd 
from math import radians, cos, sin, asin, sqrt

def get_low_clearances(user_height):

    df = pd.read_csv('CSVs/low_clearances.csv')

    no_clearance = []

    for i in df['height']:
        boolean = user_height < i
        no_clearance.append(boolean)

    df['pass_through'] = no_clearance

    df = df.loc[df['pass_through'] == False]

    return df

def get_med_coordinate(lon1, lat1, lon2, lat2):
        lat_med = (lat1+lat2) / 2
        lon_med = (lon1+lon2) / 2

        return lat_med, lon_med

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r

def km_to_mile(distance):
    distance = distance *0.621371
    return distance

def location_finder(df, latitude, longitude, distance):
    """
    Returns places of interest within a designated area for a users specific geographic coordinates.
    
    Parameters:
        df (Pandas DataFrame): DataFrame containing places of interest and their corresponding lat/long coordinates
        latitude (Float value): Users designated latitude
        longitude (Float value): Users designated longitude
        distance (Int): Value that determines the search area size for designated place of interest
        
    Returns:
        df (Pandas DataFrame): DataFrame containing only the places of interest that are within the user's designated search area
    
    
    """
    
    # Each lat/long degree is ~69.2 miles
    geo_dist = distance / 69.2
    geo_dist = geo_dist * .7

    # Creates boundary limits on the latitude parallel
    lat_plus = latitude + geo_dist
    lat_minus = latitude - geo_dist

    # Creates boundary limits on the longitude parallel
    long_plus = longitude + geo_dist
    long_minus = longitude - geo_dist
    
    long_list = []
    lat_list = []

    # Append to list the longitude coordinates that fall within boundary limits
    for i in df['longitude']:
        if i < long_plus:
            if i > long_minus:
                long_list.append(i)
    
    # Create new dataframe containing only rows containing longitude's within long_list
    df_long = df.loc[df['longitude'].isin(long_list)]

    # Append to list the latitude coiordinates that fall within boundary limits
    for i in df_long['latitude']:
        if i < lat_plus:
            if i > lat_minus:
                lat_list.append(i)
                
    # Create final dataframe containing only rows containing latitude's within lat_list 
    df_final = df_long.loc[df_long['latitude'].isin(lat_list)]
    
    #df_final = df_final.drop('Unnamed: 0', axis=1)
    
    return df_final