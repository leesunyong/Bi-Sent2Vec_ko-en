import os


def init():
    os.system("pip install -U pip")
    os.system("pip install -r setup/requirements.txt")


def download_all():
    init()
