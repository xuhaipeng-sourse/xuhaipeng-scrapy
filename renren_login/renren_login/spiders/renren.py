# -*- coding: utf-8 -*-
import scrapy
import time


class RenrenSpider(scrapy.Spider):
    name = "renren"
    # allowed_domains = ["'renren.com'"]
    start_urls = ['http://www.renren.com/']
    url = 'http://www.renren.com/'


    def start_requests(self):
        #构造时间戳
        base_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp='
        s = time.strftime("%S")
        ms = int(round(time.time() % (int(time.time())), 3) * 1000)
        date_time = '2020414' + str(s) + str(ms)
        login_url = base_url + date_time
        data = {'email': '1780592702@qq.com',
                'icode': '',
                'origURL': 'http://www.renren.com/home',
                'domain': 'renren.com',
                'key_id': '1',  ####注意这里面一定是字符型1，整型1会报错。如果使用
                'captcha_type': 'web_login',
                'password': '77e58d855bccbb2556f90f3c2bcf7fe9bcc504802f9b926072ba2f9904c05d27',
                'rkey': '3907379e90e99c8cab502ca083179e25',
                'f': 'http%3A%2F%2Fwww.renren.com%2F974183878',
                }
        yield scrapy.FormRequest(url=login_url, formdata=data, callback=self.parse_login, dont_filter=True)


    def parse_login(self, response):
        yield scrapy.Request(url='http://www.renren.com/880151247/profile', callback=self.parse_text, dont_filter=True)


    def parse_text(self, response):
        with open(r'renren.html', 'w', encoding='utf-8') as f:
            f.write(response.text)
