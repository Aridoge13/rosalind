def readdata(location):
    with open(location) as f:
        nodes = []
        edges = []
        for i in f:            
            if [int(i.split()[0]), int(i.split()[1])] not in edges:
                edges.append([int(i.split()[0]), int(i.split()[1])])

            for j in i.split():
                if int(j) not in nodes:
                    nodes.append(int(j))
    nodes.sort()
    
    
    return nodes, edges

def delnodes(nodes, edges):
    for i in range(len(edges)):
        if edges[i][0] not in [item for sublist in edges[:i] + edges[i+1:] for item in sublist]:
            nodes.pop(nodes.index(edges[i][0]))
        if edges[i][1] not in [item for sublist in edges[:i] + edges[i+1:] for item in sublist]:
            nodes.pop(nodes.index(edges[i][1]))
    return nodes

def Deg(nodes, edges):
    res = ''
    for i in nodes:
        temp = 0
        for j in edges:
            if i == j[0] and j[1] in nodes:
                temp += 1
            elif i == j[1] and j[0] in nodes:
                temp += 1
        res += str(temp) + ' '
    return res
    
def main():
    a,b = readdata('rosalind_deg.txt')
    a = delnodes(a, b)
    print(Deg(a, b))

main()
