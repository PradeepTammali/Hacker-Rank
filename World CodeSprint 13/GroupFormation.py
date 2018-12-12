#!/bin/python

import os
import sys

student_grades = {}

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


# Complete the membersInTheLargestGroups function below.

# n = number of test cases
# m = number of requests
# a = min for group
# b = max for group
# f = first grade max
# s = second grade max
# t = third grade max
def membersInTheLargestGroups(n, m, a, b, f, s, t):
    groups = {}         # { 0 : [A, B], 1 : [C, D, E]}
    student_group = {}  # { A : 0, B : 0, C : 1, D : 1, E : 1}
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
            if student_group[studentOne] != student_group[studentTwo] and len(groups[student_group[studentOne]]) + len(groups[student_group[studentTwo]]) <= b:
                # check if max limit reached for studentOne and studentTwo's groups
                if checkGradesLimit(groups[student_group[studentTwo]] | groups[student_group[studentOne]]):
                    # concat higher group with lower group and discard higher group
                    mergeGroups = (student_group[studentTwo], student_group[studentOne]) if student_group[studentOne] > student_group[studentTwo] else (
                        student_group[studentOne], student_group[studentTwo])
                    for i in groups[mergeGroups[1]]:
                        student_group[i] = mergeGroups[0]
                    groups[mergeGroups[0]] = groups[mergeGroups[0]
                                                    ] | groups[mergeGroups[1]]
                    for i in range(mergeGroups[1], len(groups)-1):
                        groups[i] = groups[i+1]
                        for student in groups[i+1]:
                            student_group[student] = i
                    groups.pop(len(groups)-1)
        elif studentOneFlag:
            if len(groups[student_group[studentOne]]) < b and checkGradesLimit(groups[student_group[studentOne]] | {studentTwo}):
                #  add studentTwo to studentOne's group
                student_group[studentTwo] = student_group[studentOne]
                groups[student_group[studentOne]].add(studentTwo)
                # check for the student grades in each group
        elif studentTwoFlag:
            if len(groups[student_group[studentTwo]]) < b and checkGradesLimit(groups[student_group[studentTwo]] | {studentOne}):
                #  add studentOne to studentTwo's group
                student_group[studentOne] = student_group[studentTwo]
                groups[student_group[studentTwo]].add(studentOne)
        else:
            # add both the students to a new group
            student_group[studentOne] = len(groups)
            student_group[studentTwo] = len(groups)
            groups[len(groups)] = {studentOne, studentTwo}

    max_len = 0
    for group in groups:
        if len(groups[group]) > max_len:
            max_len = len(groups[group])
    if max_len >= a:
        output = [item for sublist in filter(lambda g: len(
            g) == max_len, groups.values()) for item in sublist]
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
