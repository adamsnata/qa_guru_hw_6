import os
import os.path as path
import zipfile
from os.path import basename
from pathlib import Path

from qa_guru_hw_6.utils import path_dir


def test_all_into_one():
    # current_dir = path.dirname(path.abspath(__file__))
    # print('current dir = ', current_dir)
    # resources_dir = path.join(current_dir, 'resources')
    # print('resources dir =', resources_dir)
    # tmp_dir = path.join(current_dir, 'tmp')
    files = os.listdir(path_dir.resources())
    zip_path = path.join(path_dir.tmp(), 'my_archive.zip')

    with zipfile.ZipFile(zip_path, mode='w', compression=zipfile.ZIP_DEFLATED) as my_archive:
        for file in files:
            print(file)
            add_file = path.join(path_dir.resources(), file)
            print(add_file)
            my_archive.write(add_file, basename(add_file))





def extraction_file_path(file_name):
    current_dir = path.dirname(path.abspath(__file__))
    resources_dir = path.join(current_dir, 'resources')
    return path.join(resources_dir, file_name)[1:]


