from datetime import datetime

def get_timestamp():
    return datetime.now().strftime("%d-%m-%Y-%H:%M:%S")

def get_date():
    return datetime.now().strftime("%d-%m-%Y")