"""
Ubuntu-Inspired Image Fetcher
"I am because we are"
This script fetches images from the internet respectfully and saves them locally.
"""

import os
import requests
from urllib.parse import urlparse

# Part 1: Prompt the user for a URL
url = input("🌐 Enter the image URL: ").strip()

# Part 2: Create directory "Fetched_Images" if it doesn't exist
directory = "Fetched_Images"
os.makedirs(directory, exist_ok=True)

try:
    # Part 3: Fetch the image from the URL
    response = requests.get(url, timeout=10)
    
    # Part 4: Check for HTTP errors
    response.raise_for_status()
    
    # Part 5: Extract filename from URL
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    
    # If filename is empty, generate one
    if not filename:
        filename = "downloaded_image.jpg"
    
    # Full path for saving image
    filepath = os.path.join(directory, filename)
    
    # Part 6: Save image in binary mode
    with open(filepath, "wb") as file:
        file.write(response.content)
    
    print(f"✅ Success! Image saved to: {filepath}")

except requests.exceptions.MissingSchema:
    print("❌ Error: Invalid URL. Please enter a proper image link.")

except requests.exceptions.HTTPError as http_err:
    print(f"❌ HTTP error occurred: {http_err}")

except requests.exceptions.ConnectionError:
    print("❌ Connection error: Unable to connect to the server.")

except requests.exceptions.Timeout:
    print("❌ Timeout error: The request took too long to respond.")

except Exception as err:
    print(f"❌ Unexpected error: {err}")