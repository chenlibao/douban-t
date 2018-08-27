#1.表单交互
# import requests
# url = 'https://www.douban.com/'
# params = {
#     'source':'index_nav',
#     'form_email':'15210647516',
#     'form_password':'clb891212'
# }
# html = requests.post(url,params)
# print(html.text)

#2.模拟登陆 --提交cookie模拟登陆  cookie:存储信息的本地文件
#
# import requests
# url = 'https://www.douban.com'
# headers = {
#     'Cookies':'bid=LsnijblZKm8; __yadk_uid=ASowBaI01wSocGRTX6cviOd6jlwl22D7; gr_user_id=7c0b7d76-7fe9-4565-8c9c-20328aab1f48; ll="108296"; _vwo_uuid_v2=BFA5F87D29CCA9CF0E6C98C2E6A76E74|e7bb905d0fb4ee9bf4d10ed963ac4470; __utmv=30149280.17370; viewed="26961851_26419787_27622006_25829645_27173829_27204860_25746586"; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1523865178%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D-kGT_7g0-8lelqnBYPSlzMbuVtk3zE1wtPnfoVdYkjQJUrO-Ckq176wk6nuZnOL7%26wd%3D%26eqid%3Dc39f84170000aa0b000000025ad45655%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.322048557.1499912483.1523336843.1523865179.24; __utmc=30149280; __utmz=30149280.1523865179.24.22.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _ga=GA1.2.322048557.1499912483; _gid=GA1.2.1367545102.1523865628; push_noty_num=0; push_doumail_num=0; ap=1; _pk_id.100001.8cb4=7741d04049e8d64e.1499912483.29.1523866004.1523336842.; __utmt=1; __utmb=30149280.4.10.1523865179'
# }
# html = requests.get(url,headers=headers)
# print(html.text)


#拉勾网案例分析
#1.我们已知的是url和单个的表单params（因为是Ajax，所以url就是唯一的一个，它是通过表单的形式来提交的，这里的变量就成了params）
#  __name__ =='__main__' 中传入的已知信息就是url和params，而page是变化的，是需要我们获取的，所以需要传入get_page(url,params)
#2.需要构造get_page(url,params),通过获得通过已知的url,params访问网站，可以获取json文件（json.loads(html.text()),用键取得
# total_count，从而计算出总的page，获得page后，那么我们就可以取得每一页的信息了，将page传入到get_info(url,page)
#3.构造get_info（url,page)函数，因为page是在params中的，所以我们需要用for in 遍历形成多个params
# for pn in range(1,page+1）因为需要取到page页，所以需要page+1. 这里传入的page是数值型的，但params中pn是字符串，所以要用str(pn)
# 每一个params都需要进行获取结果信息,所以我们需要对每一个params进行访问，用loads获取json文件，用key-d取结果，其result也是一个json文件，
# 属于字典类型，我们将每一个值构造一个新的字典infos(比较困惑为何要这样），然后传入到db中去，每一次try都休息2s，except信息就填连接错误
#4.运用到的模块：math(math.ceil()向上取整） time（time.sleep(2)） json( json.loads(html.text)获取html的文件） MongoClient
# （连接数据库） requests(访问url（get获取，post上传登录）

import requests
import math
import pymongo
import time
import json

client = pymongo.MongoClient('localhost',27017)
mydb = client['mydb']
lagou = mydb['lagou']
headers = {
    'xxx':'xxx'
}

def get_page(url,params):
    html = requests.post(url,data=params,headers=headers)
    json_data = json.loads(html.text)
    totalcount = json_data['content']['totalCount']
    page_numbers = math.ceil(totalcount/15) if math.ceil(totalcount/15) <30 else 30
    get_info(url,page_numbers)

def get_info(url,page):
    for pn in range(1,page+1):
        params = {
            'first': 'false',
            'pn': str(pn),
            'kd': 'Java'
        }
        try:
            html = requests.post(url,data=params,headers=headers)
            json_data = json.loads(html.text)
            results = json['content']['']['result']
            for result in results:
                data = {
                    'xxx':result['xxx'],
                    'xxx':result['xxx']
                }
                lagou.insert(data)
                print(data)
            time.sleep(2)
        except requests.exceptions.ConnectionError:
            pass
if __name__ == "__main__":
    url = 'https://www.lagou.com/zhaopin/Java/30/?filterOption=31'
    params = {
        'first': 'true',
        'pn': '1',
        'kd': 'Java'
    }
    get_page(url,params)