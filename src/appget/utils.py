import os
import shutil

import requests

from appget import log

# develop
DEBUG = os.environ.get('APPGET_MODE', '').lower() == 'debug'


def copy_file_or_folder(source, destination):
    """
    拷贝单个文件或整个文件夹及其子目录。
    """
    if os.path.isfile(source):
        if not os.path.exists(destination):
            os.makedirs(destination)
        shutil.copy2(source, destination)
    elif os.path.isdir(source):
        basename = os.path.basename(source)
        destination = os.path.join(destination, basename)
        shutil.copytree(source, destination, dirs_exist_ok=True)
    else:
        log.error("Error: {} is not a valid file or directory".format(source))


def download(url, destination):
    try:
        log.info(f'Downloading: {url}')
        response = requests.get(url)
        if response.status_code == 200:
            with open(destination, 'wb') as f:
                f.write(response.content)
            log.info(f'Downloaded and saved: {destination}')
        else:
            log.error(f'Download failed with status code: {response.status_code}')
    except Exception as e:
        log.error(f'Download failed: {e}')
