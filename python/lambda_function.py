#!/usr/bin/env python3

import datetime
import json
from get_counter import *
from return_spam_line import *

def lambda_handler(event, context):
    datetime_ = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M")
    counter = get_counter(datetime_)
    if counter == 0:
        create_counter(datetime_)
    spam = return_spam_line(counter)
    increment_counter(datetime_)
    return {
        "statusCode": 200,
        "body": spam
    }
    
if __name__ == '__main__':
    print(lambda_handler("event","context"))
#    datetime_ = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M")
#    counter = get_counter(datetime_)
#    if counter == 0:
#        create_counter(datetime_)
#    print(return_spam_line(counter))
#    increment_counter(datetime_)
