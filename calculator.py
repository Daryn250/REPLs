# calculator
valid_signs=['+','-','*','/']
while True:
  try:
    x = int(input("Provide a number: "))
    break
  except:
    print("Not a Valid Number")
while True:
  try:
    sign = input("Provide a sign: ")
    if sign in valid_signs:
      break
    else:
      print("Not in valid signs")
  except:
    print("Not in valid signs")
while True:
  try:
    y = int(input("Provide a second number: "))
    break
  except:
    print("Not a Valid Number")
if sign=='+':
  print(x+y)
elif sign=='-':
  print(x-y)
elif sign=='*':
  print(x*y)
elif sign=='/':
  try:
    print(x/y)
  except:
    print("Error: Cannot Divide By Zero")
