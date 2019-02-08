my_diction = {'FullName':'HASSAN Abdullahi Kolawole', 'reasonForAttendingAISaturday':'I want to be very good in data science and AI'}
print('My name is ' + my_diction['FullName'] + ' and at the end of this cohort, ' + my_diction['reasonForAttendingAISaturday'])
number_series = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
even = 0
odd = 0
for x in number_series:
    if x % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print('Numbers of even numbers: ' + str(even))
print('Numbers of odd numbers: ' + str(odd))
