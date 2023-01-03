class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        arr = [str(i+1) for i in range(n)]

        for i in range(n):
            if (int(arr[i]) % 3 == 0 and int(arr[i]) % 5 == 0):
                arr[i] = "FizzBuzz"
            elif (int(arr[i]) % 3 == 0):
                arr[i] = "Fizz"
            elif (int(arr[i]) % 5 == 0):
                arr[i] = "Buzz"
            else:
                continue
        return arr
        
        
