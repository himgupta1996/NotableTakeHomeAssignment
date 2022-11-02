import datetime
def validate_date(date_text):
    try:
        valid_date = datetime.datetime.strptime(date_text, '%Y:%m:%d')
        return True
    except ValueError:
        return False

def validate_time(time_text):
    try:
        validtime = datetime.datetime.strptime(time_text, '%H:%M')
        minute = time_text.split(":")[1]
        print(minute)
        valid_minutes = ['0', '00', '15', '30', '45']
        if minute not in valid_minutes:
            return False
        return True
    except ValueError:
        return False