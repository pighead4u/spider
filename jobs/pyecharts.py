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

from __future__ import unicode_literals

from data import Job
from pyecharts.charts import pie

count_chengxi = Job.select().where((Job.city == '杭州') & (Job.district == '西湖区') | (Job.district == '余杭区')).count()
count_binjiang = Job.select().where((Job.city == '杭州') & (Job.district == '滨江区') | (Job.district == '萧山区')).count()
count_gongshu = Job.select().where((Job.city == '杭州') & (Job.district == '拱墅区')).count()
count_jianggan = Job.select().where((Job.city == '杭州') & (Job.district == '江干区')).count()
count_shangcheng = Job.select().where((Job.city == '杭州') & (Job.district == '上城区')).count()
count_xiacheng = Job.select().where((Job.city == '杭州') & (Job.district == '下城区')).count()

v1 = [count_chengxi, count_binjiang, count_gongshu, count_jianggan, count_shangcheng, count_xiacheng]
attr = [u'城西', u'滨江', u'拱墅', u'江干', u'上城', u'下城']

pie = pie.Pie("Android岗位数量城区分布")
pie.add("", attr, v1, is_label_show=True)
pie.render()
