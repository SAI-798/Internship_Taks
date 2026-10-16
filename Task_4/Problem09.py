
# Problem Name: Mutations
# HackerRank Link: https://www.hackerrank.com/challenges/python-mutations/problem

def mutate_string(string, position, character):
    result = string[:position] + character + string[position + 1:]
    return result

if __name__ == '__main__':
    s = input()
    position, character = input().split()

    result = mutate_string(s, int(position), character)
    print(result)
