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

from peewee import CharField, Model, SqliteDatabase

db = SqliteDatabase('jobs.db')


class Job(Model):
    searchName = CharField()
    positionName = CharField()
    salary = CharField()
    workYear = CharField()
    education = CharField()
    jobNature = CharField()
    city = CharField()
    companyShortName = CharField()
    district = CharField(null=True)
    positionLables = CharField(null=True)
    secondType = CharField()
    companyFullName = CharField(null=True)

    class Meta:
        database = db  # This model uses the "jobs.db" database.
