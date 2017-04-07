american = "05.17.2016"
point = american.find('.')
mounth = american[:point + 1 ]
point2 = american.find('.', point + 1 ) 
day = american[point + 1 : point2 + 1 ]
year = american[ point2 + 1 : ]
europe = day + mounth + year
print(europe)

first = 'aaaaaa'
second = 'bbbbbb'
inp = second [:int(len(second)/2)] + first + second[int(len(second)/2):]
result = first[:int(len(first)/2)] + inp + first[int(len(first)/2):]
print(result)

string = 'aaa bbb ccc ddd'
capt = string.find(' ')
capt2 = string.find(' ', capt +  capt+1)
strint2 =  string[:capt] + string[capt:capt2].upper() + string[capt2:]
print(strint2)

import math
leo = 'Leo Tolstoy*1828-08-28*1910-11-20'
fn = leo.find('*')
sp =  leo.find('-')
birthday = leo[fn+1:sp]
fn1 = leo.find("*", fn + fn)
sp1= leo.find("-", fn1 )
death = leo[fn1+1:sp1]
age =  int(death) - int(birthday)
final = leo[:fn] + ', ' + str(age)
print(final)


































