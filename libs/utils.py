import sys
import queue

def aoc_read(filename):
    try:
        print("Opening: %s" % filename)
        with open(filename) as f:
            lines = f.read().splitlines() 

        return lines
    except Exception as e:
        print(e)
        exit(-1)

    return []

def aoc_read_bysection(filename, convert="no"):
    lines = aoc_read(filename)

    r = []
    p = []
    for l in lines:
        if l == '':
            r.append(p)
            p = []
        else:
            if convert == "int":
                p.append(int(l))
            else:
                p.append(l)
    r.append(p)

    return r

def rechunk(r, cs):
    res = []
    for i in range(r[0], r[1], cs):
        f = i+cs-1
        if i+cs >= r[1]:
            f = r[1]
        res.append((i, f))

    return res

def aoc_read_asmap(filename):
    lines = aoc_read(filename)

    map = []
    for l in lines:
        m = [x for x in l]
        map.append(m)

    return map

class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        #for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)

class Cell:
    def __init__(self, x, y, dist, prev) :
        self.x = x
        self.y = y
        self.dist = dist; #distance to start
        self.prev = prev; #parent cell in the path
    def __str__(self):
        return "("+ str(self.x) + "," + str(self.y) + ")" 


def shortestPath(matrix, start, end):
    sx = start[0]
    sy = start[1]
    dx = end[0]
    dy = end[1]
    #if start or end value is 0, return
    if matrix[sx][sy] == 0 or matrix[dx][dy] == 0 :
        print("There is no path.")
        return  
    #initialize the cells 
    m = len(matrix)
    n = len(matrix[0])    
    cells = []
    for i in range (0, m) :
        row = []
        for j in range(0, n) :               
            if matrix[i][j] != 0 :
                row.append(Cell(i, j, sys.maxsize, None))
            else:
                row.append(None)
        cells.append(row) 
    #breadth first search
    queue = []     
    src = cells[sx][sy]
    src.dist = 0
    queue.append(src)
    dest = None
    p = queue.pop(0)
    while p != None :
        #find destination 
        if p.x == dx and p.y == dy : 
            dest = p
            break	             
        # moving up
        visit(cells, queue, p.x-1, p.y, p)    
        # moving left
        visit(cells, queue, p.x, p.y-1, p)     
        # moving down
        visit(cells, queue, p.x+1, p.y, p)             
        #moving right
        visit(cells, queue, p.x, p.y+1, p)
        if len(queue) > 0:
            p = queue.pop(0)
        else:
            p = None       
    #compose the path if path exists
    if dest == None :
        print("there is no path.")
        return
    else :
        path = []
        p = dest
        while p != None :
            path.insert(0, p)	      
            p = p.prev	       
        for i in path:
            print(i)

#function to update cell visiting status, Time O(1), Space O(1)
def visit(cells, queue, x, y, parent) :		
    #out of boundary
    if x < 0 or x >= len(cells) or y < 0 or y >= len(cells[0]) or cells[x][y] == None :
        return
    #update distance, and previous node
    dist = parent.dist + 1
    p = cells[x][y]
    if dist < p.dist :
        p.dist = dist
        p.prev = parent
        queue.append(p)

def mapPrint(m):
    print()
    for y in m:
        print(''.join([str(s) for s in y]))