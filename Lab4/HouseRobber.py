# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed away.
# The only constraint stopping you from robbing each of them is that adjacent houses have a security system connected,
# and it will automatically contact the police if two adjacent houses are broken into on the same night.
# Given a list of non-negative integers representing the amount of money in each house, determine the maximum amount of money you can rob tonight without alerting the police.

# Input
# The first number contains the number of houses n (1≤n≤106). The second line contains n non-negative integers a1​,a2​,...,an​, where ai​ is the amount of money that can be taken from the i-th house.
# Output
# Print the maximum sum you can steal tonight without triggering a police alert.

number_of_houses = int(input())
money_in_house = list(map(int, input().split()))
if number_of_houses == 1:
    print(money_in_house[0])
elif number_of_houses == 2:
    print(max(money_in_house[0], money_in_house[1]))
else:
    house_to_stole = [0]*3
    # house_to_stole = [0]*number_of_houses
    house_to_stole[0] = money_in_house[0]
    house_to_stole[1] = max(money_in_house[0], money_in_house[1])

    for amount_of_houses_to_steal in range(2, number_of_houses):
        house_to_stole[amount_of_houses_to_steal % 3] = max(money_in_house[amount_of_houses_to_steal] + house_to_stole[(amount_of_houses_to_steal - 2) % 3], house_to_stole[(amount_of_houses_to_steal - 1) % 3])
        # house_to_stole[amount_of_houses_to_steal] = max(money_in_house[amount_of_houses_to_steal] + house_to_stole[amount_of_houses_to_steal - 2], house_to_stole[amount_of_houses_to_steal - 1])

    print(house_to_stole[amount_of_houses_to_steal % 3])
    # print(house_to_stole[amount_of_houses_to_steal])
