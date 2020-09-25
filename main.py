# make an openlist containing only the starting node
#    make an empty closed list
#    while (the destination node has not been reached):
#        consider the node with the lowest f score in the open list
#        if (this node is our destination node) :
#            we are finished 
#        if not:
#            put the current node in the closed list and look at all of its neighbors
#            for (each neighbor of the current node):
#                if (neighbor has lower g value than current and is in the closed list) :
#                    replace the neighbor with the new, lower, g value 
#                    current node is now the neighbor's parent            
#                else if (current g value is lower and this neighbor is in the open list ) :
#                    replace the neighbor with the new, lower, g value 
#                    change the neighbor's parent to our current node

#                else if this neighbor is not in both lists:
#                    add it to the open list and set its g

class Node:
    def __init__(self, state, cost=None, heuristic=None, parent=None):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic


def manhattan_distance(current_position):
    # returns the manhattan distance of a state
    final_coords = {0:[1,1], 1:[0,0], 2:[0,1], 3:[0,2], 4:[1,2], 5:[2,2], 6:[2,1], 7:[2,0], 8:[1,0]}
    total = 0
    for i in range(9):
        for j in range(3):
            for k in range(3):
                if current_position[j][k] == i:
                    x = j
                    y = k
                    x_final = final_coords[i][0]
                    y_final = final_coords[i][1]
                    total += abs(x - x_final) + abs(y - y_final)
    return total

def generate_children(current_node, open_list):
    # generates 4 new nodes with states based on the current state
    # the new nodes will have their parent sent to current_node
    state = current_node.state.copy()
    # get the position of the blank spot (which has a value of 0)
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x = i
                y = j
                print("found empty spot at: {0} {1}".format(x, y))
    new_state = state.copy()
    try: 
        new_state[x][y], new_state[x+1][y] = new_state[x+1][y], new_state[x][y]
        open_list.append(Node(new_state, cost=current_node.cost + new_state[x][y], heuristic=manhattan_distance(new_state),
        parent=current_node))
        new_state[x+1][y], new_state[x][y] = new_state[x][y], new_state[x+1][y]
    except IndexError:
        pass
    
    try:
        new_state[x][y], new_state[x-1][y] = new_state[x-1][y], new_state[x][y]
        open_list.append(Node(new_state, cost=current_node.cost + new_state[x][y], heuristic=manhattan_distance(new_state),
        parent=current_node))
        new_state[x-1][y], new_state[x][y] = new_state[x][y], new_state[x-1][y]
    except IndexError:
        pass

    try:
        new_state[x][y], new_state[x][y+1] = new_state[x][y+1], new_state[x][y]
        open_list.append(Node(new_state, cost=current_node.cost + new_state[x][y], heuristic=manhattan_distance(new_state),
        parent=current_node))
        new_state[x][y+1], new_state[x][y] = new_state[x][y], new_state[x][y+1]
    except IndexError:
        pass

    try:
        new_state[x][y], new_state[x][y-1] = new_state[x][y-1], new_state[x][y]
        open_list.append(Node(new_state, cost=current_node.cost + new_state[x][y], heuristic=manhattan_distance(new_state),
        parent=current_node))
        new_state[x][y-1], new_state[x][y] = new_state[x][y], new_state[x][y-1]
    except IndexError:
        pass

        


def main():
    open_list = []
    initial_state = []
    final_state = [[1,2,3], [8,0,4], [7,6,5]]
    with open('positions.txt', 'r') as infile:
        for line in infile:
            initial_state.append([int(x) for x in line.split()])
    open_list.append(Node(state=initial_state, cost=0, heuristic=manhattan_distance(initial_state)))
    generate_children(open_list[0], open_list)


main()



