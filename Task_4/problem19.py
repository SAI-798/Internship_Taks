
# Problem Name: Collections.Counter()
# HackerRank Link: https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

if __name__ == '__main__':
    x = int(input())
    shoe_sizes = list(map(int, input().split()))

    size_count = Counter(shoe_sizes)

    n = int(input())
    total_money = 0

    for i in range(n):
        size, price = map(int, input().split())

        if size_count[size] > 0:
            total_money += price
            size_count[size] -= 1

    print(total_money)
