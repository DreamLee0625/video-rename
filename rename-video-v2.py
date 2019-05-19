# coding:utf-8

from __future__ import print_function

import os
import sys
import time
import argparse

from moviepy.editor import *

VIDEO_END_LIST = ['.avi', '.MOV', '.mp4', '.MP4']


parser = argparse.ArgumentParser(description="default: rename for video_file, env requires: python3 on windows/macOS")
parser.add_argument('--input', '-i', help='input file or dir')
parser.add_argument('--isDir', '-d', action='store_true', help='rename for video_dir') 
parser.add_argument('--ext_str', '-s', default=None, help='ext string in new_name')
parser.add_argument('--out_format', '-f', default=None, help='trans format of new video file')
args = parser.parse_args()


def process_file(video_file, ext_str=None, out_format=None):
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
    if out_format is not None:
        video_ext = out_format
    if ext_str:
        new_name = "{}.{}{}".format(time_str, ext_str, video_ext)
    else:
        new_name = time_str + video_ext
    new_file = os.path.join(video_path, new_name)
    ### rename
    if out_format is None:
        try:
            os.rename(video_file, new_file)
        except:
            print("[{}] rename err.".format(video_file), file=sys.stderr)
            return False
    else:
        vfc = VideoFileClip(video_file)
        vfc.write_videofile(filename=new_file, remove_temp=False)
    print("[{}] rename done.".format(video_file), file=sys.stderr)    
    return True


def process_batch(video_dir, ext_str=None, out_format=None):
    count = 0
    err_count = 0
    for video_name in os.listdir(video_dir):
        video_name, video_ext = os.path.splitext(video_name)
        if (video_ext not in VIDEO_END_LIST) or (video_name.startswith('.')):
            continue
        count += 1
        video_file = os.path.join(video_dir, video_name+video_ext)
        res = process_file(video_file, ext_str=ext_str, out_format=out_format)
        if not res:
            err_count += 1
    print("total: [{}], err: [{}]".format(count, err_count), file=sys.stderr)

        
if __name__ == "__main__":
    ext_str = args.ext_str
    in_data = args.input
    out_format = args.out_format
    if args.isDir:
        process_batch(in_data, ext_str, out_format)
    else:
        process_file(in_data, ext_str, out_format)