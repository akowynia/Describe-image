# [PL]
# Opis Projektu

Ten projekt to skrypt Pythona, który generuje opisy dla obrazów za pomocą modelu Salesforce/blip-image-captioning-large z biblioteki transformers. Skrypt może przetwarzać obrazy z lokalnego folderu, z wszystkich podfolderów w danym folderze lub z pojedynczego obrazu pobranego z internetu.

Użyty model: 
[Salesforce/blip-image-captioning-large](https://huggingface.co/Salesforce/blip-image-captioning-large) 


Model jest pobierany i zapisywany lokalnie w folderach o nazwach: "local_model_model" oraz "local_model_procesor"

## Funkcje

1. **Opisywanie wszystkich obrazów w folderze**: Skrypt przeszukuje podany folder w poszukiwaniu obrazów i generuje dla nich opisy. Opisy są zapisywane w pliku CSV razem z nazwą pliku obrazu.

2. **Opisywanie wszystkich obrazów we wszystkich podfolderach**: Skrypt przeszukuje podany folder i wszystkie jego podfoldery w poszukiwaniu obrazów i generuje dla nich opisy. Opisy są zapisywane w pliku CSV razem z nazwą pliku obrazu.

3. **Opisywanie pojedynczego obrazu z internetu**: Skrypt pobiera obraz z podanego URL, generuje dla niego opis i wyświetla go na konsoli.

Plik csv jest zapisywany w miejscu w którym jest skrypt, nazwa pliku: described_images.csv


## Wymagania

- Python 3.6 lub nowszy
## Używane biblioteki 🔧

| Biblioteka | Opis |
| --- | --- |
| [transformers](https://github.com/huggingface/transformers) | Biblioteka do pracy z modelami języka naturalnego |
| [PIL (Pillow)](https://pillow.readthedocs.io/en/stable/) | Biblioteka do przetwarzania obrazów |
| [glob](https://docs.python.org/3/library/glob.html) | Biblioteka do przeszukiwania katalogów |
| [csv](https://docs.python.org/3/library/csv.html) | Biblioteka do pracy z plikami CSV |
| [sys](https://docs.python.org/3/library/sys.html) | Biblioteka do pracy z niektórymi zmiennymi używanymi lub utworzonymi przez interpreter Pythona |
| [os](https://docs.python.org/3/library/os.html) | Biblioteka do pracy z systemem operacyjnym |
| [urllib](https://docs.python.org/3/library/urllib.html) | Biblioteka do pracy z URLami |
| [re](https://docs.python.org/3/library/re.html) | Biblioteka do pracy z wyrażeniami regularnymi |
| [ssl](https://docs.python.org/3/library/ssl.html) | Biblioteka do pracy z protokołem SSL |



## Użycie

Aby uruchomić skrypt, użyj jednego z poniższych poleceń:
python describe_photo.py <folder/url> <mode> 
gdzie `<mode>` to tryby: 
1. Opisywanie wszystkich obrazów w folderze
2. Opisywanie wszystkich obrazów we wszystkich podfolderach
3. Opisywanie pojedynczego obrazu z internetu
Gdzie `<folder>` to ścieżka do folderu z obrazami, a `<url>` to adres URL obrazu do pobrania i opisania.

## Licencja

Ten projekt jest dostępny na licencji MIT. Zobacz plik LICENSE dla szczegółów.

# [ENG]
# Project Description

This project is a Python script that generates descriptions for images using the Salesforce/blip-image-captioning-large model from the transformers library. The script can process images from a local folder, from all subfolders in a given folder, or from a single image downloaded from the internet.

Used model: 
[Salesforce/blip-image-captioning-large](https://huggingface.co/Salesforce/blip-image-captioning-large) 

The model is downloaded and saved locally in folders named: “local_model_model” and “local_model_processor”.

## Features

1. **Describing all images in a folder**: The script searches the given folder for images and generates descriptions for them. The descriptions are saved in a CSV file along with the image file name.

2. **Describing all images in all subfolders**: The script searches the given folder and all its subfolders for images and generates descriptions for them. The descriptions are saved in a CSV file along with the image file name.

3. **Describing a single image from the internet**: The script downloads an image from the given URL, generates a description for it, and displays it on the console.

The CSV file is saved in the location where the script is, file name: described_images.csv

## Requirements

- Python 3.6 or newer

## Used Libraries 🔧

| Library | Description |
| --- | --- |
| [transformers](https://github.com/huggingface/transformers) | Library for working with natural language models |
| [PIL (Pillow)](https://pillow.readthedocs.io/en/stable/) | Library for image processing |
| [glob](https://docs.python.org/3/library/glob.html) | Library for directory browsing |
| [csv](https://docs.python.org/3/library/csv.html) | Library for working with CSV files |
| [sys](https://docs.python.org/3/library/sys.html) | Library for working with some variables used or maintained by the Python interpreter |
| [os](https://docs.python.org/3/library/os.html) | Library for working with the operating system |
| [urllib](https://docs.python.org/3/library/urllib.html) | Library for working with URLs |
| [re](https://docs.python.org/3/library/re.html) | Library for working with regular expressions |
| [ssl](https://docs.python.org/3/library/ssl.html) | Library for working with the SSL protocol |


## Usage

To run the script, use one of the following commands:
python describe_photo.py <folder/url> <mode> 
where `<mode>` are the modes: 
1. Describing all images in a folder
2. Describing all images in all subfolders
3. Describing a single image from the internet
Where `<folder>` is the path to the folder with images, and `<url>` is the URL of the image to download and describe.

## License

This project is available under the MIT license. See the LICENSE file for details.