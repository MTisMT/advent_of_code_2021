## Part 1
with open("day2.txt") as f:
    lines = [l.strip() for l in f]

commands = [l.split(' ') for l in lines]
commands = [[c[0], int(c[1])] for c in commands]
forward = [c for c in commands if c[0]=='forward']
down = [c for c in commands if c[0]=='down']
up = [c for c in commands if c[0]=='up']
print(len(commands)== len(forward)+len(down)+len(up))
total_forwards = sum([c[1] for c in forward])
total_down = sum([c[1] for c in down])
total_up = sum([c[1] for c in up])
print('total_forwards: ',total_forwards,'\n','total_down: ',total_down,'\n','total_up: ',total_up)
answer_1 = total_forwards * (total_down - total_up)
print("Answer of part 1",answer_1)

## Part 2
depth = 0
aim = 0
horiz = 0
for c in commands:
    if c[0] == 'down':
        aim += c[1]
    elif c[0] == 'up':
        aim -= c[1]
    else:
        horiz += c[1]
        depth += c[1]*aim
answer_2 = depth*horiz
print("Answer of part 2",answer_2)
