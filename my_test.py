
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
        ProvisionedThroughput={
            'ReadCapacityUnits': '5',
            'WriteCapacityUnits': '5',
        },
        TableName='mytable',
    )



