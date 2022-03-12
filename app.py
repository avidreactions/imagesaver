import os
import requests
from bs4 import *

def create_folder():
  folder_path = "imagesaver/"
  try:
    folder_name = input("Enter Folder Name:- ")
    os.makedirs(folder_path + folder_name)

  except:
    print("Folder Exist with that name!")
    create_folder()

def grab_images(url):
  print(f"grabbing images from {url}");
  create_folder();

url = input('Please enter url: ');

grab_images(url);