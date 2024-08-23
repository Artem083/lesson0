grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students = {'Johnny','Bilbo','Steve','Khendrik','Aaron'}
##avg_grades = (sum(grades[0]) / (len(grades[0])), sum(grades[1]) / (len(grades[1])),
               #sum(grades[2]) / (len(grades[2])), sum(grades[3]) / (len(grades[3])),
               #sum(grades[4]) / (len(grades[4]))) ### не совсем верно
# print(students.union(avg_grades))
# print(type(students.union(avg_grades)))
# result_st = (students.union(avg_grades))
# #print(result_st.)
# print(sorted(students))
# print(type(avg_grades))
# print(avg_grades)
# print(type(avg_grades))
# print(type(sorted(students)))
# print(type(students))
#def passed (average_point : sum(grades) / len(grades)):


avg_grades = [sum(grades[0]) / len(grades[0]), sum(grades[1]) / len(grades[1]),
               sum(grades[2]) / len(grades[2]), sum(grades[3]) / len(grades[3]),
               sum(grades[4]) / len(grades[4])] ## Исправленное


print(avg_grades)
print(type(avg_grades))
print(sorted(students))
abc_student = sorted(students)
print(abc_student)
print(type(abc_student))
result_dict = (dict(zip(abc_student,avg_grades)))
print(result_dict)
print(type(result_dict))

########################################## BINGO ##############################

