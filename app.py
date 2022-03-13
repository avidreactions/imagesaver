import os
import requests
from bs4 import *

def create_folder(images):
  try:
    folder_name = input("Enter Folder Name: ")
    full_path = "imagesaver/" + folder_name
    os.makedirs(full_path);

  except:
    print("Folder Exist with that name!")
    create_folder()
  download_images(images, full_path)

def download_images(images, folder_name):
  count = 0;
  print(f"total {len(images)} have been found!");

  if len(images) != 0:
    for i, image in enumerate(images):

      try:
        image_link = image["src"]

      except:
        pass

      try:
        request = requests.get(image_link).content;

        try:
          request = str(request, 'utf-8');

        except UnicodeDecodeError:
          with open(f"{folder_name}/images{i+1}.jpg", "wb+") as f:
            f.write(request);

          count += 1;
      except:
        pass;

    if count == len(images):
      print("All images have been downloaded!");

    else:
      print(f"Total {count} images downloaded out of {len(images)}");

def grab_images(url):
  print(f"grabbing images from {url}");
  
  url_request = requests.get(url);

  soup = BeautifulSoup(url_request.text, "html.parser");

  images = soup.findAll('img');

  create_folder(images);

url = input('Please enter url: ');

grab_images(url);