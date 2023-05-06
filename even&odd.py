def evenodd(number):
  if number%2==0:
    return "even"
  else :
    return "odd"
a = int(input("enter the number "))
print("the given number is",evenodd(a))
