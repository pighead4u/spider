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

import matplotlib.pyplot as plt
from data import Job
from matplotlib import font_manager

count_chengxi = Job.select().where((Job.city == '杭州') & (Job.district == '西湖区') | (Job.district == '余杭区')).count()
count_binjiang = Job.select().where((Job.city == '杭州') & (Job.district == '滨江区') | (Job.district == '萧山区')).count()
count_gongshu = Job.select().where((Job.city == '杭州') & (Job.district == '拱墅区')).count()
count_jianggan = Job.select().where((Job.city == '杭州') & (Job.district == '江干区')).count()
count_shangcheng = Job.select().where((Job.city == '杭州') & (Job.district == '上城区')).count()
count_xiacheng = Job.select().where((Job.city == '杭州') & (Job.district == '下城区')).count()

slices = [count_chengxi, count_binjiang, count_gongshu, count_jianggan, count_shangcheng, count_xiacheng]
activities = [u'城西', u'滨江', u'拱墅', u'江干', u'上城', u'下城']
cols = ['c', 'm', 'r', 'b', 'y', 'g']

chinese_font = font_manager.FontProperties(fname='/System/Library/Fonts/PingFang.ttc')

p = plt.pie(slices,
            labels=activities,
            colors=cols,
            startangle=90,
            shadow=False,
            explode=(0, 0.1, 0, 0, 0, 0),
            autopct='%1.1f%%')

plt.title(u'Android岗位数量城区分布', fontproperties=chinese_font)
plt.legend(prop=chinese_font)

for front in p[1]:
    front.set_fontproperties(font_manager.FontProperties(
        fname='/System/Library/Fonts/PingFang.ttc'))

plt.show()
