import main
import random

FibArray = [0,1] 
def fibonacci(n): 
  if n<0: 
    print("Incorrect input") 
  elif n<=len(FibArray): 
    return FibArray[n-1] 
  else: 
    temp_fib = fibonacci(n-1)+fibonacci(n-2) 
    FibArray.append(temp_fib) 
    return temp_fib

def fib_temp(n):
  o=[]
  for i in range(n):
    o.append(fibonacci(i+1))
  return o

def test_main():
  for i in range(20):
    r = random.randint(0, 1000)
    assert main.fibb(r) == fib_temp(r)
