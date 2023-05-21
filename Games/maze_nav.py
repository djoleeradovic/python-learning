import curses
from curses import wrapper
import time
import queue

maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]



def print_maze(maze,stdscr,path=[]):
    blue_black = curses.color_pair(1)
    red_black = curses.color_pair(2)
    for i,row in enumerate(maze):
        for j,value in enumerate(row):
            if (i,j) in path:
                stdscr.addstr(i,j*2,"X",blue_black)
            else:
                stdscr.addstr(i,j*2,value,red_black)

def find_start(maze,start):
    for i,row in enumerate(maze):
        for j,value in enumerate(row):
            if value == start:
                return i,j
    return None

def make_path(maze,stdscr):
    start = "O"
    end = "X"
    start_position = find_start(maze,start)
    
    q = queue.Queue()
    q.put((start_position,[start_position]))

    visited = set()

    while not q.empty():
        current_position,path = q.get()
        row,col = current_position

        stdscr.clear()
        print_maze(maze,stdscr,path)
        time.sleep(0.2)
        stdscr.refresh()

        if maze[row][col] == end:
            return path
    
        neighbords = find_neighbords(maze,row,col)
        for neighbor in neighbords:
            if neighbor in visited:
                continue
            r,c = neighbor
            if maze[r][c] == "#":
                continue
            new_path = path + [neighbor]
            q.put((neighbor,new_path))
            visited.add(neighbor)
            
def find_neighbords(maze,row,col):
    neighbords=[]

    if row > 0:
        neighbords.append((row-1,col))
    if row +1<len(maze):
        neighbords.append((row+1,col))
    if col >0:
        neighbords.append((row,col-1))
    if col+1 <len(maze[0]):
        neighbords.append((row,col+1))
    return neighbords

def main(stdscr):
    curses.init_pair(1,curses.COLOR_BLUE,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)

    make_path(maze,stdscr)
    stdscr.getch()

wrapper(main)