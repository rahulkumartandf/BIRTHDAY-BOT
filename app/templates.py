import random

MESSAGES = [

"""🎉 Happy Birthday {name}!

Have a wonderful year ahead.

Best wishes from everyone.
""",

"""🎂 Happy Birthday {name}!

May all your dreams come true.

Have an amazing day.
""",

"""🎈 Wishing you a very Happy Birthday {name}!

Stay healthy and happy.
"""
]


def generate(name):

    return random.choice(MESSAGES).format(name=name)