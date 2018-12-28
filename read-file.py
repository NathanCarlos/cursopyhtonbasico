from datetime import datetime as dt
import unicodecsv

with open('enrollments.csv', 'rb') as f:
    reader = unicodecsv.DictReader(f)
    enrollments = list(reader)
# Takes a date as a string, and returns a Python datetime object. 
# If there is no date given, returns None
def parse_date(date):
    if date == '':
        return None
    else:
        return dt.strptime(date, '%Y-%m-%d')
    
# Takes a string which is either an empty string or represents an integer,
# and returns an int or None.
def parse_maybe_int(i):
    if i == '':
        return None
    else:
        return int(i)

calc_date = 0
calc_media = 0
calc_canceled = 0
calc_notCanceled = 0
calc_total = 0
# Clean up the data types in the enrollments table
for enrollment in enrollments:
    enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])
    enrollment['days_to_cancel'] = parse_maybe_int(enrollment['days_to_cancel'])
    enrollment['is_canceled'] = enrollment['is_canceled'] == 'True'
    enrollment['is_udacity'] = enrollment['is_udacity'] == 'True'
    enrollment['join_date'] = parse_date(enrollment['join_date'])
    if not enrollment['days_to_cancel'] is None:
        calc_date += enrollment['days_to_cancel']
        calc_media += 1
    if enrollment['is_canceled'] == True:
        calc_canceled += 1
    if enrollment['is_canceled'] == False:
        calc_notCanceled += 1
    if enrollment['is_canceled'] == True or enrollment['is_canceled'] == False:
        calc_total += 1
# print(calc_date / calc_media)
porcentagem_canceled = (float(calc_canceled) / float(calc_total)) * 100
print(porcentagem_canceled)
porcentagem_not_canceled = (float(calc_notCanceled) / float(calc_total)) * 100
print(porcentagem_not_canceled)
print(calc_total)