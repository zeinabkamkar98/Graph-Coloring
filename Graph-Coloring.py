import numpy as np
from sys import stdin
import copy
###############################
graph=[]
vertice_num=0
delta=0
checked_color=[]

file = stdin
# file = open("input.txt")
data=file.readlines()

###############################

def Allowed_colors(index):
    temp=[]
    
    for i in range(1,delta+2):
        if i in graph[index]:
            pass
        else:
            temp.append(i)
    
    return copy.deepcopy(temp)
            
###############################            
def change_color_path(v,color1,color2):

    for i in range(vertice_num):
        if graph[v][i] == color1:
            graph[v][i]=color2
            graph[i][v]=color2
            change_color_path(i,color2,color1)

###############################
def coloring(V1,V2):
    
    V1_color=np.array(Allowed_colors(V1))
    V2_color=np.array(Allowed_colors(V2))
    intersect=np.intersect1d(V1_color,V2_color)
    
    if len(intersect)!=0:
        graph[V1][V2]=intersect[0]
        graph[V2][V1]=intersect[0]
        
    
    else:
        if V2_color[0] in checked_color:
            change_color_path(V2,V2_color[0],V1_color[0])
            
        else:
            checked_color.append(V2_color[0])
            V3=0
            for i in range(vertice_num):
                if graph[V1][i] == V2_color[0]:
                    V3=i
                    break
                
            coloring(V1,V3)
            
        V1_color=np.array(Allowed_colors(V1))
        V2_color=np.array(Allowed_colors(V2))
        intersect=np.intersect1d(V1_color,V2_color)   

###############################            
def print_results():
    global data
    global delta
    

    color_set=set()

    for i in range(vertice_num):
        for j in range(vertice_num):
            color_set.add(graph[i][j])

    
    color_set.remove(-1)

    print(delta," ",len(color_set))

    for d in range(len(data)):
        
        if d!=0:
            node_data=data[d].split()
            print(node_data[0]," ",node_data[1]," ",graph[int(node_data[0])][int(node_data[1])])
            
###############################
def read_file():
    global data
    global delta
    global vertice_num
    
    for d in range(len(data)):
        
        node_data=data[d].split()
        
        if d==0:
            vertice_num=int(node_data[0])
            temp_list=[]
            
            for j in range(vertice_num):
                temp_list.append(-1)
            
            for i in range(vertice_num):
                graph.append(copy.deepcopy(temp_list))
                
        else:
            graph[int(node_data[0])][int(node_data[1])]=0
            graph[int(node_data[1])][int(node_data[0])]=0
    
    for i in range(vertice_num):
        m=graph[i].count(0)
        if m > delta:
            delta=m
            
###############################
def main():
    global checked_color
    
    read_file()

    for i in range(vertice_num):
        for j in range(vertice_num):
            if graph[i][j]==0:
                coloring(i,j)
                checked_color=[]
    
    print_results()

###############################   
if __name__ == "__main__":
    main()