# -*- coding: utf-8 -*-


from scrapy import Spider,Request
import psycopg2,json,logging,threading,time
attrs=['id', 'name', 'pcode', 'pname', 'citycode', 'cityname', 'adcode', 'adname', 'biz_type', 'type', 'typecode', 'business_area', 'location', 'address', 'rating', 'cost', 'tag', 'entr_location', 'website', 'tel', 'importance', 'timestamp', 'groupbuy_num', 'shopid', 'poiweight', 'photos', 'postcode', 'exit_location', 'shopinfo', 'children', 'gridcode', 'distance', 'truefloor', 'cpid', 'floor', 'navi_poiid', 'discount_num', 'event', 'indoor_map', 'alias', 'recommend', 'email', 'match']

class GaodeSpider(Spider):
    api_key = '59a8167b169e97d4acda9ad829fbcc23'
    name='GaodeSpider'

    api_url = 'http://restapi.amap.com/v3/place/text?key={0}&keywords={1}&city=武汉&offset=100&page={2}&extensions=all'
    def __init__(self):
        self.conn=psycopg2.connect('dbname=postgres user=postgres host=localhost port=5439')
        cursor=self.conn.cursor()
        cursor.execute('select name from gaode.spois')

        self.names =cursor.fetchall()
        threading._start_new_thread(self.get_count,tuple())
    def get_count(self):
        while True:
            time.sleep(10)
            cursor=self.conn.cursor()
            cursor.execute("select count(id) from poi.gaodepois where citycode = '027'")
            logging.info('crawl {0} pois'.format(cursor.fetchone()[0]))
    def start_requests(self):
        for i in range(self.names.__len__()):
            item=self.names[self.names.__len__()-i-1]
            keyword=item[0]
            if keyword is None:
                continue
            if keyword.__len__()>6:
                keyword=keyword[:6]
            yield Request(self.api_url.format(self.api_key,keyword,1),callback=self.parse,meta={'keyword':keyword,'page':1})

    def parse(self, response):
        res=json.loads(response.body.decode('utf-8'))
        if int(res['infocode']) != 10000:
            logging.info(res)
            return
        for poi in res['pois']:
            for x in poi.items():
                if type(x) is dict:
                    for xx in x.items():
                        x[xx[0]]=xx[1]
                    poi.pop(x)
            item=[]
            for attr in attrs:
                try:
                    if type(poi[attr]) is list:
                        item.append(None)
                    else:
                        item.append(poi[attr])
                except:
                    item.append(None)
            item=tuple(x for x in item)
            self.conn.cursor().execute("insert into poi.GaodePois VALUES ({0}) on CONFLICT do nothing".format(','.join(list('%s' for x in attrs))),item)
            self.conn.commit()
        if res['pois'].__len__() == 50:
            meta=response.meta
            meta['page']+=1
            yield Request(self.api_url.format(self.api_key,meta['keyword'],meta['page']),callback=self.parse,meta=meta)





