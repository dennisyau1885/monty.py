#!/usr/bin/env python3

import datetime
import get_counter
import return_spam_line

if __name__ == '__main__':
	datetime_ = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M")
	counter = get_counter.get_counter(datetime_)
	if counter == 0:
		get_counter.create_counter(datetime_)
	print(return_spam_line.return_spam_line(counter))
	get_counter.increment_counter(datetime_)