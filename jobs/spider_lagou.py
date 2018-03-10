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

import data
import requests


class Crawl:

    def __init__(self, city, filename, searchername):
        self.city = city
        self.filename = filename
        self.searchername = searchername

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
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
            'Referer': 'https://www.lagou.com/jobs/list_Android?px=default&city={city}'.format(city=city),
            'Origin': 'https://www.lagou.com',
            'Host': 'www.lagou.com',
            'Cookie': 'user_trace_token=20171018150757-11d7072b-b3d3-11e7-9595-5254005c3644; LGUID=20171018150757-11d70ccb-b3d3-11e7-9595-5254005c3644; Hm_lvt_9d483e9e48ba1faa0dfceaf6333de846=1510029000,1510044572,1510069860,1510103314; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=5; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAACBHABBIE7CD5943FF544D0FEE9479A3B6501DD3; TG-TRACK-CODE=index_navigation; _gat=1; _gid=GA1.2.273848703.1512557694; _ga=GA1.2.589815693.1508310478; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1512206891,1512220618,1512557694,1512610017; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1512616430; LGSID=20171207101355-472ffbae-daf4-11e7-9c4b-5254005c3644; LGRID=20171207111349-a54c84d8-dafc-11e7-8804-525400f775ce; SEARCH_ID=3f98f136bc1d4fb98886a9f6fdebfff1'
        }

        url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city={city}&needAddtionalResult=false&isSchoolJob=0'.format(
            city=city)

        response = requests.post(url, data=data, headers=HEADERS)

        return response

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
