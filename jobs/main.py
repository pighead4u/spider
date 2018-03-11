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
from spider_lagou import Crawl

cities = [
    "%E5%B9%BF%E5%B7%9E", "%E6%9D%AD%E5%B7%9E", "%E4%B8%8A%E6%B5%B7",
    "%E5%8C%97%E4%BA%AC", "%E6%B7%B1%E5%9C%B3"
]
filenames = ["guangzhou", 'hangzhou', 'shanghai', 'beijing', 'shenzhen']

for (city, filename) in zip(cities, filenames):
    print("{city}--{filename}".format(city=city, filename=filename))
    spider = Crawl(city, filename, "Android")
    spider.getjobdata(50)
