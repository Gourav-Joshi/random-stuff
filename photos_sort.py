'''
@__author__ = Gourav-Joshi
Usage : Every time when selecting pictures I want to keep same copy of jpegs & raw images.

python photos_sort.py -r <raw_folder path> -j <jpeg_folder path> -re <raw_extension> -e <jpeg_extension> -d 

default values : 
    raw_extension   default='CR3'  
    jpeg_extension  default='jpeg'
    -d delete       false

Don't trust me : Always check all options before executing.
'''
import argparse
import os
import shutil
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Script for me as a photographer to keep same copy of jpegs/jpgs & raw files in separate folder")
    parser.add_argument('-r', '--raw_folder', help='Path to the RAW folder')
    parser.add_argument('-j', '--jpeg_folder', help='Path to the JPEG folder')
    parser.add_argument('-re', '--raw_extension', default='CR3', help='RAW file extension (default: CR3)')
    parser.add_argument('-e', '--jpeg_extension', default='jpeg', help='JPEG file extension (default: jpeg)')
    parser.add_argument('-d', '--delete', action='store_true', help='Delete RAW files not present in JPEG folder (default: False)')
    args = parser.parse_args()

    raw_folder = args.raw_folder
    jpeg_folder = args.jpeg_folder
    raw_extension = args.raw_extension
    jpeg_extension = args.jpeg_extension
    is_delete = args.delete
    delete_dir = 'deleted_raw'

    if is_delete and not os.path.exists(os.path.join(raw_folder, delete_dir)):
        print("RAW files to delete are under this directory", os.path.join(raw_folder, delete_dir))
        os.makedirs(os.path.join(raw_folder, delete_dir))            
    
    jpeg_files = set(os.path.splitext(file)[0] for file in os.listdir(jpeg_folder) if os.path.isfile(os.path.join(jpeg_folder, file)))
    raw_files = set(os.path.splitext(file)[0] for file in os.listdir(raw_folder) if os.path.isfile(os.path.join(raw_folder, file)))
    
    if len(jpeg_files) != len([file for file in os.listdir(jpeg_folder) if os.path.isfile(os.path.join(jpeg_folder, file))]) or len(raw_files) != len([file for file in os.listdir(raw_folder) if os.path.isfile(os.path.join(raw_folder, file))]) :
        sys.exit("Exit because same file name with different extensions exists")

    pics_to_delete_from_raw = raw_files.difference(jpeg_files)
    print("Total numbers of pictures to move : ", len(pics_to_delete_from_raw))
    for file in pics_to_delete_from_raw:
        print("Item to delete : {}.{}".format(file, raw_extension))
        if is_delete:
            shutil.move(os.path.join(raw_folder, "{}.{}".format(file, raw_extension)), os.path.join(raw_folder, delete_dir))
