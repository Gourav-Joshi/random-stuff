import argparse
import os
import shutil
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Script for me as a photographer to keep same copy of jpegs/jpgs & raw files in separate folder")
    parser.add_argument('-r', '--raw_folder', help='Raw folder path')
    parser.add_argument('-j', '--jpeg_folder', help='JPEG folder path')
    parser.add_argument('-re', '--raw_extension', default='CR3', help='Raw file extension')
    parser.add_argument('-e', '--jpeg_extension', default='jpeg', help='JPEG file extension')
    parser.add_argument('-d', '--delete', action='store_true', help='Delete = True')
    args = parser.parse_args()
    print(args)
    raw_folder = args.raw_folder
    jpeg_folder = args.jpeg_folder
    raw_extension = args.raw_extension
    jpeg_extension = args.jpeg_extension
    is_delete = args.delete
    delete_dir = 'deleted_raw'

    if not os.path.exists(os.path.join(raw_folder, delete_dir)):
        print(os.path.join(raw_folder, delete_dir))
        if is_delete:
            os.makedirs(os.path.join(raw_folder, delete_dir))            

    jpeg_pics = [ i.split('.{}'.format(jpeg_extension))[0] for i in os.listdir(jpeg_folder) if os.path.isfile(os.path.join(jpeg_folder, i))]
    raw_pics = [ i.split('.{}'.format(raw_extension))[0] for i in os.listdir(raw_folder) if os.path.isfile(os.path.join(raw_folder, i))]

    if len(jpeg_pics) != len(set(jpeg_pics)) or len(raw_pics) != len(set(raw_pics)) :
        sys.exit("Exit because same file name with different extensions exists")
    
    jpeg_pics = set(jpeg_pics)
    raw_pics = set(raw_pics)

    pics_to_delete_from_raw = raw_pics.difference(jpeg_pics)
    for file in pics_to_delete_from_raw:
        print("Item to delete : {}".format(os.path.join(raw_folder, "{}.{}".format(file, raw_extension))))
        if is_delete:
            shutil.move(os.path.join(raw_folder, "{}.{}".format(file, raw_extension)), os.path.join(raw_folder, delete_dir))
