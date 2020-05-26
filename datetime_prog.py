# from datetime import datetime

# string_datetime = "2020-02-26 8:15:45 PM"
# format = "%Y-%m-%d %I:%M:%S %p";
# date_obj = datetime.strptime(string_datetime, format)

# print("Newly created datetime object : \n")
# print(date_obj)
 
# date_object_back_to_string = date_obj.strftime(format)
# print("\nConverted datetime object back to string : {}\n".format(date_object_back_to_string));


# python datetime_prog.py 
# Newly created datetime object : 

# 2020-02-26 20:15:45

# Converted datetime object back to string : 2020-02-26 08:15:45 PM


# *******************************************

# from datetime import datetime

# print("Enter valid date with format (day-month-year) : \n")

# input_date = input()

# date_object = datetime.strptime(input_date,"%d-%m-%Y")
# month = date_object.strftime("%B")

# print("Entered date comes in month is : {}".format(month))

# #
# Enter valid date with format (day-month-year) : 

# 25-03-2020
# Entered date comes in month is : March

# -----------------------------------------------
# PRINT NUMBER OF DAYS IN MONTH
# from datetime import datetime

# print("Enter year in format YYYY : \n")
# input_year = input()
# print("Enter month in number format : \n")
# input_month = input()

# input_date = "{}-{}".format(input_year,input_month);
# format = "%Y-%m"
# start_date_obj = datetime.strptime(input_date, format)

# if int(input_month) < 12:
#     input_month = str(int(input_month)+1)
# else: 
#     input_month = "1"
#     input_year = int(input_year)+1

# next_input_date = "{}-{}".format(input_year, input_month)
# next_date_obj = datetime.strptime(next_input_date, format)

# difference_in_days = (next_date_obj-start_date_obj).days

# print("\n***************Output**********************\n")
# print("\nYour entered year and month is : {}".format(start_date_obj))
# print("\nNext month  : {}".format(next_date_obj))
# print("\nDifference in days are : {}".format(difference_in_days))


# $ python3.8 datetime_prog.py 
# Enter year in format YYYY : 

# 2020
# Enter month in number format : 

# 1

# ***************Output**********************


# Your entered year and month is : 2020-01-01 00:00:00

# Next month  : 2020-02-01 00:00:00

# Difference in days are : 31

# --------------------------------------------------------------

# $ python3.8 datetime_prog.py 
# Enter year in format YYYY : 

# 2020
# Enter month in number format : 

# 2

# ***************Output**********************


# Your entered year and month is : 2020-02-01 00:00:00

# Next month  : 2020-03-01 00:00:00

# Difference in days are : 29

# from datetime import datetime

# print("Enter month in number format : \n")
# input_month = input()
# format = "%m"
# start_date_obj = datetime.strptime(input_month, format)

# if int(input_month) < 12:
#     next_month = int(input_month)+1
# else:
#     next_month = "1"

# next_month_date_obj = datetime.strptime(str(next_month), format)

# print("\n***************Output**********************")
# print("\nYour entered month is : {}".format(start_date_obj.strftime("%B")))
# print("\nUpcomming mext month is  : {}".format(next_month_date_obj.strftime("%B")))


# #PYTHON OUTPUT 1
# $ python3.8 datetime_prog.py 
# Enter month in number format : 

# 03

# ***************Output**********************

# Your entered month is : March

# Upcomming mext month is  : April


# #PYTHON OUTPUT 2

# $ python3.8 datetime_prog.py 
# Enter month in number format : 

# 12

# ***************Output**********************

# Your entered month is : December

# Upcomming mext month is  : January




