#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import json
import requests
from urllib.request import urlretrieve

URL = "https://storage.googleapis.com/panels-api/data/20240916/media-1a-i-p~s"

# Check if the file exists
if os.path.exists("@mksld_media.json"):
    print("Loading data from local file...")
    with open("@mksld_media.json", 'r') as file:
        data = json.load(file)
else:
    print("Fetching data from official API ...")
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        # Optionally save to local file for next time
        with open("@mksld_media.json", 'w') as file:
            json.dump(data, file)
    else:
        raise Exception(f"Failed to fetch data from official API, status code {response.status_code}")

# Check if we have data
if not data:
    raise ValueError("No data loaded or fetched")

# Directory for saving images
output_dir = 'output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"Created directory: {output_dir}")

# List to store 'dhd' URLs
dhd_urls = []

# Traverse the JSON and collect 'dhd' URLs
for key, value in data.get('data', {}).items():
    if 'dhd' in value:
        dhd_urls.append(value['dhd'])
        print(f"Added URL from item {key}")

print(f"Found {len(dhd_urls)} URLs to download.")

# Download each image
for idx, url in enumerate(dhd_urls, 1):
    try:
        # Generate filename from the last part of the URL
        filename = url.split('/')[-1].split('?')[0]
        filepath = os.path.join(output_dir, f"{idx}_{filename}")
        print(f"Downloading: {url}")
        urlretrieve(url, filepath)
        print(f"Image saved as {filepath}")
    except Exception as e:
        print(f"Failed to download {url}. Error: {e}")

print("All downloads attempted!")