# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PoiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    website = scrapy.Field()
    tel = scrapy.Field()
    typecode = scrapy.Field()
    importance = scrapy.Field()
    timestamp = scrapy.Field()
    groupbuy_num = scrapy.Field()
    entr_location = scrapy.Field()
    cityname = scrapy.Field()
    shopid = scrapy.Field()
    poiweight = scrapy.Field()
    photos = scrapy.Field()
    tag = scrapy.Field()
    pname = scrapy.Field()
    postcode = scrapy.Field()
    exit_location = scrapy.Field()
    address = scrapy.Field()
    rating = scrapy.Field()
    cost = scrapy.Field()
    business_area = scrapy.Field()
    shopinfo = scrapy.Field()
    children = scrapy.Field()
    gridcode = scrapy.Field()
    distance = scrapy.Field()
    citycode = scrapy.Field()
    truefloor = scrapy.Field()
    cpid = scrapy.Field()
    floor = scrapy.Field()
    navi_poiid = scrapy.Field()
    name = scrapy.Field()
    discount_num = scrapy.Field()
    adcode = scrapy.Field()
    pcode = scrapy.Field()
    id = scrapy.Field()
    event = scrapy.Field()
    indoor_map = scrapy.Field()
    alias = scrapy.Field()
    biz_type = scrapy.Field()
    adname = scrapy.Field()
    location = scrapy.Field()
    recommend = scrapy.Field()
    type = scrapy.Field()
    email = scrapy.Field()
    match = scrapy.Field()

    pass
