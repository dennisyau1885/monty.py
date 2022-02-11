#!/usr/bin/env python3

import sys

def return_spam_line(line: int) -> str:
    spam_menu = [
    'Egg and Spam',
    'Egg, bacon and Spam',
    'Egg, bacon, sausage and Spam',
    'Spam, bacon, sausage and Spam',
    'Spam, egg, Spam, Spam, bacon and Spam',
    'Spam, Spam, Spam, egg and Spam',
    'Spam, Spam, Spam, Spam, Spam, Spam, baked beans, Spam, Spam, Spam and Spam',
    'Lobster Thermidor aux crevettes with a Mornay sauce, garnished with truffle pâté, brandy and a fried egg on top, and Spam'
    ]
    if line < len(spam_menu):
        return spam_menu[line % len(spam_menu)]
    else: # print x number of Spams
        return ", ".join(list(["Spam"]*(line-1))) + " and Spam"
if __name__ == '__main__':
    # TODO: handle non-numeric and empty args
    print(return_spam_line(int(sys.argv[1])))