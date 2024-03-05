if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student = [name,score]
        records.append(student)

 #sort the list of lists based on specific element in inner list

second_grade = sorted(set([i[1] for i in records]))[1]
names = [i[0] for i in records if i[1] == second_grade]
names.sort()
for name in names:
    print(name)