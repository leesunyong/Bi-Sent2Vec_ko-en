# Download initial required packages
#   Some packages are required to download Khaiii.

import os


def download_all():
    os.system("pip install -U pip")
    os.system("pip install -r setup/requirements.txt")
