#!/usr/bin/env python3

import boto3
import datetime
import decimal  
import json
import sys
import time
from botocore.exceptions import ClientError

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
	def default(self, o):
		if isinstance(o, decimal.Decimal):
			if o % 1 > 0:
				return float(o)
			else:
				return int(o)
		return super(DecimalEncoder, self).default(o)

def get_counter(datetime_: str) -> int:
	db = boto3.resource('dynamodb')
	table = db.Table('monty_py')

	try:
		response = table.get_item(
			Key= {
 				'hash': 'spam',
				'datetime': datetime_
			}
		)
	except ClientError as e:
		return 0
	else:
		if 'Item' in response:
			return int(json.dumps(response['Item']['count'], cls=DecimalEncoder))
		else:
			return 0 

def create_counter(datetime_: str):
	db = boto3.resource('dynamodb')
	table = db.Table('monty_py')

	item = {
		'datetime': datetime_,
		'hash': 'spam',
		'count': 0,
		'ttl': int(time.time())+60*60*24*90
	}
	table.put_item(Item=item)

def increment_counter(datetime_: str):
	db = boto3.resource('dynamodb')
	table = db.Table('monty_py')

	response = table.update_item(
		Key={
			'datetime': datetime_,
			'hash': "spam"
		},
		UpdateExpression="SET #s = #s + :v",
		ExpressionAttributeNames={
			"#s": "count"
		},
		ExpressionAttributeValues={
			":v": decimal.Decimal(1)
		},
		ReturnValues="UPDATED_NEW"
	)

if __name__ == '__main__':
	if len(sys.argv) != 0:
		datetime_ = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M")
	else:
		datetime_ = sys.argv[1]
	counter = get_counter(datetime_)
	if counter == 0:
		create_counter(datetime_)
	print(counter)
	increment_counter(datetime_)