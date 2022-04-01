#!/usr/bin/env python3

import sys
import heapq

Location = TypeVar('Location')

class PriorityQueue:
    def __init__(self):
        self.elements: List[Tuple[float, T]] = []
    
    def empty(self) -> bool:
        return not self.elements
    
    def put(self, item: T, priority: float):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self) -> T:
        return heapq.heappop(self.elements)[1]

def findRoute(maze, start, end):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from: Dict[Location, Optional[Location]] = {}
    cost_so_far: Dict[Location, float] = {}
    came_from[start] = None
    cost_so_far[start] = 0

def main():
    if len(sys.argv) == 1:
        #print("Opening: %s" % sys.argv[1])

        maze = []
        #for l in open(sys.argv[1]).read().splitlines():
        for l in open("/Users/malfax/Documents/adventofcode/2021/15/ss.txt").read().splitlines():
            t = []
            for c in l:
                t.append(int(c))
            maze.append(t)

        path = astar(maze, (0,0), (len(maze[0])-1, len(maze)-1))
        print(path)

if __name__ == '__main__':
    main()