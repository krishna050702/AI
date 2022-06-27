Name:- Krishna Mundada
Roll No:- 45
Branch:- AI-ML

Your Pac-Man agent will find paths through his maze world, to reach a particular
location. Aim of the assignment is to find a path to the goal by Breadth First Search.
Show the intermediate solution and also show the final path at the end.

==>
installed a module pyamaze which gives us a random generated maze according to our dimensions 
 pip install pyamaze

so I customized the module according to my need and imported as 

from pyMaze import maze,COLOR,agent

now the main part comes the function of BFS, it will take maze,goal and start as input

then declared a list for bsearch[]
and a dict for bfsPath={}

also made two list frontier and explored which will keep track which nodes are visited and will also be helped to perform backtracking

while frontier!=[] means till frontier becomes empty
current node will pe frointer's first node  stack is used

we have check all the possibilities in the matrix in East , West , South and North direction
so it is current cell and currentcell +1 ,currentcell and currentcell -1
current-1 and currentcell

so like this way it will check in all directions around the currentnode

 now part comes to create the maze

m=maze()
goal state is predeclared (19,1)
and start state is (10,15)

we loaded a csv file which have all the matrix coordinates of the maze
the declaring a agent that is arrow and pac man on the maze by giving them colors and footprints to trace the location
tracePath function will color the visited path of the arrow




