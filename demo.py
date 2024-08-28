url="https://xy223x83x92x53xy2409y8738y5011ye40yy5xy.mcdn.bilivideo.cn:4483/upgcxcode/13/56/1429345613/1429345613_x1-1-100026.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1720434220&gen=playurlv2&os=mcdn&oi=1974145043&trid=0000e0101a030e134a5598d03d54b5f124feu&mid=609923881&platform=pc&og=cos&upsig=86de5004667db7becca9d9ef1ef05005&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&mcdnid=50003288&bvc=vod&nettype=0&orderid=0,3&buvid=F177B347-C784-61DF-EEB3-02B37599BE5024989infoc&build=0&f=u_0_0&agrr=1&bw=177030&logo=A0020000"
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0' , 'referer':'https://www.bilibili.com/video/BV1bz42187ub/?spm_id_from=333.1007.top_right_bar_window_history.content.click&vd_source=dc8cd7d687a8fd1da70145f37642a6fd'}
import requests
res = requests.get(url,headers=headers)
print(res.status_code)
open("医疗兵.mp4","wb").write(res.content)

#爬取音频
url="https://xy223x83x92x53xy2409y8738y5011ye40yy5xy.mcdn.bilivideo.cn:4483/upgcxcode/13/56/1429345613/1429345613-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1720434220&gen=playurlv2&os=mcdn&oi=1974145043&trid=0000e0101a030e134a5598d03d54b5f124feu&mid=609923881&platform=pc&og=cos&upsig=3e1df01e0e51e54a2a731eaa936db87b&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&mcdnid=50003288&bvc=vod&nettype=0&orderid=0,3&buvid=F177B347-C784-61DF-EEB3-02B37599BE5024989infoc&build=0&f=u_0_0&agrr=1&bw=22138&logo=A0020000"
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0' , 'referer':'https://www.bilibili.com/video/BV1bz42187ub/?spm_id_from=333.1007.top_right_bar_window_history.content.click&vd_source=dc8cd7d687a8fd1da70145f37642a6fd'}
res = requests.get(url,headers=headers)
print(res.status_code)
open("医疗兵.mp3","wb").write(res.content)

#合成视频
from moviepy.editor import *
视频数据=VideoFileClip('医疗兵.mp4')
音频数据=AudioFileClip('医疗兵.mp3')
最终数据=视频数据.set_audio(音频数据)
最终数据.write_videofile('上帝啊让我再救一个吧.MP4')