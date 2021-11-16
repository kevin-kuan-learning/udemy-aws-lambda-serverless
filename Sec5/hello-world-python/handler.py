import json
import time

def hello(event, context):
    print("hello")
    time.sleep(3)
    return "hello world - Updated!"
