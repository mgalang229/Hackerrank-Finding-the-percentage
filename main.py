n = int(input())

student_marks = {}
for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input()
sum = 0
for x in student_marks[query_name]:
    sum += x
sum = sum / 3
ans = "{:.2f}".format(sum)
print(ans)
