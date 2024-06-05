import unittest
import os
import sys
import subprocess

from describe_photo import check_if_model_is_downloaded


class TestCheckIfModelIsDownloaded(unittest.TestCase):
    def test_check_if_model_is_downloaded(self):
        # Call the function
        check_if_model_is_downloaded()

        # Check if the directories exist
        self.assertTrue(os.path.exists("local_model_procesor"))
        self.assertTrue(os.path.exists("local_model_model"))

class TestDescribePhoto(unittest.TestCase):
    def test_translate_folder(self):
        # Run the script with mode 1
        subprocess.run(["python3.11", "describe_photo.py", "test_folder", "1"])
        # Check if the CSV file was created
        self.assertTrue(os.path.exists("described_images.csv"))

    def test_download_image(self):
        # Run the script with mode 3
        subprocess.run(["python3.11", "describe_photo.py", "https://avatars.githubusercontent.com/u/23085819?s=400&v=4", "3"])
        # Check if the image was downloaded
        self.assertTrue(os.path.exists("web/latest.jpg"))

if __name__ == '__main__':
    unittest.main()