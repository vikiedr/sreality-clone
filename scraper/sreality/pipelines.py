# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import psycopg2
import os


class SrealityPipeline:
    def __init__(self):
        hostname = 'db'
        username = os.environ.get('POSTGRES_USER')
        password = os.environ.get('POSTGRES_PASSWORD')
        database = os.environ.get('POSTGRES_NAME')
        
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        
        self.cur = self.connection.cursor()
        
    def process_item(self, item, spider):
        self.cur.execute(""" insert into listing_flat (title, img_url) values (%s,%s)""", (
            item["title"],
            item["img_url"]
        ))

        self.connection.commit()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()
