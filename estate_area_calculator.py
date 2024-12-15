import math

def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # Convert decimal degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    
    # Radius of earth in kilometers
    r = 6371
    
    # Calculate the distance
    return c * r

def estimate_estate_area(center_lat, center_lon, reported_size_ha):
    """
    Estimate estate area based on reported size and center coordinates
    
    Args:
        center_lat (float): Latitude of estate center
        center_lon (float): Longitude of estate center
        reported_size_ha (float): Reported size in hectares
    
    Returns:
        dict: Estimated boundaries and area details
    """
    # Approximate side length of a square estate
    side_length_km = math.sqrt(reported_size_ha / 100)
    
    # Calculate corner coordinates (simple approximation)
    half_side = side_length_km / 2
    
    # Adjust for latitude and longitude differences
    lat_diff = half_side / 111  # 1 degree of latitude ≈ 111 km
    lon_diff = half_side / (111 * math.cos(math.radians(center_lat)))
    
    # Define boundary coordinates
    boundaries = {
        'northwest': [center_lon - lon_diff, center_lat + lat_diff],
        'northeast': [center_lon + lon_diff, center_lat + lat_diff],
        'southwest': [center_lon - lon_diff, center_lat - lat_diff],
        'southeast': [center_lon + lon_diff, center_lat - lat_diff]
    }
    
    # Calculate approximate distances between corners
    nw_to_ne = haversine_distance(
        boundaries['northwest'][1], boundaries['northwest'][0],
        boundaries['northeast'][1], boundaries['northeast'][0]
    )
    nw_to_sw = haversine_distance(
        boundaries['northwest'][1], boundaries['northwest'][0],
        boundaries['southwest'][1], boundaries['southwest'][0]
    )
    
    # Estimated area
    estimated_area = nw_to_ne * nw_to_sw
    
    return {
        'name': 'Estimated Area',
        'center': [center_lon, center_lat],
        'reported_size': reported_size_ha,
        'estimated_area_sq_km': round(estimated_area, 2),
        'estimated_area_ha': round(estimated_area * 100, 2),
        'boundaries': boundaries
    }

# Estate data
estates = [
    {
        'name': 'Cenderamata Oil Palm Estate',
        'coords': [117.720694, 4.511972],
        'reported_size': 53
    },
    {
        'name': 'Dumpas Oil Palm Estate',
        'coords': [117.720694, 4.511972],
        'reported_size': 53
    },
    {
        'name': 'Sungai Indit Oil Palm Estate',
        'coords': [117.697833, 4.660639],
        'reported_size': 70
    },
    {
        'name': 'Banita Oil Palm Estate',
        'coords': [117.509333, 4.526500],
        'reported_size': 65
    },
    {
        'name': 'Kapilit Oil Palm Estate',
        'coords': [117.509333, 4.526500],
        'reported_size': 79
    },
    {
        'name': 'Sungai Tiagau Oil Palm Estate',
        'coords': [117.492083, 4.531611],
        'reported_size': 82
    },
    {
        'name': 'Mawang Oil Palm Estate',
        'coords': [117.483028, 4.556444],
        'reported_size': 83
    },
    {
        'name': 'Kumansi Oil Palm Estate',
        'coords': [117.449611, 4.478444],
        'reported_size': 91
    },
    {
        'name': 'Bukit Tukok Oil Palm Estate',
        'coords': [117.494528, 4.460528],
        'reported_size': 87
    }
]

# Calculate and print estate areas
print("Estate Area Calculations:")
print("-" * 50)

for estate in estates:
    result = estimate_estate_area(
        estate['coords'][1], 
        estate['coords'][0], 
        estate['reported_size']
    )
    
    print(f"{estate['name']}:")
    print(f"  Reported Size: {estate['reported_size']} ha")
    print(f"  Estimated Area: {result['estimated_area_ha']} ha")
    print(f"  Center Coordinates: {estate['coords']}")
    print("-" * 50)
