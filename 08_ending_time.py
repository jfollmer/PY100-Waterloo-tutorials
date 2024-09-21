# Waterloo tutorials, 8. Remix, "Ending Time" exercise
# https://cscircles.cemc.uwaterloo.ca/8-remix/

"""This program takes two lines of input. The first line is a "starting 
time" expressed in a 24-hour clock with leading zeroes, like 08:30 or 
14:07. The second line is a duration D in minutes. Print out what time 
it will be D minutes after the starting time. For example, for input
    12:30
    47
the correct output would be 13:17. All times should be formatted as 
numbers between 00:00 and 23:59, but the time period may go over 
midnight. For example, on input
    23:59
    13
the correct output is 00:12.
"""

# I redid this and added it here after completing PY101. Not sure what
# solution I came up with the first time through. I tried to solve it
# without using techniques I didn't know about then.

inputs = {
    '12:30': '47',   # 13:17
    '23:59': '70',    # 00:06 # this line is printing what the 7th line should be printing?
    '08:30': '185',  # 11:35
    '15:52': '976',  # 08:08
    '03:43': '471',  # 11:34
    '10:10': '52',   # 11:02
    '23:59': '70',   # 01:09 # this line is being skipped?
    '23:50': '1800', # 05:50
}

# start_time = input() # replaced with the inputs dictionary and iterating over it
# duration = int(input())
for start_time, duration in inputs.items():
    print(start_time, duration) # debug
    """inputs.items() is skipping the 2nd item and reording the 7th item 
    to the 2nd item somehow, but it works otherwise. Not sure what's
    happening."""
    duration = int(duration)
    # the solution I used on the website:
    hour = int(start_time[0:2])
    minute = int(start_time[3:len(start_time)])

    end_minute = str((minute + duration) % 60)
    hours_later = (minute + duration) // 60
    end_hour = hour + hours_later

    while end_hour > 23:
        end_hour -= 24
    end_hour = str(end_hour)

    if len(end_hour) < 2:
        end_hour = '0' + end_hour
    if len(end_minute) < 2:
        end_minute = '0' + end_minute
    print(start_time, duration) # debug
    print(end_hour + ':' + end_minute)