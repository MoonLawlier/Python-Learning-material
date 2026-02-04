'''import math 
def codingProblems(a1,a2):
    a1 = int(a1/2)
    a2 = int(a2/2)
    return (a1+a2)*5

print(codingProblems(10,12))

def lcm(a,b):
    m = max(a,b)
    n = min(a,b)
    
    while(1):
        if m%a == 0 and m%b == 0:
            return m
        m += 1
    return m

print(lcm(4,6))

def sum(a,b,c):
    res = [a,b,c]
    high = max(res)
    return a+b+c - high + high*high

print(sum(1,5,5))

def dogYears(a1):
    if (a1 == 1):
        return a1*15
    elif (a1==2):
        return 9+15
    elif (a1>=3 and a1<=6):
        return 9+15+(a1-2)*4
    else:
        return 9+15+16+(a1-6)*5
    
print(dogYears(68))

n = int(input())
count = 0
for _ in range(n):
    a,b = input().split( )
while(1):
   lst1 = list(a)
   lst2 = list(b)
   if lst1 == lst2:
       count +=1
       print(count)

def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)

def unique_list(arr):
    return list(set(arr))


def get_pangram(a1):
    alpha = "qwertyuiopasdfghjklzxcvbnm"
    for char in alpha:
        if char not in a1.lower():
            print("It is not a Pangram")
            break
        else:
            print("It is a Pangram")
            break
    return ""

print(get_pangram("go")

def animal_crackers(a1):
    word1, word2 = a1.lower().split()
    if word1[0] == word2[0]:
        return True
    return False

print(animal_crackers("Levelheaded Llama"))
print(animal_crackers("Crazy Kangaroo"))

def spy_game(a1):
    sub = [0,0,7]
    if sub in a1:
        return True 
    return False

print(spy_game([1,2,4,0,0,7,5]))



def reverse_string(s):
    return s[::-1]

print(reverse_string("Hello"))

def capitalize(s):
    return ' '.join(word.capitalize() for word in s.split(' '))

print(capitalize("hello world! practice makes perfect"))

def remove(s,i):
    string = list(s)
    string.pop(i)
    return ''.join(string)


print(remove("hello", 1))

def mulWord(s, n):
    print(" ".join([s]*n))

mulWord('Hello', 3)

def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1): 
        if num % i == 0:
            return False
    return True 

print(int(3**0.5 + 1))
print(int(15**0.5 + 1))


def mirrorDistance(num):
    new = list(str(num))
    new.reverse()
    rev = int(''.join(new))
    return abs(num - rev)

print(mirrorDistance(123))

from collections import Counter
def minCost(s,cost):
    total = 0
    new = []
    counts = Counter(s)
    most_common_char , frequency = counts.most_common(1)[0]
    print(most_common_char[0])
   
    for i in range(len(s)-1):
        if s[i] != most_common_char[0]:
            new.append(i)
        else:
            continue
    print(new)
    for j in new:
        total += cost[j]
    return total


print(minCost("aabaac",[1,2,3,4,1,10]))

def largestOddNumber(num):
        """
        :type num: str
        :rtype: str
        """
        n = int(num)
        largest_odd = None
        curr = n

        while curr > 0:
            if curr%2 != 0:
                if largest_odd is None or curr> largest_odd:
                    largest_odd = curr
                    curr //= 10
        return largest_odd
                        
print(largestOddNumber("10133890"))

def is_anagram(s,t):

    arr_s = list(s)
    arr_s.sort()
    arr_t = list(t)
    arr_t.sort()
    if arr_s == arr_t:
        return True
    return False

print(is_anagram("cat","rat")) 

def reverseWords(s):
        """
        :type s: str
        :rtype: str
        """
        arr = s.split() # splits the string into words
        print(arr)
        arr.reverse() # reverses the list of words
        return ' '.join(arr) 

print(reverseWords("the sky is blue"))

def anagram(n):

    cnt = 0
    for _ in range(n):
        a,b = map(int, input().split())

        lst1 = list(str(a)).sort()
        lst2 = list(str(b)).sort()

        if lst1 == lst2:
            cnt += 1
        else:
            continue
    return cnt

print(anagram(3))

def missingNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if len(nums) == 1 :
            if nums[-1]<= 0:
                return nums[-1] +1 
            else:
                return nums[-1] -1 
        for i in range(0,nums[-1]):
            if nums[i] + 1 != nums[i+1]:
                  return nums[i]+1
        return nums[-1]+1

print(missingNumber([1,2]))'''













    


        