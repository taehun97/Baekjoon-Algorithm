input_string1=input().split()
num_of_vertices=int(input_string1[0])
num_of_edges=int(input_string1[1])
start_vertice=int(input_string1[2])

edges=[[0]*num_of_vertices for i in range (num_of_vertices)]
visited_vertices=[]

for i in range (num_of_edges):
    input_string2=input().split()
    edges[int(input_string2[0])-1][int(input_string2[1])-1]=1
    edges[int(input_string2[1])-1][int(input_string2[0])-1]=1

print(edges)

# dfs
temp=start_vertice
visited_vertices.append(temp)
while(len(visited_vertices)!=num_of_vertices):
    for i in range (num_of_vertices):
        if edges[start_vertice-1][i]==1:
            edges[start_vertice-1][i]=0
            edges[i][start_vertice-1]=0
            visited_vertices.append(i+1)
            temp=i+1
            break

print(visited_vertices)

