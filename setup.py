import os


def download(args):

    if args == 'all':
        _package_download()

    if not os.path.isdir('./khaiii'):
        _khaiii_download()
    else:
        print("khaiii is already installed.")


def _package_download():
    # install requirements
    print("Download python packages.")
    os.system("pip3 install -r requirements.txt")


def _khaiii_download():
    # download khaiii from Github
    print("Download Khaiii")
    os.system("git clone https://github.com/kakao/khaiii.git")

    # build python
    os.system("mkdir khaiii/build")
    os.system("cd khaiii/build && cmake ..")

    os.system("cd khaiii/build && make all && make resource && ctest")

    # Python binding
    os.system("cd khaiii/build && make package_python")
    os.system("cd khaiii/build/package_python && pip3 install .")
