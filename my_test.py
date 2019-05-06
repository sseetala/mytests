from __future__ import absolute_import, division, print_function, unicode_literals

import datetime
import functools
import json
import os
import shutil
import tempfile
import time  # NOQA needed for some recordings

from unittest import TestCase

from botocore.exceptions import ClientError
from dateutil.tz import tzutc

import c7n.exceptions

from c7n.exceptions import PolicyValidationError
from c7n.executor import MainThreadExecutor
from c7n.resources import s3
from c7n.mu import LambdaManager
from c7n.ufuncs import s3crypt

from tests.common import BaseTest, functional

class test_record(BaseTest):

    def test_example(self):
    #     session_factory = self.record_flight_data('/Users/rmsc/Desktop/cc/cloud-custodian/test_example')
    #     policy = {
    #         'name': 's3-obj-count',
    #         'resource': 's3'
    #         }
    #
    #     policy = self.load_policy(
    #         policy,
    #         session_factory=session_factory, )
    #     resources = policy.run()

        self.patch(s3.S3, "executor_factory", MainThreadExecutor)
        self.patch(s3, "S3_AUGMENT_TABLE", [])
        session_factory = self.replay_flight_data("/Users/rmsc/Desktop/cc/cloud-custodian/test_example")
        # p = self.load_policy(
        #     {
        #         "name": "s3-obj-count",
        #         "resource": "s3",
        #         "filters": [
        #             {
        #                 "type": "metrics",
        #                 "value": 10000,
        #                 "name": "NumberOfObjects",
        #                 "op": "greater-than",
        #             }
        #         ],
        #     },
        #     session_factory=session_factory,
        # )

        p = self.load_policy(
            {
                "name": "s3-obj-count",
                "resource": "s3"
            },
            session_factory=session_factory,
        )
        resources = p.run()

        assert 1 == 1


#########################
import boto3
session = boto3.session.Session(region_name='us-east-1')
dynamodb = session.resource('dynamodb')
table = dynamodb.Table('mytesttable')

table_exists = False

try:
    table.creation_date_time
    table_exists = True
except:
    table_exists = False

if table_exists:
    print("Table name already exists, please try with a different name")
else:
    new_table = dynamodb.create_table(
        AttributeDefinitions=[
            {
                'AttributeName' : 'partition_key',
                'AttributeType' : 'S',
            },
        ],
        KeySchema=[
            {
                'AttributeName' : 'partition_key',
                'KeyType' : 'HASH',
            },
        ],
        TableName='mytable',
    )



