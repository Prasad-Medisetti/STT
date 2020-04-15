#li = [['Prasad', 80, 83],
# ['Vara Prasad', 90, 95],
# ['Vineeth', 80, 85],
# ['Surya', 75, 70],
# ['Sai', 80, 75],
# ['Pratap', 90, 75],
# ['Sumanth', 80, 86],
# ['Suresh', 81, 73],
# ['Anil', 80, 76],
# ['Kiran', 8, 81]]
li = []
for i in range(10):
    e = []
    name = input("Enter Name of Student{}:\t".format(i+1)); e.append(name)
    sub1 = int(input("Enter Sub1 Marks:\t")); e.append(sub1)
    sub2 = int(input("Enter Sub2 Marks:\t")); e.append(sub2)
    li.append(e)
print('Name'.ljust(15,' '), 'Sub1', 'Sub2', sep='\t')
for i in range(10):
    print(li[i][0].ljust(15,' '), li[i][1], li[i][2], sep='\t')