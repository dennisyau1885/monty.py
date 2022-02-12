#!/usr/bin/env python3

import datetime
from get_counter import *
from return_spam_line import *

if __name__ == '__main__':
    datetime_ = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M")
    counter = get_counter(datetime_)
    if counter == 0:
        create_counter(datetime_)
    print(return_spam_line(counter))
    increment_counter(datetime_)
