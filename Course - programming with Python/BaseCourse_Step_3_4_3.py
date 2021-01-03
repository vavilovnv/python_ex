# Текст задания: https://stepik.org/lesson/3363/step/4?unit=1135

math, phis, rusl, students = 0, 0, 0, [student.strip().split(';') for student in open('input.txt').readlines()]

f = open('out.txt', 'w')
for student in students:
    f.write(str((int(student[1]) + int(student[2]) + int(student[3]))/3)+'\n')
    math += int(student[1])
    phis += int(student[2])
    rusl += int(student[3])
f.write(str(math/len(students)) + ' ' + str(phis/len(students)) + ' ' + str(rusl/len(students)))
f.close()

