# -*- coding: utf-8 -*-

import pymysql
import sqlsoup

class Store:
    PREFIX = 'mysql+pymysql'
    CHARSET = 'charset=utf8mb4'
    HOST = 'scraping-db'
    PORT = '3306'
    DB_NAME = 'scraped'
    USER = 'root'
    PASSWD = 'password'

    def __init__(self):
        self.db = sqlsoup.SQLSoup(self._make_db_url())

    def get_db(self):
        return self.db

    # protected method
    def _make_db_url(self):
        url = '{0}://{1}:{2}@{3}:{4}/{5}?{6}'.format(
                self.PREFIX,
                self.USER,
                self.PASSWD,
                self.HOST,
                self.PORT,
                self.DB_NAME,
                self.CHARSET)

        return url
