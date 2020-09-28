import copy

class Node:
    def __init__(self, state, cost=None, heuristic=None, parent=None, total=None):
        self.state = state.copy()
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

        # this is used to find the cheapest node
        if total is None:
            self.total = self.cost + self.heuristic
        else:
            self.total = total

def heuristic_func(current_position):
    # returns the out of position tiles in the puzzle
    counter = 0
    final = [[1,2,3], [8,0,4], [7,6,5]]
    for i in range(3):
        for j in range(3):
            if current_position[i][j] != final[i][j]:
                counter += 1
    return counter

def generate_children(current_node):
    open_list = []
    # generates 4 new nodes with states based on the current state
    # the new nodes will have their parent set to current_node
    state = copy.deepcopy(current_node.state)
    # get the position of the blank spot (which has a value of 0)
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x = i
                y = j
    new_state = copy.deepcopy(state)
    try: 
        new_state[x][y], new_state[x+1][y] = new_state[x+1][y], new_state[x][y]
        node_state = copy.deepcopy(new_state)
        open_list.append(Node(copy.deepcopy(node_state), cost=current_node.cost + node_state[x][y], heuristic=heuristic_func(copy.deepcopy(node_state)),
        parent=current_node))
        new_state[x+1][y], new_state[x][y] = new_state[x][y], new_state[x+1][y]
    except IndexError:
        pass
    
    try:
        if x-1 >= 0:
            new_state[x][y], new_state[x-1][y] = new_state[x-1][y], new_state[x][y]
            node_state = copy.deepcopy(new_state)
            open_list.append(Node(copy.deepcopy(node_state), cost=current_node.cost + node_state[x][y], heuristic=heuristic_func(copy.deepcopy(node_state)),
            parent=current_node))
            new_state[x-1][y], new_state[x][y] = new_state[x][y], new_state[x-1][y]
    except IndexError:
        pass

    try:
        new_state[x][y], new_state[x][y+1] = new_state[x][y+1], new_state[x][y]
        node_state = copy.deepcopy(new_state)
        open_list.append(Node(copy.deepcopy(node_state), cost=current_node.cost + node_state[x][y], heuristic=heuristic_func(copy.deepcopy(node_state)),
        parent=current_node))
        new_state[x][y+1], new_state[x][y] = new_state[x][y], new_state[x][y+1]
    except IndexError:
        pass

    try:
        if y-1 >= 0:
            new_state[x][y], new_state[x][y-1] = new_state[x][y-1], new_state[x][y]
            node_state = copy.deepcopy(new_state)
            open_list.append(Node(copy.deepcopy(node_state), cost=current_node.cost + node_state[x][y], heuristic=heuristic_func(copy.deepcopy(node_state)),
            parent=current_node))
            new_state[x][y-1], new_state[x][y] = new_state[x][y], new_state[x][y-1]
    except IndexError:
        pass

    return open_list

def sort_function(node):
    return node.total

def find_solution(open_list=None, final_state=None):
    closed_list = []
    # while open list is not 0
    current_node = open_list[0]
    found_better_open = False
    found_better_closed = False
    while len(open_list) != 0:
        print("Checking the state:")
        for i in current_node.state:
            print(i)
        # pop the first element in the open list
        open_list = open_list[1:]

        if current_node.state == final_state:
            print("Final position reached with a total cost of: {0}".format(current_node.total))
            break

        children = generate_children(current_node)
        for i in children:

            # else if a similar state is found in open list with a lower cost, continue
            for j in open_list:
                if j.state == i.state:
                    if j.total < i.total:
                        found_better_open = True
                        break

            # else if a similar state is found in the closed list with a lower cost, continue
            for k in closed_list:
                if k.state == i.state:
                    if k.total < i.total:
                        found_better_closed = True
                        break    
            
            if found_better_open is False and found_better_closed is False:
                open_list.append(i)

                
            found_better_closed = False
            found_better_open = False


        closed_list.append(current_node)
        # find the node in the open list with the smallest total value f(n) = g(n) + h(n)
        open_list.sort(key=sort_function)
        current_node = open_list[0]


def main():
    open_list = []
    initial_state = []
    final_state = [[1,2,3], [8,0,4], [7,6,5]]
    with open('positions.txt', 'r') as infile:
        for line in infile:
            initial_state.append([int(x) for x in line.split()])
    open_list.append(Node(state=initial_state, cost=0, total=0, heuristic=heuristic_func(initial_state)))

    find_solution(open_list=open_list, final_state=final_state)

if __name__ == '__main__':
    main()



