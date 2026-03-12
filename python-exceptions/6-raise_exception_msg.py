#!/usr/bin/python3
def raise_exception_msg(message=""):
    try:
        raise Exception(message)
    except Exception as e:
        print(e)
