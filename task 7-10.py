american_date = "05.17.2016"
point_idx = american_date.find('.')
mounth = american_date[:point_idx + 1 ]
point2 = american_date.find('.', point_idx + 1 )
day = american_date[point_idx + 1 : point2 + 1 ]
year = american_date[ point2 + 1 : ]
europe_date = day + mounth + year
print(europe_date)

first = 'aaaaaa'
second = 'bbbbbb'
inp = second [:int(len(second)/2)] + first + second[int(len(second)/2):]
result = first[:int(len(first)/2)] + inp + first[int(len(first)/2):]
print(result)

string = 'aaaaa bb xx ccc ddd'
capt = string.find(' ')
capt2 = string.find(' ', capt +1)
strint2 =  string[:capt] + string[capt:capt2].upper() + string[capt2:]
print(strint2)

import math
leo = 'Leo Tolstoy*1828-08-28*1910-11-20'
find_idx = leo.find('*')
space_ind =  leo.find('-')
birthday = leo[find_idx+1:space_ind]
find_idx1 = leo.find("*", find_idx + 1)
space_ind1= leo.find("-", find_idx1 )
death = leo[find_idx1+1:space_ind1]
age =  int(death) - int(birthday)
final = leo[:find_idx] + ', ' + str(age)
print(final)


































