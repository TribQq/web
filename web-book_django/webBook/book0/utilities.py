from datetime import datetime
from os.path import splitext


def get_timestamp_path(instance, filename, used_in = 'cover_img_'):
    return '%s%s%s' %(used_in, datetime.now().timestamp(), splitext(filename)[1])