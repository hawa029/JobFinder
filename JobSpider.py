import scrapy

class JobSpider(scrapy.Spider):
    name = 'Jobspider'
    start_urls = ['https://www.apec.fr/candidat/recherche-emploi.html/emploi?lieux=21&typesContrat=20053']

    def parse(self, response):
        for title in response.css('.card-title'):
            yield {'title': title.css('::text').get()}