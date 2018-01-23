#from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
import time
from boto3.dynamodb.conditions import Key, Attr
import base64
import ast

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb')
context=0
event=0
table = dynamodb.Table('hashtags')

print("Popular Hashtags")

response = table.scan()

def gun(response):
    x=[]
    for i in response['Items']:
        d = ast.literal_eval((json.dumps(i, cls=DecimalEncoder)))
        f=d["htCount"]
        x.append(d)
        x.sort(cmp=lambda r,y: cmp(r["htCount"], y["htCount"]), reverse=True)
    return x
    
def lambda_handler(event, context):
    response = table.scan()
    event = gun(response)
    return event
lambda_handler(event,context)