import scrapy


class BokeyuanspiderSpider(scrapy.Spider):
    name = 'bokeyuanSpider'
    allowed_domains = ['https://www.cnblogs.com/']
    start_urls = ['https://www.cnblogs.com//']

    def parse(self, response):
        title=response.css(".post-item-title::text").extract()
        name=response.css(".post-item-author span::text").extract()
        url=response.css(".post-item-title::attr(href)").extract()
        time=response.css("span.post-meta-item span::text").extract()
        article_nums=response.css("a.post-meta-item span::text").extract()   # 下面的标签使用的是空格
        thumbsup=[]
        comments=[]
        views=[]
        # 索引除3余数为0的是点赞数
        for i in range(len(article_nums)):
            if(i%3==0):
                thumbsup.append(article_nums[i])
            if(i%3==1):
                comments.append(article_nums[i])
            if(i%3==2):
                views.append(article_nums[i])
        pass
