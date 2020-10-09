"""
Find Duplicate number

Given an array 'nums' containing n + 1 integers where each integer is between
1 and n (inclusive). Prove that at least one duplicate number must exist
"""


def find_duplicade(nums):
    tartatuga, lebre = nums[0], nums[0]
    while True:
        tartatuga = nums[tartatuga]
        lebre = nums[nums[lebre]]
        if tartatuga == lebre: break

    ponto1 = nums[0]
    ponto2 = tartatuga
    while ponto1 != ponto2:
        ponto1 = nums[ponto1]
        ponto2 = nums[ponto2]

    return ponto1

print(find_duplicade([3, 3, 3, 4, 1, 5, 3, 7]))