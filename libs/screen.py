# -*- coding: utf-8 -*-

import codecs

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Screen():
    WAIT_TIMEOUT = 30

    def __init__(self):
        self.driver = None
        self._driver_initialize()

    def after_processing(self):
        self._close()

    def open(self, url):
        self.driver.get(url)

    def wait(self, selector, timeout = WAIT_TIMEOUT):
        locator = self.__create_locator(By.CSS_SELECTOR, selector)
        self.__wait(locator, timeout)

    def get_html(self):
        return self._get_soup().prettify()

    def write_html(self, filepath):
        fw = codecs.open(filepath, 'w', 'utf_8')
        fw.write(self.get_html())
        fw.close()

    def snapshot(self, basename):
        paths = self.get_snapshot_paths(basename)
        self.capture(paths['capture'])
        self.write_html(paths['html'])

    def get_snapshot_paths(self, basename):
        return {
            'capture': basename + '.png',
            'html': basename + '.html',
        }

    def capture(self, filepath):
        self.driver.save_screenshot(filepath)

    def _close(self):
        if self.driver is not None:
            self.driver.close()
        self.driver = None

    def _driver_initialize(self):
        self._close()

        options = Options()
        options.add_argument('--no-sandbox') # need in docker
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')

        # Ignore error
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--allow-running-insecure-content')
        options.add_argument('--disable-web-security')

        # not need function at headless
        options.add_argument('--disable-desktop-notifications')
        options.add_argument("--disable-extensions")

        options.add_argument('--lang=ja')
        # not read images
        options.add_argument('--blink-settings=imagesEnabled=false')

        options.add_argument('--window-size=1280,1024')

        self.driver = webdriver.Chrome(chrome_options=options)

    def _get_soup(self):
        return BeautifulSoup(self.driver.page_source, 'html5lib')

    def __create_locator(self, identity, value):
        return EC.visibility_of_element_located((identity, value))

    def __wait(self, locator, timeout):
        WebDriverWait(self.driver, timeout).until(locator)
