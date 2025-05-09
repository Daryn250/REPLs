import random
winc=0
losec=0
tiec=0
auto=False
runs=5000000
total=0
set=None
while runs>0:
  valid = ['rock', 'paper', 'scissors']
  if auto:
    if set==None:
      r = random.randint(1,3)
      if r == 1:
        a = valid[0]
      if r == 2:
        a = valid[1]
      if r == 3:
        a = valid[2]
    else:
      a=set
  else:
    print('Rock Paper or Scissors?')
    a = input()
  def check(a,b):
    if a!=b:
      if a == 'rock':
        if b == 'paper':
          return False
        if b == 'scissors':
          return True
      if a == 'paper':
        if b == 'rock':
          return True
        if b == 'scissors':
          return False
      if a == 'scissors':
        if b == 'rock':
          return False
        if b == 'paper':
          return True
  if a in valid:
    r = random.randint(1,3)
    if r == 1:
      b = valid[0]
    if r == 2:
      b = valid[1]
    if r == 3:
      b = valid[2]
    if not auto:
      print(b)
    if a == b:
      if not auto:
        print('tie')
      tiec+=1
    elif check(a,b):
      if not auto:
        print('YOU WIN')
      winc+=1
    else:
      if not auto:
        print('RIP')
      losec+=1
  else:
    if not auto:
      print('                       ', end='\n')
  runs-=1
  total+=1
if auto:
  print("average win %: " + str((winc/total)*100) + "  total: " + str(winc))
  print("average lose %: " + str((losec/total)*100) + "  total: " + str(losec))
  print("average tie %: " + str((tiec/total)*100) + "  total: " + str(tiec))
  print("total: "+ str(winc+losec+tiec))