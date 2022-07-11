from datetime import datetime
from datetime import timedelta
import pytz
from tzlocal import get_localzone


def sw_datetime_to_utc(sw_datetime: str):
    """
    Convert date and time reported by Southwest to UTC
    :param sw_datetime: Datetime string given by Southwest ('Wed, Aug 17, 2022 7:00AM')
    :return: Datetime object in UTC (Coordinated Universal Time)
    """
    dt = datetime.strptime(sw_datetime, '%a, %b %d, %Y %I:%M%p')
    datetime_utc = dt.replace(tzinfo=get_localzone()).astimezone(pytz.utc) # Make timezone aware and -> UTC
    return datetime_utc


def time_until_checkin(flight_time_utc):
    """
    :param flight_time_utc: Datetime object in UTC
    :return: Timedelta object representing time until check-in (24hr before flight)
    """
    now = datetime.now(tz=pytz.UTC)
    time_until_flight = flight_time_utc - now
    time_until_checkin = time_until_flight - timedelta(hours=24)
    return time_until_checkin


def strfdelta(timedelta, fmt):
    """
    Converts timedelta object to formatted string
    Source: https://stackoverflow.com/questions/8906926/formatting-timedelta-objects
    :param timedelta: Timedelta object
    :param fmt: String specifying output format
    :return: String presenting timedelta object in specified format
    """
    d = {"days": timedelta.days}
    d["hours"], minsec = divmod(timedelta.seconds, 3600)
    d["minutes"], d["seconds"] = divmod(minsec, 60)
    return fmt.format(**d)