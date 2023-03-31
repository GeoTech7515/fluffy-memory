import os
import shutil

def copy_files(src_folder, dst_folder, partial_filename):
    for filename in os.listdir(src_folder):
        if partial_filename in filename:
            src_path = os.path.join(src_folder, filename)
            dst_path = os.path.join(dst_folder, filename)
            shutil.copy(src_path, dst_path)

src_folder = 'C:\\Users\\Geo\\Desktop\\sno files'
dst_folder = 'D:\\'
partial_filename = input('filename: ')
copy_files(src_folder, dst_folder, partial_filename)