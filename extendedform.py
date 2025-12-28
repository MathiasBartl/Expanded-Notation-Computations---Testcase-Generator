op = input("Enter Operator, eiter * or +:")
n = int(input("Enter Number of values:"))
values = []
if(op == "*"):
  res = 1
else:
  res = 0
for _ in range(n):
  inp = int(input("Enter Value as Integer:"))
  values.append(inp)
  if(op == "*"):
    res *= inp
  else:
    res += inp
print()
print(op)
print(n)
for _ in range(n):
  pot = 1
  output = ""
  num = values.pop(0)
  while (num > 0):
    digit = num % 10
    if pot > 1:
        if (len(str(num)) > 1):
          output = "+" + str(digit) + "x" + str(pot) +  output
        else:
          output = str(digit) + "x" + str(pot)  + output
    else:
      if (len(str(num)) > 1):
        output += "+" + str(digit)
      else:
        output += str(digit)
    num /= 10
    num=int(num)
    pot *= 10 
  print(output)  
print()
print(res)