#!/bin/python

import os
import sys

student_grades = {}
student_group = {}  # { A : 0, B : 0, C : 1, D : 1, E : 1}

# helper function to check the limits for each grade


def checkGradesLimit(students_list):
    firstGrade = secondGrade = thirdGrade = 0
    for student in students_list:
        if student_grades[student] == 1:
            firstGrade = firstGrade + 1
        elif student_grades[student] == 2:
            secondGrade = secondGrade + 1
        elif student_grades[student] == 3:
            thirdGrade = thirdGrade + 1
    return firstGrade <= f and secondGrade <= s and thirdGrade <= t


def getKeysByValue(value):
    return [k for (k, v) in student_group.items() if v == value]


# Complete the membersInTheLargestGroups function below.

# n = number of test cases
# m = number of requests
# a = min for group
# b = max for group
# f = first grade max
# s = second grade max
# t = third grade max
def membersInTheLargestGroups(n, m, a, b, f, s, t):
    groups_count = 0
    requests = {}
    i = 0
    while i < n:
        name, grade = input().rstrip().split(' ')
        student_grades[name] = int(grade)
        i += 1
    for i in range(0, m):
        requests[i] = input().rstrip().split(' ')
    for i in range(0, m):
        studentOne, studentTwo = requests[i]
        studentOneFlag = False
        studentTwoFlag = False
        if studentOne in student_group:
            studentOneFlag = True
        if studentTwo in student_group:
            studentTwoFlag = True
        if studentOneFlag and studentTwoFlag:
            studentOneKeys = getKeysByValue(student_group[studentOne])
            studentTwoKeys = getKeysByValue(student_group[studentTwo])
            if student_group[studentOne] != student_group[studentTwo] and len(studentOneKeys) + len(studentTwoKeys) <= b:
                # check if max limit reached for studentOne and studentTwo's groups
                if checkGradesLimit(studentOneKeys + studentTwoKeys):
                    # concat higher group with lower group and discard higher group
                    mergeGroups = (student_group[studentTwo], student_group[studentOne]) if student_group[studentOne] > student_group[studentTwo] else (
                        student_group[studentOne], student_group[studentTwo])
                    student_group.update(dict.fromkeys(
                        getKeysByValue(mergeGroups[1]), mergeGroups[0]))
                    for i in range(mergeGroups[1]+1, groups_count):
                        student_group.update(
                            dict.fromkeys(getKeysByValue(i), i-1))
                    groups_count -= 1
        elif studentOneFlag:
            studentOneKeys = getKeysByValue(student_group[studentOne])
            if len(studentOneKeys) < b and checkGradesLimit(studentOneKeys + [studentTwo]):
                #  add studentTwo to studentOne's group
                student_group[studentTwo] = student_group[studentOne]
        elif studentTwoFlag:
            studentTwoKeys = getKeysByValue(student_group[studentTwo])
            if len(studentTwoKeys) < b and checkGradesLimit(studentTwoKeys + [studentOne]):
                #  add studentOne to studentTwo's group
                student_group[studentOne] = student_group[studentTwo]
        else:
            # add both the students to a new group
            student_group[studentOne] = groups_count
            student_group[studentTwo] = groups_count
            groups_count += 1

    max_len = 0
    output = []
    for group in range(0, groups_count):
        groupKeys = getKeysByValue(group)
        max_value = len(groupKeys)
        if max_value == max_len:
            output += groupKeys
        if max_value > max_len:
            max_len = max_value
            output = groupKeys
    if max_len >= a:
        output.sort()
        for student in output:
            print(student)
    else:
        print("no groups")
    return


if __name__ == '__main__':
    nmabfst = input().split()
    n = int(nmabfst[0])
    m = int(nmabfst[1])
    a = int(nmabfst[2])
    b = int(nmabfst[3])
    f = int(nmabfst[4])
    s = int(nmabfst[5])
    t = int(nmabfst[6])
    membersInTheLargestGroups(n, m, a, b, f, s, t)
