year = int(input('year:'))
month = int(input('month:'))
day = int(input('day:'))
day_sum = 0

months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
if 0 < month <= 12:
    day_sum = months[month - 1]
else:
    print('数据错误。')

day_sum += day
leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = 1
if (leap == 1) and (month > 2):
    day_sum += 1
print(f'共计有 {day_sum} 天。')
