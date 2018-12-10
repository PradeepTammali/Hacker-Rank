#!/bin/python

import os
import sys

# Complete the membersInTheLargestGroups function below.


def membersInTheLargestGroups(n, m, a, b, f, s, t):
    students = {}
    requests = {}
    groups = {}
    i = 0
    while i < n:
        name, grade = input().rstrip().split(' ')
        students[name] = int(grade)
        i += 1
    i = 0
    for i in range(0, m):
        requests[i] = list(input().rstrip().split(' '))

    for i in range(0, m):
        studentOne, studentTwo = requests[i][0], requests[i][1]
        for j in range(0, len(groups)):
            addStudent = False
            if studentOne in groups[j] and len(groups[j])+1 <= b:
                for k in range(0, len(groups)):
                    if k != j and studentTwo not in groups[k]:
                        addStudent = True
                        break
            if addStudent:
                groups[j].update(requests[i])
                break
        else:
            groups[len(groups)] = set(requests[i])
                
            
    # for i in range(0, m):
    #     for j in range(0, len(groups)):
    #         if j > 0 and any(elem in groups[j-1] for elem in groups[j]):
    #             print(set([groups[j-1],groups[j]]))
    #         if any(elem in requests[i] for elem in groups[j]) and len(groups[j]) < b:
    #             groups[j].update(requests[i])
    #             break
    #     else:
    #         groups[len(groups)] = set(requests[i])
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
