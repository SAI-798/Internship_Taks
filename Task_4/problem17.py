
# Problem Name: Finding the Percentage
# HackerRank Link: https://www.hackerrank.com/challenges/finding-the-percentage/problem

if __name__ == '__main__':
    n = int(input())
    student_marks = {}

    for i in range(n):
        name, *marks = input().split()
        scores = list(map(float, marks))
        student_marks[name] = scores

    query_name = input()

    marks = student_marks[query_name]
    average = sum(marks) / len(marks)

    print("{:.2f}".format(average))
