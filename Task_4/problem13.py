
# Problem Name: Symmetric Difference
# HackerRank Link: https://www.hackerrank.com/challenges/symmetric-difference/problem

if __name__ == '__main__':
    n = int(input())
    set_a = set(map(int, input().split()))

    m = int(input())
    set_b = set(map(int, input().split()))

    result = set_a.symmetric_difference(set_b)

    for number in sorted(result):
        print(number)
