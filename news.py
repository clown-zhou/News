import requests
import json
import time
import re
class New():
    def __init__(self):
        self.headers = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',}
        self.authority = 'feed.mix.sina.com.cn'
        self.referer = 'https://news.sina.com.cn/roll/'
        self.path = 'api/roll/get?pageid=153&lid=2509&k=&num=50&page=1&r=0.25875248806596374&callback=jQuery111219038953616241436_{0}&_={1}'.format(time.time(),time.time())
        self.accept_encoding = 'gzip,deflate,br'
        self.method = 'GET'
        self.scheme = 'https'
        self.accept = '*/*'
        self.accept_language = 'zh-CN,zh;q=0.9'

    def get_news(self):
        data = {
            'referer': self.referer,
            ':authority': self.authority,
            ':path': self.path,
            'accept-encoding':self.accept_encoding,
            ':method':self.method,
            ':scheme':self.scheme,
            'accept':self.accept,
            'accept-language': self.accept_language,

        }
        url = 'https://' + self.authority + '/' + self.path
        # print(url)
        s = requests.session()
        response = s.get(url, headers=self.headers,params=data).text

        response1 = re.findall('try{jQuery.*?\((.*?)\);}catch\(e\){};',response)[0]
        return response1
    def _return_data(self):
        response = self.get_news()
        datas = json.loads(response)['result']['data']

        for data in datas:

            # print(data['hasVideo'])#判断是否有视频
            title = data['title']

            print('标题:>>',title)
            content_url = (data['wapurls'].replace('\\', ''))

            print('内容链接:>>',content_url)
            # for wapurl in (data['wapurls'].replace('\\', '')).replace(']',',]').replace('\"','\''):
            #     print(wapurl)
            intro = data['intro']

            print('介绍:>>',intro)
            image_dict = {}
            for image in data['images']:
                image_dict[image['u']] = image['t']
                # print(image['u'])
            print('图片:>>',image_dict)

            keywords = data['keywords']

            print('关键字:>>',keywords)



if __name__== "__main__":
    new = New()
    new._return_data()