"""
Your task is to make a function that can take any non-negative integer
as an argument and return it with its digits in descending order.
Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321
"""

def descending_order(num: int):
    num_arr = list(str(num))

    # Sorting
    for index in range(1, len(num_arr)):
        next = num_arr[index]
        curr = index - 1

        while num_arr[curr] < next and curr != -1:
            num_arr[curr + 1] = num_arr[curr]
            curr = curr - 1

        num_arr[curr + 1] = next
    
    ans = ""

    for digit in num_arr:
        ans += f"{digit}"

    return ans

print(descending_order(23562))