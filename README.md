# video-rename

rename video_files according to create date,  
also can create some extern string.  
such:  
20190325-121500.MP4  
20190325-121500-trip.MP4  

env requires: python3 on windows/macOS

## Usage
for rename one video:  
```
python rename-video.py -i video_path [-s some_extern_string]
```
for rename videos of one folder:
```
python rename-video.py -d -i video_dir [-s some_extern_string]
```