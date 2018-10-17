# -*- coding: UTF-8 -*-
#输出日历
def print_calendar(year,month,date = 1):
    month_dict = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July',
                  '8':'August','9':'September','10':'October','11':'November','12':'December'}
    
    #数字月份转换为字符串,并判断月份和号数是否合法
    if month in range(1,13) and date in range(1,31):
        month_str = str(month)
        if month_str in month_dict:
            month_str = month_dict[month_str]
    else:
        print('月份或号数输入不合法')
        return -1
    
    #头部
    print('%15s%8d'%(month_str,year))
    print('-'*33)
    print('Sun  Mon  Tue  Wed  Thu  Fri  Sat')
    
    #得到每月1号是星期几
    first_day = get_start_day(year,month,1)
    #得到此月有多少天
    month_num = days_of_month(year,month)

    each_day = 0
    #主体
    for index in range(1,43):
    
        if index < first_day + 1:
            print(' '*5,end = '')
        else:
            if (index - 1) % 7 == 0:
                print('')
            each_day += 1
            if each_day > month_num:
                return False
            if each_day < 10:
                if each_day == date:
                    print('%-5s'%('--'),end = '')
                else:
                    print(' %-4d'%(each_day),end = '')
            else:
                if each_day == date:
                    print('%-5s'%('--'),end = '')
                else:
                    print('%-5d'%(each_day),end = '')
                
              
#输入一个年月日，判断是星期几
#需要一个比较标准：2010-1-1是星期五
#计算当前距离标准过了多少天(total_days % 7  + 5 -1)%7
#先遍历年份，是闰年+366，不是+365
#再遍历月份，31,30,29,28
def get_start_day(year,month,date):
    total_days = 0
    #遍历年份
    for one_year in range(2010,year):
        if is_leap_year(one_year):
            total_days += 366
        else:
            total_days += 365
    #print(total_days)
    #遍历月份
    for one_month in range(1,month):
        total_days += days_of_month(year,one_month)
    #print(total_days)
    #加上当月号数,则求得总共过了多少天
    total_days += date

    #求输入的年月日是星期几
    day = (total_days % 7 + 5 - 1) % 7
    
    #print(total_days)
    #print(day)
    return day

#输入一个年份和月份，输出这月有多少天
#1,3,5,7,8,10,12--------31天
#4,6,9,11 --------------30天
#如果是闰年2------------29天
#不是闰年 2-------------28天
def days_of_month(year,month):
    days = 0
    if month in (1,3,5,7,8,10,12):
        days = 31
    elif month in (4,6,9,11):
        days = 30
    elif is_leap_year(year):
        days = 29
    else:
        days = 28
    return days

def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False

def main():
    print('*'*33)
    year = int(input('Please input year:'))
    month = int(input('Please input month:'))
    date = int(input('Please input day:'))
    print('*'*33)
    #某年某月有多少天
    #days = days_of_month(year,month)
    #print('{}年{}月有{}天'.format(year,month,days))
    #某年某月某日是星期几
    #day = get_start_day(year,month,date)
    #print('{}年{}月{}日是星期{}'.format(year,month,date,day))
    #打印日历
    print_calendar(year,month,date)
    
#执行
main()