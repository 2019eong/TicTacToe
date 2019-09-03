blank = "."*9
global player
player = 0
ppl = {1:"X", -1:"O"}
############################################################################################
def gridForm(str):
    grid = " ".join([x for x in str[0:3]]) + "\n" + " ".join([x for x in str[3:6]]) + "\n" + " ".join([x for x in str[6:]])
    return grid
def get_next_player():
    global player
    player = -1*player
    return player
def find_valid_moves(str):   # Str is current board string; p is person's turn
    return [x for x in range(len(str)) if str[x]=="."]
def make_move(str, var, p):
    str = str[0:var]+ppl[p]+str[var+1:]
    return str
def goal_test(str, p):
    # check row wins
    R = [True if str[x:x+3]==ppl[p]*3 else False for x in range(0, 9, 3)]
    if True in R:  return True  # AKA if there's one row that's True
    # check col wins
    C = [True if str[x:9:3]==ppl[p]*3 else False for x in range(0,3)]
    if True in C: return True
    # check diagonal wins
    D = True if str[0:9:4]==ppl[p]*3 or str[2:8:2]==ppl[p]*3 else False
    if D: return True
# def BFS(str):                   # performs BFS on str, which is starting config
#     visited = set() # set of visited states
#     n = Node(str, None, "", 1) # first node doesn't have parent
#     fringe = deque()
#     fringe.append(n)
#     while len(fringe) > 0:
#         temp = fringe.popleft()    # remove from front, treat like a queue  deque
#         if goal_test(temp.state)==True:     # if state is the goal state
#             return temp
#         else:   # if state is NOT goal state, put on valid children that haven't been visited yet
#             up = make_move(temp.state, "U")
#             down = make_move(temp.state, "D")
#             left = make_move(temp.state, "L")
#             right = make_move(temp.state, "R")
#             directions, dChar , ct = [up, down, left, right], ["U", "D", "L", "R"], 0
#             for x in directions:
#                 if x not in visited and x!=None:    # if config not performed before and config is possible
#                     fringe.append(Node(x, temp, dChar[ct], temp.depth+1))     # add to queue
#                     visited.add(x)
#                 ct+=1
#     return
############################################################################################
# b = blank
# b = make_move(b, 0, 1)
# b = make_move(b, 4, 1)
# b = make_move(b, 8, 1)
# print(gridForm(b))
# print(goal_test(b, 1))