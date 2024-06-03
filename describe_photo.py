"""
This script is used to describe images using a pre-trained image captioning model.
It provides three modes of operation:
1. Translate all images in a folder.
2. Translate all images in all folders in a given folder (recursion method).
3. Translate a single image from the web (pasting captions on the console).

Usage: python describe_photo.py <folder/url> <mode>

Modes:
1: Translate all images in the folder.
2: Translate all images in all folders in the folder (recursion method).
3: Translate a single image from the web (pasting captions on the console).
"""

# import statements...
# import requests
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import glob
import csv
import sys
import os
from urllib import request
import re


# Importing the ssl module
import ssl

# Overriding the default https context creation method in the ssl module
# This is done to fix SSL errors that may occur due to the default context
# The _create_stdlib_context method creates a new SSL context with secure default settings
ssl._create_default_https_context = ssl._create_stdlib_context


def done():
    print("Done.")


def all_folders(folder):

    list_folders = [f for f in glob.glob(f"{folder}/*") if os.path.isdir(f)]
    print(list_folders)
    for dir in list_folders:
        try:
            print(f"current folder : {dir}")
            translate(dir)
        except:
            print("Error")
            continue

# download image from given url and process it
def download_image(url):
    try:
        if not os.path.exists("web"):
            os.makedirs("web")
        # image path to save and use to process
        image = "web/latest.jpg"
        # download image
        request.urlretrieve(url, image)

        # process image

        processor = BlipProcessor.from_pretrained("local_model_procesor")
        model = BlipForConditionalGeneration.from_pretrained(
            "local_model_model")
        images_captions = []
        raw_image = Image.open(image).convert('RGB')

        # conditional image captioning
        text = ""
        inputs = processor(raw_image, text, return_tensors="pt")
        out = model.generate(**inputs)

        # unconditional image captioning
        inputs = processor(raw_image, return_tensors="pt")
        out = model.generate(**inputs)

        descr = processor.decode(out[0], skip_special_tokens=True)
        print(descr)

    except Exception as e:
        print("Error with download: ", e)

# Translate all images in the folder and save it to csv
def translate(folder):
    processor = BlipProcessor.from_pretrained("local_model_procesor")
    model = BlipForConditionalGeneration.from_pretrained("local_model_model")

    csvName = "described_images.csv"
    # Create csv if not exists
    if not os.path.exists(csvName):
        header = ["Name_File", "Caption image"]
        with open(f'{csvName}', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(header)

    # images extensions
    images_extensoes = ["jpg", "jpeg", "png"]

    # list all files in folder with the extensions
    for extensions in images_extensoes:

        # this line will get all files in the folder with the extension
        # if you run script on other OS (i using MacOs and linux), change the / to \\
        list_files = glob.glob(folder+f"/*.{extensions}")

        # Load existing file
        with open(csvName, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=';')
            existing_records = list(reader)

        for image in list_files:

            images_captions = []
            raw_image = Image.open(image).convert('RGB')

            # conditional image captioning
            text = ""
            inputs = processor(raw_image, text, return_tensors="pt")
            out = model.generate(**inputs)

            # unconditional image captioning
            inputs = processor(raw_image, return_tensors="pt")
            out = model.generate(**inputs)

            try:
                descr = processor.decode(out[0], skip_special_tokens=True)


                # Remove "arafed" from description, sometimes model generates this word, datasource have a lot of this word
                descr = re.sub(r'\baraf\w*\b', '', descr, flags=re.IGNORECASE)

                new_record = [image, descr]

                # Check if record exists
                if new_record not in existing_records:

                    images_captions.append(new_record)
                    print(new_record)
                    with open(f'{csvName}', 'a', newline='', encoding='utf-8') as f:
                        writer = csv.writer(f, delimiter=';')
                        writer.writerows(images_captions)
            except Exception as e:
                print("Error", e)
                continue

# Check if model is downloaded and save it locally
def check_if_model_is_downloaded():
    if not os.path.exists("local_model_procesor") or not os.path.exists("local_model_model"):
        print("Downloading model")

        model_to_downlad = "Salesforce/blip-image-captioning-large"
        processor = BlipProcessor.from_pretrained(model_to_downlad)
        model = BlipForConditionalGeneration.from_pretrained(model_to_downlad)
        processor.save_pretrained("local_model_procesor")
        model.save_pretrained("local_model_model")
    else:
        print("Model already downloaded, skipping download...")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        multiine_message = """
        Usage: python describe_photo.py <folder/url> <mode> \n
        modes: \n
        1: Translate all images in the folder \n
        2: Translate all images in all folders in the folder(recursion method) \n
        3: Translate a single image from web(Pasting captions on console) \n
        
        """

        print(multiine_message)

        sys.exit(1)
    else:
        folder = sys.argv[1]
        mode = sys.argv[2]
        if mode == 1 or mode == "1":
            check_if_model_is_downloaded()
            translate(folder)
            done()
        if mode == 2 or mode == "2":
            check_if_model_is_downloaded()
            all_folders(folder)
            done()
        if mode == 3 or mode == "3":
            check_if_model_is_downloaded()
            download_image(folder)
            done()
