from os.path import splitext
from datetime import datetime


def get_timestamp_path(instance,filename):
    return 'bs_%s%s' % (datetime.now().timestamp(), splitext(filename)[1])
