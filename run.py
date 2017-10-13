# -*- coding: utf-8 -*-

from datetime import datetime
from libs.screen import Screen
from libs.result import Result

url = 'https://www.google.co.jp/'

screen = Screen()

screen.open(url)
screen.wait('body')

screen.snapshot('google') # Save capture and HTML

# Sample of store to database
record = {}
record['url'] = url
record['html'] = screen.get_html()
record['scraped_at'] = datetime.now()

result = Result()
result.save(record)
