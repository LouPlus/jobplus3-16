import scrapy

class JobsSpdier(scrapy.Spider):
	name = 'jobs'
	start_urls = ['https://www.lagou.com/']

	def parse(self, response):
		for job in response.css('li.position_list_item'):
			yield {
			    'name':job.xpath('.//@data-positionname').extract_first(),
			    'company':job.xpath('.//@data-company').extract_first(),
			    'salary': job.xpath('.//@data-salary').extract_first(),
                'experience': job.css('div.position_main_info span::text').extract_first(),
                'create_date': job.css('span.create-time::text').re_first('\u2002(.+)\u2002')
			}