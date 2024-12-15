import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Mapbox access token (you'll need to set this in .env)
MAPBOX_ACCESS_TOKEN = os.getenv('MAPBOX_ACCESS_TOKEN')

# Estate locations
ESTATES = [
    {
        'name': 'Cenderamata Oil Palm Estate',
        'coords': [117.720694, 4.511972],
        'zoom': 15
    },
    {
        'name': 'Dumpas Oil Palm Estate',
        'coords': [117.720694, 4.511972],
        'zoom': 15
    },
    {
        'name': 'Sungai Indit Oil Palm Estate',
        'coords': [117.697833, 4.660639],
        'zoom': 15
    },
    {
        'name': 'Banita Oil Palm Estate',
        'coords': [117.509333, 4.526500],
        'zoom': 15
    },
    {
        'name': 'Kapilit Oil Palm Estate',
        'coords': [117.509333, 4.526500],
        'zoom': 15
    },
    {
        'name': 'Sungai Tiagau Oil Palm Estate',
        'coords': [117.492083, 4.531611],
        'zoom': 15
    },
    {
        'name': 'Mawang Oil Palm Estate',
        'coords': [117.483028, 4.556444],
        'zoom': 15
    },
    {
        'name': 'Kumansi Oil Palm Estate',
        'coords': [117.449611, 4.478444],
        'zoom': 15
    },
    {
        'name': 'Bukit Tukok Oil Palm Estate',
        'coords': [117.494528, 4.460528],
        'zoom': 15
    },
    {
        'name': 'Kapilit Palm Oil Mill',
        'coords': [117.524139, 4.503361],
        'zoom': 15
    }
]

def generate_satellite_images():
    # Ensure static/estate_images directory exists
    os.makedirs('static/estate_images', exist_ok=True)
    
    for estate in ESTATES:
        # Mapbox Static Images API URL
        url = f'https://api.mapbox.com/styles/v1/mapbox/satellite-v9/static/{estate["coords"][0]},{estate["coords"][1]},{estate["zoom"]}/1000x1000?access_token={MAPBOX_ACCESS_TOKEN}'
        
        # Filename for the image
        filename = f'static/estate_images/{estate["name"].lower().replace(" ", "_")}_satellite.jpg'
        
        try:
            # Download the image
            response = requests.get(url)
            response.raise_for_status()
            
            # Save the image
            with open(filename, 'wb') as f:
                f.write(response.content)
            
            print(f'Generated image for {estate["name"]}')
        except Exception as e:
            print(f'Error generating image for {estate["name"]}: {e}')

if __name__ == '__main__':
    generate_satellite_images()
