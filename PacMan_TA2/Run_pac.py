# from pyamaze import maze,COLOR,agent
from pyMaze import maze,COLOR,agent

def BFS(m,start,goal):
    bsearch=[]
    bfsPath={}
    frontier=[start]
    explored=[start]
    while frontier!=[]:
        current=frontier.pop(0)
        if current==goal:
            break
        for d in 'ESNW':
            if m.maze_map[current][d]==True:
                if d=='E':
                    child = (current[0],current[1]+1)
                elif d=='W':
                    child = (current[0],current[1]-1)
                elif d=='N':
                    child = (current[0]-1,current[1])
                elif d=='S':
                    child = (current[0]+1,current[1])
                if child in explored:
                    continue
                frontier.append(child)
                explored.append(child)
                bfsPath[child]=current
                bsearch.append(child)
    path={}
    cell=goal
    while cell!=start:
        path[bfsPath[cell]]=cell
        cell = bfsPath[cell]
    return bsearch,bfsPath,path
    


m=maze()
goal = (19,1)
start = (10,15)
m.CreateMaze(19,1,loadMaze='maze--2022-06-19--18-44-25.csv')
pac=agent(m,start[0],start[1],footprints=True,color=COLOR.blue,filled=True)
arrow = agent(m,start[0],start[1],shape='arrow',footprints=True,color=COLOR.green,filled=False)
bsearch,bfsPath,p=BFS(m,start,goal)
m.tracePath({arrow:bsearch},delay=100)
m.tracePath({pac:p})
m.run()

