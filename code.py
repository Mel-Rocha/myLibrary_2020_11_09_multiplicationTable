print(30*'=')
print('     multiplication table')
print(30*'=')
print('')

number = int(input('Type the number you want to see the multiplication tab le: '))
counter  = 0 

while counter <= 10:
  x = range(11)
  for n in x:
    result = number * n
    print('{} X {} = {}'.format(n, number, result ))
    counter += 1
