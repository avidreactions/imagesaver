import os

def create_folder():
  try:
    folder_name = input("Enter Folder Name:- ")
    os.mkdir(folder_name)

  except:
    print("Folder Exist with that name!")
    create_folder()


def grab_images(url):
  print(f"grabbing images from {url}");
  create_folder();

url = input('Please enter url: ');

grab_images(url);