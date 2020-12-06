import calendar
import datetime
# importing datetime and calender module

def getLastThursday(input_month):
    month = int(input_month[5:7]) #to access month for eample if date is '2020-12-1' then 2 is at 0'th position 0 is at 1'th position and so on
    year = int(input_month[0:4])
    thursday_number = -1
    cal = calendar.Calendar(firstweekday=calendar.MONDAY)
    monthcal = cal.monthdatescalendar(year, month)
    selected_thursday = [day for week in monthcal for day in week if \
                         day.weekday() == calendar.THURSDAY and \
                         day.month == month][thursday_number]
    return selected_thursday


def isLastThursday(input_date):
    date = int(input_date[8:10])
    month = int(input_date[5:7])
    year = int(input_date[0:4])
    born = datetime.date(year, month, date)
    if (born.strftime("%A") == 'Thursday'):
        return True
    else:
        return getLastThursday(input_date)


str = input('date (in format yyyy-mm-dd)')  # input date in string format

t = isLastThursday(str)  #calling function to check if inputed date is last thursday
if t == True:
    print('yes, {} is the last Thursday of {} month in {}'.format(str[8:10], str[5:7], str[0:4]))

else:
    print('{} is not a Last Thursday. it''s last thursday is on {}'.format(str[8:10], t))
