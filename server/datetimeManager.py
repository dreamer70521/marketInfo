# -*- coding: utf-8 -*-

import time
from datetime import datetime

class datetimeManager:

    def __init__(self):
        super().__init__()

    def getDateTimeString(self):
        ts = time.time()
        timeFormat = '%Y/%m/%d %H:%M:%S'
        timeString = time.strftime(timeFormat, time.localtime(ts))
        return timeString
    
    def getDurationString(self, start_ts, end_ts):
        duration = str(round(end_ts - start_ts, 4))
        return duration
