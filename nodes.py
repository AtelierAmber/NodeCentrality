#Node Distance Search
import sys;
import collections;

true = True;
false = False;

# Because the 'f' is important!
def printf(*args) : 
  for arg in range(0, len(args)):
    #if this does not work let me know. It should though
    if(sys.version_info[0] > 2):
      print(args[arg], end="");
    else :
      print(args[arg]),
  
class Graph :
  def __init__(self):
    self.edges = {};
    
  def neighbors(self, id) :
    return self.edges[id];
    
class Queue:
  def __init__(self):
    self.elements = collections.deque()
  
  def empty(self):
    return len(self.elements) == 0
  
  def put(self, x):
    self.elements.append(x)
  
  def get(self):
    return self.elements.popleft()

def breadth_first_search(graph, start, goal):
  frontier = Queue();
  frontier.put(start);
  came_from = {};
  came_from[start] = None;
  
  while not frontier.empty():
    current = frontier.get();
    
    if current == goal:
      break;
    
    for next in graph.neighbors(current):
      if next not in came_from:
        frontier.put(next);
        came_from[next] = current;

  return came_from
  
def findDist(graph, start, goal) :
  full_path = breadth_first_search(graph, start, goal);
  
  if(goal in full_path.keys()) :
    path = [];
    curNode = goal
    pathCost = 0;
    while(curNode != start) :
      path.append(curNode);
      curNode = full_path[curNode];
      pathCost += 1;
    path.append(start);
    path.reverse();
    return pathCost;
  else : return 0;

def main() :
  nodes_f = open("nodes.csv", 'r');
  numNodes = int(nodes_f.readline());
  
  nodes = Graph();
  nodes.__init__();
  nodes.edges = {};
  for i in range(0,numNodes) :
    nodes.edges[i] = [];

  for n in nodes_f :
    node = n.split(',');
    if(int(node[1].strip()) not in nodes.edges[int(node[0])]):
      nodes.edges[int(node[0])].append(int(node[1].strip()));
  for n in nodes.edges.items() :
    printf(n[0], '-> ', n[1], '\n');
##############################################################
  while(true) :
    start = int(input("Enter the starting node (-1 to exit): "));
    if(start == -1) :
        break;
    while(true) : 
      finish = int(input("\nEnter the ending node (-1 to reselect start): "));
      if(finish == -1) :
        break;
      dist = findDist(nodes, start, finish);
      if(dist == 0) :
        printf("No path found from node ", start, " to node ", finish);
      else : printf(dist);

  nodeDists = {};
  for i in range(0, numNodes) :
    nodeDists[i] = [];
  printf(nodeDists);
  for i_n in range(0, numNodes) :
    for i_d in range(0, numNodes) :
      nodeDists[i_n].append(findDist(nodes, i_n, i_d));
  printf(nodeDists);
  
  dists_f = open("dC.csv", 'w');
  to_write = "";
  for key in range(0, numNodes) :
    to_write += "\n" + str(key);
    for nodeEdge in nodeDists[key] :
      to_write += ',' + str(nodeEdge);
  printf(to_write);
  dists_f.write(to_write);

  nodes_f.close();
  dists_f.close();
  
if __name__ == "__main__" :
  main();
  