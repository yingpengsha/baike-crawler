# -*- coding: utf-8 -*-
# Author: yingpengsha
# Time  : 2019/2/4 19:03
import urllib2


class HtmlDownload(object):
    def download(self, url):
        if url is None:
            return None

        response = urllib2.urlopen(url)

        if response.getcode() != 200:
            return None

        return response.read()
