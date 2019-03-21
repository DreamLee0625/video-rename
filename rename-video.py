# coding:utf-8


import os
from pymediainfo import MediaInfo


video_file = "/home/lixiang/Desktop/C0001.MP4"
media_info = MediaInfo.parse(video_file)


# def main(video_dir):
#     for video_name in os.listdir(video_dir):
#         video_file = os.path.join(video_dir, video_name)
#         print(video_file)
#         media_info = MediaInfo.parse(video_file)
#         data = media_info.to_data()
#         print(data)
#         break


# if __name__ == "__main__":
#     video_dir = "/media/lixiang/storageSSD1/raw"
#     main(video_dir)