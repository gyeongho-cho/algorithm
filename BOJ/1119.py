N = int(input())

graph = []

def to_bool(x):
  ret = []
  for i in range(len(x)):
    if x[i]=='Y':
      ret.append(1)
    else:
      ret.append(0)
  return ret

num_path = 0
for _ in range(N):
  # print(init[0])
  instance = to_bool(input())
  graph.append(instance)
  num_path += sum(instance)

num_path /=2

# print(num_path)

node_list = list(range(N))
connected_node = [0]*N

def find_connected(node, num):
    global connected_node, node_list
    
    if visit[node]:
        return
    
    visit[node] = 1
    connected_node[node]=num
    counting_nodes.append(node)
    for next_node in node_list:
        # print(next_node, node)
        # print(graph[node][next_node])
        if graph[node][next_node] == 1:
            find_connected(next_node, num)
            
    return
        
    

num = 0
if num_path < N-1:
  print(-1)
elif N==0:
  print(0)
else:
  while True:
      new_node = node_list[0]
      visit = [0]*N
      counting_nodes = []
      num+=1
      connected_node[new_node]=1
      # print('------%d--------'%num)
      find_connected(new_node, num)
      # print(node_list)
      # print(counting_nodes)
      for c in counting_nodes:
          node_list.remove(c)
      if 0==len(node_list):
          break

  # print(connected_node)
  print(max(connected_node)-1)