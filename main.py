for i in range(5): 
  print 'A number:', i

name = raw_input('What is your name?\n') 
print 'Hi, %s.' % name

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)
print factorial(5)

import time
now = time.localtime()
hour = now.tm_hour
if hour < 8: print 'sleeping'
elif hour < 9: print 'commuting'
elif hour < 17: print 'working'
elif hour < 18: print 'commuting'
elif hour < 20: print 'eating'
elif hour < 22: print 'resting'
else: print 'sleeping'