#Question 6 to perform mapping on the website
#Question 6i
import scrapy
class newSpider(scrapy.Spider):
    name = "new spider"
    start_urls = ['http://172.17.50.43/creative']
#using scrapy web-crawler with appropriate parser "response.css"
    def parse(self, response):
        css_sel = 'img'
        for x in response.css(css_sel):
            xpath_sel = "@src"
            css_sel2 = "::attr(src)"
#6ii and iii where you can see the list of JPG image links extracted on webpage using JSON command using scrapy runspider Mapping.py -o results.json -t json
            yield {
                'IMAGE link': x.xpath(xpath_sel).extract_first(),
            }
            nextcss_sel = '.next a::attr(href)'
            next_page = response.css(nextcss_sel).extract_first()
            if next_page:
                yield scrapy.Request(response.urljoin(next_page),callback=self.parse)