from Data import *
_cost = 0
count = 0

class PA_Ai:
    def __init__(krishna,graph,visited_arr,dict,_cost,count,heuristic):
        krishna.graph = graph
        krishna.visited_arr = visited_arr
        krishna.dict = dict
        krishna._cost = _cost
        krishna.count = count
        krishna._stack = [[0,krishna.graph[0][0]]]
        krishna.gNodes = 1
        krishna.store = []
        krishna.D_path = []
        krishna._flag = 0
        krishna.heuristic = heuristic
        krishna.queue = [[krishna.heuristic[1],0]]

#   DEPTH FIRST SEARCH
    def DFS(krishna,choose):
        krishna.visited_arr[choose]  = 1
        krishna.D_path.append(krishna.dict[choose+1])
        krishna.gNodes += 1
        for i in range(20):
            if((krishna.graph[choose][i] != 0 and krishna.visited_arr[i]!=1) and krishna.visited_arr[5]!=1):
                krishna._cost += krishna.graph[choose][i]
                krishna.gNodes += 1
                krishna.DFS(i)
            if(krishna.visited_arr[6]==1):
                break
    def cost(krishna):
        print(f"Path : {krishna.D_path}")
        print(f"Total number of nodes genreted are: {krishna.gNodes}")
        print(f"Depth at which node is present : {len(krishna.D_path)-1}")
        print(f"Total Cost using DFS is : {krishna._cost}")


#   DEPTH LIMIT SEARCH                                                  
    def DLS(krishna):
        if(len(krishna._stack)==0):
            return
        d = krishna._stack.pop()
        krishna.store.append(d)
        krishna.visited_arr[d[1]] = 1
        if d[1] == 5:
            return
        if(krishna.count != 3):
            krishna.count += 1
            for i in range(20):
                if(krishna.graph[d[1]][i] !=0 and krishna.visited_arr[i]!= 1):
                    krishna._stack.append([krishna.count,i])
                    krishna.gNodes += 1
            krishna.DLS()
        else:
            krishna.count = krishna._stack[len(krishna._stack)-1][0]
            krishna.DLS()
    
    def path(krishna,s,t):
        for i in krishna.store[len(krishna.store)-1::-1]:
            if(i[0]<s):
                krishna.D_path.append(krishna.dict[i[1]+1])
                t.append(i[1])
                s = i[0]
        krishna.D_path.reverse()
        t.reverse()
        for j in range(len(t)-1):
            krishna._cost = krishna._cost + krishna.graph[t[j]][t[j+1]]
        krishna.cost()


#  ITERATIVE DEEPENING DFS
    def IDDFS(krishna):
        if krishna._flag == 1:
            return
        for i in range(len(krishna._stack)):
            for j in range(20):
                if krishna._stack[i][0] == krishna.count:
                    if(krishna.graph[krishna._stack[i][1]][j] !=0 ):
                            krishna._stack.append([krishna.count+1,j])
                            if(j == 5):
                                krishna._flag = 1
                                break         
            if(krishna._flag == 1):
                break
        krishna.count += 1
        krishna.IDDFS()

    def IDDFS_path(krishna,s):
        while s!= 0:
            krishna.D_path.append(krishna.dict[s+1])
            for i in range(20):
                if(krishna.graph[s][i]!=0):
                    krishna._cost = krishna._cost + krishna.graph[s][i]
                    s = i
                    break
        krishna.D_path.append(krishna.dict[1])
        krishna.D_path.reverse()
        krishna.gNodes = len(krishna._stack)
        krishna.cost()


#   BEST FIRST SEARCH 
    def BFS(krishna):
        s = krishna.queue[0]
        while True:
            if([0,5] in krishna.queue):
                krishna.store.append([0,5])
                break
            krishna.queue.sort()
            s = krishna.queue.pop(0)
            krishna.store.append(s)
            for i in range(20):
                if(krishna.graph[s[1]][i] !=0 ):
                    krishna.queue.append([krishna.heuristic[i+1],i])
                    krishna.gNodes += 1
        for i in krishna.store:
            krishna.D_path.append(krishna.dict[i[1]+1])
            krishna.count += krishna.heuristic[i[1]+1]
        krishna.cost()
        print(f"Total heuristic cost is : {krishna.count}")

                                                                       
#   A* SEARCH ALGORITHM       
    def A_star(krishna):
        s = krishna.queue[0]
        while True:
            krishna.queue.sort()
            s = krishna.queue.pop(0)
            krishna.store.append(s)
            for i in range(20):
                if(krishna.graph[s[1]][i] !=0 ):
                    krishna.queue.append([krishna.heuristic[i+1]+krishna.graph[s[1]][i],i])
                    krishna.gNodes += 1
                    if krishna.heuristic[i+1] == 0:
                        krishna.store.append([krishna.heuristic[i+1]+krishna.graph[s[1]][i],i])
                        krishna._flag = 1
            krishna.count += 1
            if(krishna._flag == 1):
                break
        for i in krishna.store:
            krishna.D_path.append(krishna.dict[i[1]+1])
            krishna.count += krishna.heuristic[i[1]+1]
        krishna.cost()
        print(f"Total heuristic cost is : {krishna.count}")
                    

                                                                           
print("\n\n|---------------------| Depth First Search |---------------------|\n")
answer = PA_Ai(graph,visited_arr,dict,_cost,count,heuristic)
answer.DFS(0)
answer.cost()

print("\n\n|---------------------| Depth Limited Search |---------------------|\n")
visited_arr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Depth_limit = PA_Ai(graph,visited_arr,dict,_cost,count,heuristic)
Depth_limit.DLS()
Depth_limit.path(5,[])

print("\n\n|---------------------| ITERATIVE DEEPENING DFS |---------------------|\n")
iterative_DFS = PA_Ai(graph,visited_arr,dict,_cost,count,heuristic)
iterative_DFS.IDDFS()
iterative_DFS.IDDFS_path(5)

print("\n\n|---------------------| Best First Search |---------------------|\n")
BestSearch = PA_Ai(graph,visited_arr,dict,_cost,count,heuristic)
BestSearch.BFS()

print("\n\n|---------------------| A* Algorithm |---------------------|\n")
A_star = PA_Ai(graph,visited_arr,dict,_cost,count,heuristic)
A_star.A_star()
