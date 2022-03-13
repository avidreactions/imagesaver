import os
import requests
from bs4 import *

def download_images(images, full_folder_path):
  count = 0;
  print(f"total {len(images)} have been found!");
  print(f"The images will be saved to {full_folder_path}");

def create_folder(images):
  try:
    folder_name = input("Enter Folder Name: ")
    full_folder_path = "imagesave/" + folder_name;
    os.makedirs(full_folder_path + folder_name);

  except:
    print("Folder Exist with that name!")
    create_folder()
  download_images(images, full_folder_path)

def grab_images(url):
  print(f"grabbing images from {url}");
  
  url_request = requests.get(url);

  soup = BeautifulSoup(url_request.text, "html.parser");

  images = soup.findAll('img');

  create_folder(images);

url = input('Please enter url: ');

grab_images(url);