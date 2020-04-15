# Sorting input.txt file and writing into output.txt

with open('input.txt') as f:
    l = [int(i) for i in f.readlines()]
    l = [str(i)+'\n' for i in sorted(l)]
    with open('output.txt','w') as o:
        o.writelines(l)