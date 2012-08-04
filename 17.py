num = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 
       6: 'six', 7: 'seven', 8:'eight', 9:'nine', 10:'ten',
       11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
       15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 
       18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty',
       40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy',
       80: 'eighty', 90: 'ninety', 
       100:'hundred', 1000: 'thousand'}

def one_to_twenty(i):
    return num[i]
 
def twenty_one_to_ninety_nine(i):   
    if i % 10 == 0: 
        return num[i]
    else:
        return num[i-i%10] + num[i%10]

def one_to_ninety_nine(i):
    if i < 21:
        return one_to_twenty(i)
    elif i < 100:
        return twenty_one_to_ninety_nine(i)   

def one_hundred_to_one_hundred_and_ninety_nine(i):
    buf = 'one' + num[100]
    if i != 100:
        buf = buf + 'and' + one_to_ninety_nine(i%100)
    return buf

def two_hundreds_to_nine_hundreds_and_ninety_nine(i):
    buf = num[i/100] + num[100]# + 's'
    if i % 100 != 0:
        buf = buf + 'and' + one_to_ninety_nine(i%100)
    return buf

def one_hundred_to_one_thousand(i):
    if i == 1000:
        return 'one' +  num[1000]
    elif i < 200:
        return one_hundred_to_one_hundred_and_ninety_nine(i)
    else:
        return two_hundreds_to_nine_hundreds_and_ninety_nine(i)

def english_num(i):
    if i < 100:
        return one_to_ninety_nine(i)
    else:
        return one_hundred_to_one_thousand(i)

sum_len = 0
for i in range(1,1001):
    sum_len = sum_len + len(english_num(i))
    #print english_num(i), len(english_num(i))

print sum_len
