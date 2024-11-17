from datetime import date, timedelta

def days_between(date1, date2):
    if date1 > date2:
        return f'{(date1 - date2).days} days'
    else:
        return f'{(date2 - date1).days} days'

def add_days(date1, days):
    return date1 + timedelta(days=days)