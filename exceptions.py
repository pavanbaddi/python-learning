import sys, os
import traceback

try:
    # a = 2/0
    a=b
except Exception as e:
    print("------")
    # print(dir(e))
    # print(e.args) #
    # print(e.__doc__) #displays message
    # print(e.message) # displays traceback

    # exc_type, exc_obj, exc_tb = sys.exc_info()
    # fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    # print(exc_type, fname, exc_tb.tb_lineno)

    print(traceback.format_exc()) # this returns traceback and also does not stop excution

print("hello")