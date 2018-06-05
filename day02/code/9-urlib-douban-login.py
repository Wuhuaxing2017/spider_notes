import urllib
import urllib.request

# url = 'https://www.douban.com/people/164698173/'

url = 'https://weibo.com/5505440936/profile?topnav=1&wvr=6&is_all=1'

# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
#            'Cookie':'bid=Xjj632HO9iI; __yadk_uid=pEzIj2tEWsS125GeVKf5SN8rcRRkfmyt; ll="108288"; _ga=GA1.2.557027477.1504366471; _vwo_uuid_v2=938EB395FEDF0DA9E9D90650DE9042F0|e0a43720af285a1e9923074545b60ff1; gr_user_id=d044fe6a-3a16-4f08-ad14-cc71033b6767; ue="455098435@qq.com"; __utmv=30149280.16469; viewed="30203973_1088812"; ps=y; push_noty_num=0; push_doumail_num=0; ap=1; _gid=GA1.2.1379291151.1527498290; __utmc=30149280; dbcl2="164698173:3ohBXfsojGY"; ck=2uA6; gr_cs1_4a53112a-4db5-4d56-b2d3-0d9702115551=user_id%3A1; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03=4a53112a-4db5-4d56-b2d3-0d9702115551_true; __utma=30149280.557027477.1504366471.1527561166.1527575013.22; __utmz=30149280.1527575013.22.21.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/accounts/login; __utmt_douban=1; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1527575118%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DCAg9GaguG436g6WA1E_utnq5M3-RdHy3qKmhOGgZe5s6RrEANoyxOBfYdN1TUABI%26wd%3D%26eqid%3Dd980c39b000071e6000000025b0cbbc5%22%5D; _pk_ses.100001.8cb4=*; __utmt=1; _pk_id.100001.8cb4=8f22acb72a922fec.1516867546.17.1527575229.1527562375.; __utmb=30149280.5.10.1527575013'}


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
           'Cookie':'SINAGLOBAL=1975597719071.4558.1504621557846; UM_distinctid=163022f9e316c2-03ca3591fb1bd5-5a442916-144000-163022f9e32446; wvr=6; TC-Ugrow-G0=370f21725a3b0b57d0baaf8dd6f16a18; ALF=1559111932; SSOLoginState=1527575933; SCF=AjIaSk-Iaw9qpELQkSKKHAq5gABMufZk7b_94DVXme4p9J50H-CuQ-m0poSM4Ul4BeczrZhqso163m6oXuCUHpw.; SUB=_2A252CIUtDeRhGeNL61cV9C7FyDqIHXVVf_HlrDV8PUNbmtAKLU7ukW9NSSXTuy444JH50Vx2C-_lg4tQs9U9kMST; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5T.g9wuaG_cPO.3KIyaOAj5JpX5KzhUgL.Fo-feh-XSh54e0q2dJLoI0qLxKqLB-qL12qLxKqL1KMLBoqLxKqLB-qL12qLxK-L1hnLB.zLxKMLB.-L12-LxK.LBKeL1-qt; SUHB=0tKalLBDtphW0c; TC-V5-G0=589da022062e21d675f389ce54f2eae7; _s_tentry=login.sina.com.cn; UOR=,,www.baidu.com; Apache=7926059196193.811.1527575933273; ULV=1527575933331:10:3:2:7926059196193.811.1527575933273:1527520518724; TC-Page-G0=1bbd8b9d418fd852a6ba73de929b3d0c'}



request  = urllib.request.Request(url=url,headers=headers)


# urllib.error.HTTPError: HTTP Error 403: Forbidden,禁止访问
response = urllib.request.urlopen(request)

print(response.read().decode('utf-8'))