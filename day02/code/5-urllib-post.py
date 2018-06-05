import urllib
import urllib.request
import urllib.parse
import json
url = 'http://fanyi.baidu.com/v2transapi'

'''from=zh&to=en&query=%E5%9B%BE%E7%89%87&transtype=realtime&simple_means_flag=3&
sign=76488.379385&token=6c98653b52133a314c97d378260dd23f'''

word = input('请输入要翻译的汉字：')

# word = urllib.parse.quote(word)

# !!! 有写post请求，对form表单，非常严格
form = {'from':'zh',
        'to':'en',
        'query':word,
        'transtype':'realtime',
        'simple_means_flag':'3',
        'sign':'76488.379385',
        'token':'6c98653b52133a314c97d378260dd23f'}

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
           'Accept-Encoding':'',
           'Origin': 'http://fanyi.baidu.com',
           'Referer': 'http://fanyi.baidu.com/?aldtype=16047',
           'Cookie':'__cfduid=d4239d00cf28765faa236f6608b6608881505905792; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; PSTM=1516063589; BAIDUID=08FF61A25E088F1E52D00EFF1BF6553D:SL=0:NR=50:FG=1; BIDUPSID=3F36E6E1D84B20491F59AC388BCE71F2; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; BDUSS=dkZ1gwSGUzR2hvQ2VER2tVZURRbk51MTlBMzgzRURZRmNTRThjcmNNc0x0ak5iQVFBQUFBJCQAAAAAAAAAAAEAAADcsb9ywre34cCkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAspDFsLKQxbQk; PSINO=2; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; BDRCVFR[tox4WRQ4-Km]=mk3SLVN4HKm; H_PS_PSSID=1433_21119_26350_20928; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1527219467,1527496949,1527560247; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1527560247; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D'}


params = urllib.parse.urlencode(form).encode('utf-8')
print(params)
request = urllib.request.Request(url = url,data = params,headers = headers)

response = urllib.request.urlopen(request)

content = response.read()

print(json.loads(content.decode('utf-8')))

print(content.decode('unicode-escape'))