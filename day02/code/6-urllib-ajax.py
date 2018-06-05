import urllib
import urllib.request

url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start={0}&limit={1}'


# 使用charles 抓包获取了ajax真实的url，请求这类数据和之前网络请求是完全一样
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
           'Accept-Encoding':'',
           'Referer': 'https://movie.douban.com/typerank?type_name=%E5%8A%A8%E4%BD%9C&type=5&interval_id=100:90&action=',
           'Cookie':'bid=Xjj632HO9iI; ll="108288"; __yadk_uid=C1l8ReLhjVA26dwkUNNwvMfAVYxdmn9K; _ga=GA1.2.557027477.1504366471; _vwo_uuid_v2=938EB395FEDF0DA9E9D90650DE9042F0|e0a43720af285a1e9923074545b60ff1; gr_user_id=d044fe6a-3a16-4f08-ad14-cc71033b6767; ue="455098435@qq.com"; __utmv=30149280.16469; viewed="30203973_1088812"; ps=y; push_noty_num=0; push_doumail_num=0; ap=1; _gid=GA1.2.1379291151.1527498290; __utma=30149280.557027477.1504366471.1527498285.1527561166.21; __utmc=30149280; __utmz=30149280.1527561166.21.20.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; gr_cs1_e88f1b22-aa22-4d61-b058-c3991b1f839b=user_id%3A0; __utmb=30149280.2.10.1527561166; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03=e88f1b22-aa22-4d61-b058-c3991b1f839b_true; as="https://music.douban.com/"; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1527562242%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=223695111.557027477.1504366471.1527325981.1527562242.9; __utmb=223695111.0.10.1527562242; __utmc=223695111; __utmz=223695111.1527562242.9.7.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_id.100001.4cf6=b6270075d3f0f249.1516866774.9.1527562390.1527326319.'}


def write2file(content, filename):

    with open(filename,'w',encoding='utf-8') as fp:
        fp.write(content)
        print('保存文件%s成功'%(filename))


    pass


def loadmovie(start, limit, page):

    for p in range(page):

        url_movie = url.format(str((start+limit*p)),str(limit))
        request = urllib.request.Request(url=url_movie,headers=headers)

        response = urllib.request.urlopen(request)

        content = response.read().decode('utf-8')

        filename = './download/'+'第'+str(p+1)+'页.json'

        write2file(content,filename)
    pass


if __name__ == '__main__':

    start = int(input('请输入起始查询索引：'))

    limit = int(input('请输入每一页最多展示的条目：'))

    page = int(input('请输入查询的页数：'))

    loadmovie(start,limit,page)
