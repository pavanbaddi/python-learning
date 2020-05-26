import pytz, datetime

#3)  strptime ignore trailing part of string
# to solve this problem


quit()
# +++

local_time = "26-05-2020 10:39:05 am"
format = "%d-%m-%Y"

try:
    local_datetime_object = datetime.datetime.strptime(local_time, format) 
except Exception as identifier:
    print(identifier)

# Output
# unconverted data remains:  10:39:05 am




# ++++
local_time = "26-05-2020 10:39:05 am"
format = "%d-%m-%Y"

local_datetime_object = datetime.datetime.strptime(local_time, format) #returns ValueError: unconverted data remains:  10:39:05 am




#2) Program to convert datetime of one timezone to another timezone
# 
india_kolkata_timezone = pytz.timezone('Asia/Kolkata')

us_alaska_timezone = pytz.timezone('US/Alaska')

# Local time
local_time = "26-05-2020 10:39:05 am"
format = "%d-%m-%Y %H:%M:%S %p"

local_datetime_object = datetime.datetime.strptime(local_time, format)

# Converted time
us_alaska_converted_datetime_object = local_datetime_object.astimezone(us_alaska_timezone)

print(f"""
Converting datetime string to timezone

Local DateTime : {local_datetime_object}
Us/Alasha DateTime : {us_alaska_converted_datetime_object}

""")

# Output
    # Converting datetime string to timezone

    # Local DateTime : 2020-05-26 10:39:05
    # Us/Alasha DateTime : 2020-05-25 21:09:05-08:00

#1) Program to get datetime by timezones
india_kolkata_timezone = pytz.timezone('Asia/Kolkata')
us_alaska_timezone = pytz.timezone('US/Alaska')
india_time = datetime.datetime.now(india_kolkata_timezone)
us_time = datetime.datetime.now(us_alaska_timezone)

print(f"""
Current Time by on Different Timezones
India/Kolkata : {india_time.strftime("%d-%m-%Y %H:%M:%S %P")}
USA/Alaska : {us_time.strftime("%d-%m-%Y %H:%M:%S %P")}
""")

# pytz.timezone() will return <class 'pytz.tzfile.US/Alaska'>

    # Output
    # Current Time by on Different Timezones
    # India/Kolkata : 26-05-2020 10:24:43 am
    # USA/Alaska : 25-05-2020 20:54:43 pm


# ----------------------------

