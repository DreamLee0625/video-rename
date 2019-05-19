# coding:utf-8

from __future__ import print_function

import os
import sys
import time
import argparse


VIDEO_END_LIST = ['.avi', '.MOV', '.mp4', '.MP4', '.MTS']


parser = argparse.ArgumentParser(description="default: rename for video_file, env requires: python3 on windows/macOS")
parser.add_argument('--input', '-i', help='input file or dir')
parser.add_argument('--isDir', '-d', action='store_true', help='rename for video_dir') 
parser.add_argument('--ext_str', '-s', default=None, help='ext string in new_name')
args = parser.parse_args()


def process_file(video_file, ext_str=None):
    ### video_path, video_file, video_ext
    video_path, video_name = os.path.split(video_file)
    video_name, video_ext = os.path.splitext(video_name)
    if (video_ext not in VIDEO_END_LIST) or (video_name.startswith('.')):
        raise IOError("This is not a video file. input: [{}]".format(video_file))
    ### begin process
    print("[{}] rename begin...".format(video_file), file=sys.stderr)
    ### modify time
    data = os.stat(video_file)
    ctime = data.st_mtime
    ctime = time.localtime(ctime)
    time_str = time.strftime("%Y%m%d-%H%M%S", ctime)
    ### new name
    if ext_str:
        new_name = "{}.{}{}".format(time_str, ext_str, video_ext)
    else:
        new_name = time_str + video_ext
    new_file = os.path.join(video_path, new_name)
    ### rename
    try:
        os.rename(video_file, new_file)
    except:
        print("[{}] rename err.".format(video_file), file=sys.stderr)
        return False
    print("[{}] rename done.".format(video_file), file=sys.stderr)    
    return True


def process_batch(video_dir, ext_str=None):
    count = 0
    err_count = 0
    for video_name in os.listdir(video_dir):
        video_name, video_ext = os.path.splitext(video_name)
        if (video_ext not in VIDEO_END_LIST) or (video_name.startswith('.')):
            continue
        count += 1
        video_file = os.path.join(video_dir, video_name+video_ext)
        res = process_file(video_file, ext_str=ext_str)
        if not res:
            err_count += 1
    print("total: [{}], err: [{}]".format(count, err_count), file=sys.stderr)

        
if __name__ == "__main__":
    ext_str = args.ext_str
    in_data = args.input
    if args.isDir:
        process_batch(in_data, ext_str)
    else:
        process_file(in_data, ext_str)