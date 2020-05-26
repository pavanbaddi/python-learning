import pytz, datetime
print("hello")
# print(dir(pytz.country_timezones));
# pytz.country_timezones['de']

# matching_tzs = [t for t in pytz.country_timezones['de'] if pytz.timezone(t)._utcoffset.total_seconds() == 3600]