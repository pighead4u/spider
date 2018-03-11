# -*- coding: utf-8 -*-
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import time

import requests
from fake_useragent import UserAgent

import data
import settings


class Crawl(object):
    def __init__(self, city, filename, searchername):
        self.city = city
        self.filename = filename
        self.searchername = searchername
        self.ua = UserAgent()

    def getjobdata(self, pagesize):

        for pn in [x + 1 for x in range(pagesize)]:
            data = self._build_request_data(pn)
            response = self._get_http_data(self.city, data)
            is_stop = self._write_data_2db(response)
            time.sleep(2)

            if is_stop:
                break

    def _build_request_data(self, pagenumb):
        if pagenumb == 1:
            is_first = 'true'
        else:
            is_first = 'false'

        data = {
            'first': is_first,
            'pn': str(pagenumb),
            'kd': self.searchername,
        }
        return data

    def _get_http_data(self, city, data):
        HEADERS = {
            'User-Agent': self.ua.google,
            'Referer':
            ('https://www.lagou.com/jobs/list_Android?px=default&city=' +
             city),
            'Origin': 'https://www.lagou.com',
            'Host': 'www.lagou.com',
            'Cookie': settings.cookie
        }  # yapf: disable

        url = ('https://www.lagou.com/jobs/positionAjax.json?px=default&city='
               + city + '&needAddtionalResult=false&isSchoolJob=0')

        return requests.post(url, data=data, headers=HEADERS)

    def _write_data_2db(self, response):
        result = response.json()
        if result.get('content').get('pageNo') == 0:
            return True
        jobs = result.get('content').get('positionResult').get('result')

        for job in jobs:
            job_db = data.Job()
            job_db.searchName = self.searchername
            job_db.positionName = job['positionName']
            job_db.salary = job['salary']
            job_db.workYear = job['workYear']
            job_db.education = job['education']
            job_db.jobNature = job['jobNature']
            job_db.city = job['city']
            job_db.companyShortName = job['companyShortName']
            job_db.district = job['district']
            job_db.positionLables = job['positionLables']
            job_db.secondType = job['secondType']
            job_db.companyFullName = job['companyFullName']

            job_db.save()

        return False
