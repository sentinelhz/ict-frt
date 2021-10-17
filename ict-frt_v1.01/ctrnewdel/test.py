def MainCount(f):
   def progFirst(*args, **kwargs):
       progFirst.calls += 1
       return f(*args, **kwargs)
   progFirst.calls = 0 
   return progFirst 

@MainCount
def progSecond(i):
    return i + 1

@MainCount
def Count(i =0, j =1):
    return i*j + 1

print(progSecond.calls)
for n in range(5):
    progSecond(n)
Count(j=0, i = 1)
print(Count.calls)
