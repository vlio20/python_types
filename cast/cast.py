import datetime as dt
from typing import cast, Dict


def third_party() -> Dict[str, object]:
    return dict()


data = third_party()
last_import_time: dt.datetime = data['last_import_time']

last_import_time2 = cast(dt.datetime, data['last_import_time'])
