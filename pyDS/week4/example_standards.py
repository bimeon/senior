import random
import math
import time, calendar
import webbrowser

# random
print(random.random())  # 0~1사이
print(random.randrange(1, 6))   # 1~6 사이 int
food = ['chocolate', 'candy', 'cookie']
print(random.choice(food))

# math
print(math.pi)
print(math.sqrt(16))

# time
print(time.time())
print(time.ctime())

# calendar
print(calendar.weekday(2024, 9, 24)) # 월:0, 화:1, 수:2 ...

# web browser
url = 'https://www.google.com'
webbrowser.open(url)