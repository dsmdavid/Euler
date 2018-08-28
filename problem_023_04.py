import time
import functools
def main():
   # Find the sum of all positive integers that cannot be written as the sum of two abundant numbers
   # NOTE: Only evaluate integers under 20162
   # NOTE: every EVEN integer greater than 46 is the sum of two abundant numbers

   # finds abundantNumbers under 20162
   print("Finding Abundant Numbers")
   abundantNumberList = findAbundantNumbers()
   abundantNumberList.sort()

   # creates an odd abundant numbers list and some small evens to lower number of additions
   print("Truncating List")
   oddList = set()
   for number in abundantNumberList:
      if number%2!=0 or number < 46:
         oddList.add(number)
   oddList = list(oddList)
   oddList.sort()

   # finds the possible sums of abundant numbers
   print("Finding Possible Sums")
   possibleSums = set()
   for number2 in oddList:
      for number in abundantNumberList:
         tempSum = number + number2
         if tempSum > 20162: break
         possibleSums.add(tempSum)

   # finds all positive integers that cannot be written as the sum of two abundant numbers
   notSums = set()
   for i in range(1, 20162):
      if not i in possibleSums:
         notSums.add(i)
   notSums = list(notSums)
   notSums.sort()

   # prints sum of all positive integers that cannot be written as the sum of two abundant numbers
   print("Answer:", sum(notSums))


def findAbundantNumbers():
   abundantNumbers = set()
   for i in range(12, 20162):
      if sum(findProperDivisors(i)) > i: abundantNumbers.add(i)
   return list(abundantNumbers)


def findProperDivisors(n):
   divisorList = list(set(functools.reduce(list.__add__,
      ([i, n/i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

   #sorts and takes off the last divisor (itself)
   divisorList.sort()
   return divisorList[:-1]

if __name__ == '__main__':
   a = time.time() 
   main()
   print(time.time() - a)
