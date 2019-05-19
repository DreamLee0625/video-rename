# video-rename

rename video_files according to create date,  
also can create some extern string.  
such:  
DJI0001.MP4 -> 20190325-121500.MP4  
DJI0001.MP4 -> 20190325-121500-trip.MP4  
DJI0001.MOV -> 20190325-121500-trip.MP4  

env requires: python3 on windows/macOS  
V1 and V2 scripts are independent of each other  
requires moviepy in rename-video-v2.py  

## Usage
for rename one video:  
```
python rename-video-v1.py -i video_path [-s some_extern_string]
```
for rename videos of one folder:
```
python rename-video-v1.py -d -i video_dir [-s some_extern_string]
```
And format conversion function is provided in V2 script:  
for rename and conversion one video:  
```
python rename-video-v2.py -i video_path [-s some_extern_string] [-f new_format, such '.mp4']
```
for rename and conversion videos of one folder:
```
python rename-video-v2.py -d -i video_dir [-s some_extern_string] [-f new_format, such '.mp4']
```