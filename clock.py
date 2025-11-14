from datetime import datetime
import pytz

def get_current_time():
    utc_now = datetime.now(pytz.UTC)
    toronto_tz = pytz.timezone('America/Toronto')
    local_now = utc_now.astimezone(toronto_tz)
    
    return {
        "utc": utc_now.isoformat(),
        "local": local_now.isoformat(),
        "unix": int(utc_now.timestamp()),
        "readable": local_now.strftime("%A, %B %d, %Y at %I:%M:%S %p %Z")
    }