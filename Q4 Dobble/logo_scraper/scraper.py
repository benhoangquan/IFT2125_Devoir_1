import requests
from bs4 import BeautifulSoup
import os

# URL of the website you want to scrape
url = 'https://companiesmarketcap.com'

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all image tags from which you want to scrape logos
# This might need to be adjusted based on the website's structure
logos = soup.find_all('img', class_='company-logo')  # Replace 'your-logo-class' with the actual class used for logos

# Directory where you want to save the logos
save_dir = 'logos'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Loop through all found logos
for i, logo in enumerate(logos[:100], start=1):  # Limit to the first 100 logos
    # Get the logo image source URL
    logo_url = url + logo['src']

    # Get the content of the logo image
    logo_response = requests.get(logo_url)

    # Save the logo image to a file
    with open(os.path.join(save_dir, f'{i}.png'), 'wb') as file:
        file.write(logo_response.content)

    if i >= 100:  # Break the loop after saving 100 logos
        break

print(f'Successfully saved {i} logos in the "{save_dir}" directory.')
