#爬取视频部分
url="https://www.example.com/xxxx"
headers={'user-agent':'xxxxxxxxxxx'}
import requests
res = requests.get(url,headers=headers)
print(res.status_code)
open("hhhh.mp4","wb").write(res.content)

#爬取音频
url="https://www.example.com/xxxxx"
headers={'user-agent':'xxx' , 'referer':'xxxx'}
res = requests.get(url,headers=headers)
print(res.status_code)
open("hhhh.mp3","wb").write(res.content)

#合成视频
from moviepy.editor import *
视频数据=VideoFileClip('hhhh.mp4')
音频数据=AudioFileClip('hhhh.mp3')
最终数据=视频数据.set_audio(音频数据)
最终数据.write_videofile('这个是爬取视频.MP4')