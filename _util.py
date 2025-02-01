import datetime
import time
import hashlib

def _print(txt="HERE", last_time=time.time()):
    this_time = time.time()
    print("{}\t{}\t{}".format(datetime.datetime.now(),
                              this_time-last_time,
                              txt)
         )
    return time.time()


def generate_unique_id(string):
    return hashlib.md5(string.encode()).hexdigest()
