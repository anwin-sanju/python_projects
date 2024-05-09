student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

height = 0
counter = 0

for i in student_heights:
  counter+=1
  height=height+i

average = height//counter

print("total height = "+str(height))
print("number of students = "+str(counter))
print("average height = "+str(average))