from decorators import run_time
import requests
import json
import time
import csv
import re


class New:
    def __init__(self):
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
         Chrome/69.0.3497.100 Safari/537.36'
        self.authority = 'feed.mix.sina.com.cn'
        self.referer = 'https://news.sina.com.cn/roll/'
        self.path = 'api/roll/get?pageid=153&lid=2509&k=&num=50&page=1&r=0.25875248806596374\
        &callback=jQuery111219038953616241436_{0}&_={1}'.format(time.time(), time.time())
        self.accept_encoding = 'gzip,deflate,br'
        self.method = 'GET'
        self.scheme = 'https'
        self.accept = '*/*'
        self.accept_language = 'zh-CN,zh;q=0.9'

    @run_time
    def get_news(self):
        headers = {'user-agent': self.user_agent}
        params = {
            'referer': self.referer,
            ':authority': self.authority,
            ':path': self.path,
            'accept-encoding': self.accept_encoding,
            ':method': self.method,
            ':scheme': self.scheme,
            'accept': self.accept,
            'accept-language': self.accept_language,
        }
        url = 'https://' + self.authority + '/' + self.path
        s = requests.session()
        response = s.get(url, headers=headers, params=params).text
        p = re.compile(r"try{jQuery.*?\((.*?)\);}catch\(e\){};")
        response1 = p.findall(response)[0]
        return response1

    @run_time
    def iter_data(self):
        response = self.get_news()
        datas = json.loads(response)['result']['data']
        for data in datas:
            title = data.get('title')
            # print('标题:>>', title)
            # print(data.get('wapurls'))
            p = re.compile(r"(http://[\w+./\-]+)")
            content_url_list = [p.findall(data.get('wapurls').replace('\\', ''))][0]
            # print('内容链接:>>>', content_url_list)
            intro = data.get('intro')
            # print('介绍:>>>', intro)
            image_dict = {}
            for image in data.get('images'):
                image_dict[image.get('u')] = image.get('t')
            # print('图片:>>>', image_dict)
            keywords = data.get('keywords')
            # print('关键字:>>>', keywords)
            yield {'title': title, 'content_url_list': content_url_list,
                   'intro': intro, 'image_dict': image_dict, 'keywords': keywords}

    @staticmethod
    @run_time
    def save_csv(data):
        with open('new.csv', 'a', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            line_one = ['title', 'content_url_list', 'intro', 'image_dict', 'keywords']
            writer.writerow(line_one)
            for row in data:
                datas = [row.get('title'), row.get('content_url_list'), row.get('intro'),
                         row.get('image_dict'), row.get('keywords')]
                # print(row.get('title'), row.get('content_url_list'), row.get('intro'),
                #       row.get('image_dict'), row.get('keywords'))
                print(datas[::])
                writer.writerow(datas)
            f.close()


if __name__ == "__main__":
    new = New()
    while True:
        new.save_csv(data=new.iter_data())
        time.sleep(10)
