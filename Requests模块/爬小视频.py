import requests
"""
爬取梨视频
1.寻找真实的视频地址
2.打开单独视频页面，发现<video>标签是js 动态加载
3.尝试在原始页面寻找视频地址，没有，说明是动态渲染
4.发现页面打开会发送一个ajax请求，里面有相似度极高的视频地址
5.分析发现，将视频的id号进行拆开拼接就可以等到真实地址
6.ajax请求没有正常响应，有一个反爬，refer验证了调转页面
7.伪造请求头，成功得到数据
"""
# https://www.pearvideo.com/
# https://www.pearvideo.com/category_loading.jsp?reqType=5
# &categoryId=4&start=60&mrd=0.9487643338815096&
from typing import List, Tuple, Dict

import requests

res = requests.get('https://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=4&start=0')
# print(res.text)

import re
import json
pattern = '<a href="(.*?)" class="vervideo-lilink actplay">'
urls: List[str] = re.findall(pattern, res.text)
print(urls)

for url in urls:
    contId = url.split('_')[-1]
    refer = 'https://www.pearvideo.com/' + url
    header ={
        'Referer': refer
    }
    video_url = 'https://www.pearvideo.com/videoStatus.jsp?contId={}&mrd=0.2150472099005749'.format(contId)

    res_video = requests.get(video_url,headers=header)

    print(res_video.text)
    result = json.loads(res_video.text)

    systemTime = result['systemTime']
    srcUrl: str= result['videoInfo']['videos']['srcUrl']

    # 真实视频地址
    real_video_url = srcUrl.replace(systemTime,'cont-{}'.format(contId))

    video = requests.get(real_video_url).content

    with open('{}.mp4'.format(contId),'wb') as f:
        f.write(video)





    break
