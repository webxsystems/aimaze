from tabulate import tabulate

init = 'A'
goal = 'B'
t = ' '
nt = '#'
M = []
current_position = []
up = bool
right = bool
left = bool
down = bool
maze_size = []
next_node = []

for line in open('C:\\Users\\pepe\\Downloads\\src0\\src0\\maze1.txt'):
    L = list(line.rstrip())
    M.append(L)


def goal_cordinates(M,goal):
    for r, row in enumerate(M):
        for c, value in enumerate(row):
            if value == goal:
                return r, c
    return None

def init_cordinates(M,init):
    for r, row in enumerate(M):
        for c, value in enumerate(row):
            if value == init:
                return r, c
    return None

def valid_action_up(current_position):
    if (current_position[0] - 1):
        if (current_position[0] - 1, current_position[1] == t):
            return True
        return False
    return False

def valid_action_right(current_position):
    if (current_position[1] + 1):
        if (M[current_position[0]][current_position[1] + 1] == t):
            return True
        return False
    return False

def valid_action_left(current_position):
    if (current_position[1] - 1):
        if ([current_position[0]][current_position[1] - 1] == t):
            return True
        return False
    return False

def valid_action_down(current_position):
    if (current_position[0] - 1):
        if ([current_position[0] - 1][current_position[1]] == t):
            return True
        return False
    return False

def valid_action_right(current_position):
    if (current_position[0][current_position[1] + 1] == t):
        return True
    return False

def get_maze_size(M):
    r = len(M)
    c = len(M[0])
    return r, c

maze_size = get_maze_size(M)

print(f"maze_size->{maze_size}")

print(f"initial state-> {init} {init_cordinates(M, init)}")
print(f"goal-> {goal} {goal_cordinates(M, goal)}")

current_position = init_cordinates(M, init)
print(current_position[0], current_position[1])
print(current_position[0]-1,current_position[1])
print(current_position[0],current_position[1]+1)
print(current_position[0],current_position[1]+1)
coords = (current_position[0], current_position[1] + 1)
print(coords)
element = M[current_position[0]][current_position[1] + 1]
print(element)

# up = valid_action_up(current_position)
# right = valid_action_right(current_position)
print(current_position[1] - 1)

def next_move():
    next_node =


if (valid_action_left(current_position)):
    print(f"can go left")
else:
    print(f"can not go left")

if (valid_action_down(current_position)):
    print(f"can go down")
else:
    print(f"can not go down")


if (valid_action_up(current_position)):
    print(f"can go up")
else:
    print(f"can not go up")

if (valid_action_right(current_position)):
    print(f"can go right")
else:
    print(f"can not go right")

# print(valid_action_up(current_position))
# print(valid_action_right(current_position))


# print(M)


# print(M[5][0])
print(tabulate(M, tablefmt="grid"))
# b = any(goal in row for row in M)
# print(b)
