import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from yangguangPro.items import YangguangproItem,YangguangproTail
class YangSpider(CrawlSpider):
    name = 'yang'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['http://wz.sun0769.com/political/index/politicsNewest?id=1&page=1']
    #正则解析  http://wz.sun0769.com/political/politics/index?id=493588
    link = LinkExtractor(allow=r'id=1&page=\d+')
    link_tail = LinkExtractor(allow=r'/index\?id=\d+')
    #http://wz.sun0769.com/political/index/politicsNewest?id=1&page=1
    rules = (
        Rule(link, callback='parse_item', follow=True),
        Rule(link_tail, callback='parse_tail'),
    )

    def parse_item(self, response):
        tr_list = response.xpath('/html/body/div[2]/div[3]/ul[2]/li')
        for li in tr_list:
            id_num = li.xpath('./span/text()').extract_first()
            title = li.xpath('./span/a/text()').extract_first()
            item = YangguangproItem()
            item['id_num'] = id_num
            item['title'] = title
            yield item
    def parse_tail(self,response):
        num_id = response.xpath('/html/body/div[3]/div[2]/div[2]/div[1]/span[4]/text()').extract_first()
        content = response.xpath('/html/body/div[3]/div[2]/div[2]/div[2]/pre//text()').extract()
        content = ''.join(content)
        item = YangguangproTail()
        item['num_id'] = num_id
        item['content'] = content
        yield item


