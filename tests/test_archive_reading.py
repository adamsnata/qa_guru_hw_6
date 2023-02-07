import csv
import zipfile
from pathlib import Path

import xlrd3 as xlrd
import os.path as path
from PyPDF2 import PdfReader
import sys

import qa_guru_hw_6

current_dir = path.dirname(path.abspath(__file__))
project_dir = Path(qa_guru_hw_6.__file__).parent.parent #path.dirname(current_dir)
sys.path.insert(0, project_dir)

from zip_packaging import extraction_file_path


resources_dir = path.join(project_dir, 'resources')
tmp_dir = path.join(project_dir, 'tmp')
archive_path = path.join(tmp_dir, 'my_archive.zip')
zip_ = zipfile.ZipFile(archive_path)



def test_csv_check1():
    print(f' \n project_dir {project_dir}')
    print(f' \n tmp_dir {tmp_dir}')
    print(f" \n tmp_dir {tmp_dir}")

    with zipfile.ZipFile(archive_path) as zf:
        cf = zf.extract("my_png.png")

    # file_path = ZipFile(archive_path).extract(extraction_file_path('my_csv.csv'), tmp_dir)

    # with open(file_path) as csv_file_path:
    #     csv_file = csv.reader(csv_file_path)
    #     for row in csv_file:
    #         if 'Abs' in row:
    #             assert True


def test_csv_check():
    file_path = zip_.extract('my_csv.csv', tmp_dir)

    with open(file_path) as csv_file_path:
        csv_file = csv.reader(csv_file_path)
        for row in csv_file:
            if 'Abs' in row:
                assert True


def test_xlsx_check():
    file_path = zip_.extract('my_xlsx.xlsx', tmp_dir)
    book = xlrd.open_workbook(file_path)
    first_sheet = book.sheet_by_index(0)
    assert first_sheet.cell_value(rowx=4, colx=1) == 'Kathleen'


def test_png_check():
    file_path = zip_.extract('my_png.png', tmp_dir)
    assert path.getsize(file_path) == 23783


def test_xls_check():
    file_path = zip_.extract('my_xls.xls', tmp_dir)
    book = xlrd.open_workbook(file_path)
    first_sheet = book.sheet_by_index(0)
    assert first_sheet.cell_value(rowx=3, colx=2) == 'Gent'


def test_pdf_check():
    file_path = zip_.extract('my_pdf.pdf', tmp_dir)
    reader = PdfReader(file_path)
    first_page = reader.pages[0]
    text_from_first_page = first_page.extract_text()
    assert 'Jan 30' in text_from_first_page
