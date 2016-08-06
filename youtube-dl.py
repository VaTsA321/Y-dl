from urllib.request import urlretrieve, urlopen
from urllib.parse import parse_qs
import os
import sys
import re

def video_get(video_id):
    url = 'http://www.youtube.com/get_video_info?video_id=' + video_id
    print(url)
    html = (urlopen(url).read())
    kk  = html.decode('utf-8')
    info = parse_qs(kk)
    title = info['title'][0] + '.mp4'
    #print(title)
    url_encoded_fmt_stream_map = info['url_encoded_fmt_stream_map'][0].split(',')
    entrys = [parse_qs(entry) for entry in url_encoded_fmt_stream_map]
    video_url_map = [dict(url=entry['url'][0], type=entry['type']) for entry in entrys]
    type = 'video/mp4'
    for etry in video_url_map:
        etry_type = etry['type'][0]
        etry_type = etry_type.split(';')[0]
        if etry_type.lower() == type.lower():
            main_url = etry['url']
            break
    print('Downloading...')
    urlretrieve(main_url, title)
    print('Done')
    
def main():
    link = sys.argv[1]
    video_id = re.search(r'watch\?v=(\S+)', link).group(1)
    video_get(video_id)

if(__name__ == '__main__'):
    main()
