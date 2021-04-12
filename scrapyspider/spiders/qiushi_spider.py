from scrapy.spiders import Spider
import scrapy

# 糗事百科爬虫
class QiuShiSpider(Spider):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/73.0.3683.86 Chrome/73.0.3683.86 Safari/537.36'
    }
    name = 'qiushibaike'
    start_urls = ['http://woodenrobot.me']

    def parse(self, response):
        content_left_div = response.xpath("//div[starts-with(@id,'qiushi_tag_')]")
        for content_div in content_left_div:
            yield {
                'author': content_div.xpath('./div/a[2]/h2/text()').get(),
                'content': content_div.xpath('./a/div/span/text()').getall(),
            }

    def start_requests(self):
        urls = [
            'https://www.qiushibaike.com/text/page/1/',
            'https://www.qiushibaike.com/text/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers=self.headers)
