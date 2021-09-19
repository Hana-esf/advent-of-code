with open('input.txt') as f:
    data = f.readlines()
numbers = [ int(num.strip('\n')) for num in data ]


for i in numbers:
    for j in numbers:
        if i + j == 2020:
            part1 = i * j
            
        for k in numbers:
            if i + j + k == 2020:
                part2 = i * j * k

print("part1 : ", part1 , "\npart2 : ",part2)