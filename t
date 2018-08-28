import time
CacheMax = 1000000
cached = [None] * CacheMax
cached[1] = 1
def recCL(n):
   if n < CacheMax and cached[n] != None:
      return cached[n]
   elif n % 2 == 0:
      temp = 1 + recCL(n/2)
   else:
      temp = 1 + recCL(3*n+1)
   if n < CacheMax:
      cached[n] = temp
   return temp

# Brute force method takes about 34 seconds
# Dynamic programming method takes ~2 seconds
start = time.clock()
maxLen = 0
maxInd = None
for ii in range(1, 1000000):
   a = recCL(ii)
   if a > maxLen:
      maxLen = a
      maxInd = ii
end = time.clock()
print("Elapsed =", end-start)
print(maxInd)
