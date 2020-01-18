import scrapy 
import pandas as pd
import pickle
import numpy

class IntroSpider(scrapy.Spider): 

    name = 'introduccion_spider' 

    urls = ['http://books.toscrape.com/catalogue/category/books_1/index.html'] 
    

    def start_requests(self): 
        for url in self.urls:
            yield scrapy.Request(url)

   

    def parse(self, response): 
        initial = False
        if(initial == False):
            titulos=[]
            prices_number=[]
            absolute_urls=[]
            initial = True
        etiqueta_contenedora = response.css('article.product_pod') 
        titulos.append(etiqueta_contenedora.css('h3 > a::text').extract())
        absolute_urls2 = []
        urlimg = etiqueta_contenedora.css('a > img::attr(src)').extract()
        for urls in urlimg:
            absolute_urls2.append(response.urljoin(urls))
        absolute_urls.append(absolute_urls2)
        prices = etiqueta_contenedora.css('div.product_price > p.price_color::text').extract()
        prices_number.append(list(map(lambda price: float(price[1:]),prices)))
        general_url = 'http://books.toscrape.com/catalogue/category/books_1/'
        try:
            next_page = response.css('ul.pager > li.next > a::attr(href)').extract()
            next_page_str = general_url + next_page[0]
        except:
            next_page_str = ""
            series_titulos = pd.Series(titulos)
            series_urlimg = pd.Series(absolute_urls)
            series_prices = pd.Series(prices_number)
            df = series_titulos.to_frame(name='Titulo')
            df['URL Images'] = series_urlimg
            df['Prices'] = series_prices
            pickle_file = 'books.pkl'
            with open(pickle_file, 'wb') as fp:
                pickle.dump(df,fp)
                pd_final = pd.read_pickle('books.pkl')
                pd_final.to_excel("books.xlsx")

        if(next_page_str != ""):
            yield scrapy.Request(next_page_str)

