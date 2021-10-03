with open('input.txt') as f:
    data = f.readlines()
pass_policy = [ str.split() for str in data ]

#part 1

valid_pass1 = 0
valid_pass2 = 0
for input in pass_policy:

    numbers = input[0].split('-')
    min = int(numbers[0])
    max = int(numbers[1])


    letter = input[1].strip(':')
    password = input[2]

    if password.count(letter) >= min and password.count(letter) <= max:
        valid_pass1 += 1

#part2
  
    if (password[min-1] == letter) ^ (password[max-1] == letter): 
        valid_pass2 += 1


print('part1:', valid_pass1)
print('part2: ',valid_pass2)


