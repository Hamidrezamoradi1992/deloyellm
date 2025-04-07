from datetime import datetime, timezone, timedelta


def get_timezone():
    now_utc = datetime.now(timezone.utc)
    time = now_utc.astimezone(timezone(timedelta(hours=3, minutes=30)))
    return time
