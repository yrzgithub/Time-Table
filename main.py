from random import *

# subjects_count : int = int(input("no. of subjects"))
# staffs_count : int = int(input("no. of subjects"))

subjects : list = input("Subject names : ").split()

staffs = dict()
for subject in subjects:
    staffs[subject] = input(f"staff name for {subject} : ")

subjects_count : int = len(subjects)
staffs_count : int = len(staffs)

week_days : int = 7
periods_per_day : int = 7

days = ("mon","tue","wed","thur","fri","sat")

table = dict()

for day in days:
    table[day] = []
    copy = subjects[:]
    for n in range(periods_per_day):
        choice_ = choice(copy)
        copy.remove(choice_)
        table[day].append(choice_)

        if len(copy) == 0:
            copy = subjects[:]


print("\n\n\nClass Room \n")

for day in days:
    print(day," : ",*table[day])

print("\n\n\nStaff Room \n")
for day in days:
    print(day," : ",end = "")
    for sub in table[day]:
        print(staffs[sub],end=", ")
    print()