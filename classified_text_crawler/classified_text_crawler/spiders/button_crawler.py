import os.path
import scrapy

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def filter_valid_texts(texts):
    result = []
    for text in texts:
        stripped_text = text.strip()
        if stripped_text:
            result.append(stripped_text)
    return result


def allowed_domains():
    with open(os.path.join(__location__, '../ALLOWLIST')) as allowlist:
        domains = filter_valid_texts(allowlist.readlines())
    return domains


class ButtonCrawler(scrapy.Spider):
    name = 'button_crawler'
    start_urls = allowed_domains()

    def parse(self, response):
        button_texts = response.xpath('//button/text()').getall()
        if len(button_texts):
            yield {
                "texts": filter_valid_texts(button_texts)
            }

        for next_page in response.css('a'):
            yield response.follow(next_page, self.parse)
