months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
year = 1900
day = 0 # Mon, 1, Jan, 1900
count = 0

for year in range(1900, 2001):
    #i = 1
    for month in months:
        #i = i + 1
        if month == 28 and year % 4 == 0:
            if year % 100 != 0 or year % 400 == 0:
                month = month + 1
        day = (day + month) % 7
        if year != 1900 and day == 6:
            #print year, i
            count = count + 1

print count
