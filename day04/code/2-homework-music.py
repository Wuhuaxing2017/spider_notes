import requests
import re
import urllib
import urllib.request
import json

# 第一个接口，根据歌手的名字查询歌曲
url_search_singer = 'http://tingapi.ting.baidu.com/v1/restserver/ting?from=android&version=5.0.0.3&method=baidu.ting.search.catalogSug&format=json&query=%s'


# 歌曲的信息，url
# 肆无忌惮
'''http://tingapi.ting.baidu.com/v1/restserver/ting?from=android&version=5.0.0.3
&method=baidu.ting.song.getInfos&format=json&songid=591579114&ts=1527731331137
&e=Y9CHPGzBMkpzw6qymF7ZxOaHfy9zU0HzRzjwQDWlDuTHY6sYdu%2FmVm371UJEKaE6
&nw=2&fr=sns&ucf=1&res=1&l2p=0&lpb=&usup=1&lebo=0'''

# 百度音乐apk反编译，查看源码！！！ 难度系数增大
# 百度音乐更前面的本版
# 演员
'''http://tingapi.ting.baidu.com/v1/restserver/ting?from=android&version=5.0.0.3
&method=baidu.ting.song.getInfos&format=json&songid=242078437&ts=1527731344280
&e=KEhLaiUVMdT4K92nZqFF6R1SCr1kLlpnAfGa8O3hkIyeJRix%2ByIl5GhHfzjmwxqT
&nw=2&fr=sns&ucf=1&res=1&l2p=0&lpb=&usup=1&lebo=0'''


# 15122721
'''http://tingapi.ting.baidu.com/v1/restserver/ting?from=android&version=5.0.0.3
&method=baidu.ting.song.getInfos&format=json&songid=15122721&ts=1527731344280
&e=KEhLaiUVMdT4K92nZqFF6R1SCr1kLlpnAfGa8O3hkIyeJRix%2ByIl5GhHfzjmwxqT
&nw=2&fr=sns&ucf=1&res=1&l2p=0&lpb=&usup=1&lebo=0'''


# 该接口可以根据一首歌的songid获取这首歌的下载信息
url_songid_url_info = '''http://tingapi.ting.baidu.com/v1/restserver/ting?method=baidu.ting.song.play
&format=jsonp&callback=jQuery17202741599001012014_1513517333931&songid=%s&_=1513517334915'''


def getsonginfo(singer):
    url = url_search_singer%(singer)
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    content = response.text

    # 该数据是json类型的数据
    songs_json = json.loads(content)

    # print(songs_json)

    song_list = songs_json['song']
    # print(song_list)
    songItems = {}
    for song in song_list:
        songname = song['songname']
        songid = song['songid']
        songItems[songname] = songid
    return songItems


def loadmusic(song_url, songname):

    urllib.request.urlretrieve(url=song_url,filename ='./music/%s.mp3'%(songname))

    print('歌曲%s下载成功！'%(songname))

    pass


def getsongurl(songs):

    for songname,songid in songs.items():

        url = url_songid_url_info%(songid)

        response = requests.get(url=url)

        response.encoding = 'utf-8'

        content = response.text

        pattern = re.compile(r'\((.*?)\)',re.S)

        # 正则表达式findall 返回[]
        songinfo = pattern.findall(content)[0]

        # json 类型不匹配
        try:
            songinfo_json = json.loads(songinfo)

            song_url = songinfo_json['bitrate']['file_link']

            loadmusic(song_url,songname)


        except Exception as e:
            print(e,'网络获取的数据，不是一个严格的json类型数据，json解析出问题')

    pass


if __name__ == '__main__':
    singer = input('请输入歌星：')

    # 返回歌曲名称以及songid
    songs = getsonginfo(singer)

    # 该方法获取某一首歌的url
    getsongurl(songs)
