# #advanced datatypes 

# #datetime
# from datetime import datetime

# #time
# from datetime import time

# #calendar
# import calendar

# #timedelta -> time difference between two dates or times
# from datetime import datetime, timedelta

# #arrow -> a library that provides a more intuitive way to work with dates and times
# import arrow

# #dateutil -> a library that provides powerful extensions to the standard datetime module
# from dateutil import parser


import arrow

arrow.now()

brewing_time = arrow.utcnow()
brewing_time.to("europe/paris")

#collections
from collections import namedtuple, deque, Counter, defaultdict, OrderedDict

chai_profile = namedtuple("ChaiProfile", ["type", "size", "price", "quantity"])


