#coding=utf-8
__author__ = 'tangyao'

import os
import zipfile

from config.global_config import REPORT_END_PATH, ZIP_DIR, ZIP_File_DIR


def report_zip():
    ZIP_File="report.zip"
    ZIP_File_Name=os.path.join(os.path.dirname(ZIP_DIR),"zip")
    if not os.path.exists(ZIP_File_Name):
        os.mkdir(ZIP_File_Name)
    f=zipfile.ZipFile(os.path.join(ZIP_File_Name,ZIP_File),"w",zipfile.ZIP_DEFLATED)
    for dir_path,dir_names,filenames in os.walk(ZIP_File_DIR):
        file_path=dir_path.replace(ZIP_File_DIR,"")
        file_path = file_path and file_path + os.sep or ''
        for file_name in filenames:
            if "report_" in dir_path:
                f.write(os.path.join(dir_path,file_name),file_path+file_name)
    f.close()
if __name__ == '__main__':
    report_zip()
