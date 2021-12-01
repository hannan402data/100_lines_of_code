# 1: To put all the negative on one side.
def negoneside(arr, n):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if (arr[i] < 0):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    print(arr)

arr = [1,2,3,-6,-7,3,60]
n = len(arr)
negoneside(arr, n)

# 2: To rotate an Array
def rotate(arr):
    print([arr[-1]] + arr[0:-1])

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    rotate(arr)

# 3: To get the maximum SubArray Sum from the array.
def maxSubArraySum(arr, n):
    curr_sum = 0
    n = len(arr)
    max_so_far = arr[0]

    for i in range(0, n):
        curr_sum += arr[i]
        if (max_so_far < curr_sum):
            max_so_far = curr_sum
        if (curr_sum < 0):
            curr_sum = 0
    print(max_so_far)
arr = [1,2,3,-3,5]
maxSubArraySum(arr, n)

# 4: Minimum Jumps to reach the end of the array.
def minJumps(arr):
    if arr[0] == 0:
        return float('inf')
    
    n = len(arr)
    dp = [0 for i in range(n)]

    for i in range(1, n):
        dp[i] = float('inf')
        for j in range(0, i):
            if i <= j + arr[j]:
                dp[i] = min(dp[i], dp[j] + 1)
    return dp[-1]
arr = [1,5,6]
print("Number of Jumps: ", minJumps(arr))

# 5: To get the duplicates element from the Array.
arr = [1,2,3,4,5,6,6,7,7]
res = []
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if (arr[i] == arr[j]):
            res.append(arr[i])
print("Duplicates are: ", res)

# 6: To get the sum of digit.

def sum_of_digit(n):
    if n == 0:
        return 0
    return (n % 10 + sum_of_digit(int(n / 10)))
num = 123456789
print("Sum is: ", sum_of_digit(num))

# 7: To get the maximum sum from the array.

l = [8,3,1,2]
res = 0

for i in range(len(l)):
    c = 0
    s = 0

    for j in l:
        s = j*c + s
        c = c + 1
    if (res<s):
        res = s

    d = l.pop()
    l.insert(0,d)

print(res)
    
# 8: To reverse the string.

def reverseString(str):
    if (len(str) <= 1):
        return str
    return reverseString(str[1:]) + str[0]
print(reverseString('Reverse'))