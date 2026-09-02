#student percentage
perc=float(input('Enter percentage : '))
if perc>=75:
  print('passed in distinction')
elif perc>=60 and perc<75:
  print('passed in first class')
elif perc>=35 and perc<60:
  print('student passed')
else:
  print('student failed to clear the exam')