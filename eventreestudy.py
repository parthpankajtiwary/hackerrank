# Enter your code here. Read input from STDIN. Print output to STDOUT
def main():
    nodes_edges = raw_input().split()
    nodes = int(nodes_edges[0])
    edges = int(nodes_edges[1])
    tree = {}
    for i in xrange(1,nodes+1):
        tree[i] = [[],0]
    for i in xrange(2,nodes+1):
        edge = raw_input().split()
        for j in xrange(2):
            edge[j] = int(edge[j])
        tree[edge[1]][0].append(edge[0])
    p = 1
    d = []
    f = 0
    for i in xrange(1,nodes+1):
        if i not in d:
            if tree[i][1] == 0:
                tree[i][1] = p
            d.append(i)
            e = tree[i][0]
            for j in e:
                if j not in d:
                    tree[j][1] = tree[i][1] + 1
                    tree[j][0].append(i)
    for i in xrange(1,nodes+1):
        if tree[i][1] > f:
            f = tree[i][1]
    count = 0
    for i in xrange(f-1,0,-1):
        for j in xrange(1,nodes+1):
            if tree[j][1] == i:
                if len(tree[j][0])%2 == 0:
                    count = count+1
                    for k in tree[j][0]:
                        if k<j:
                            tree[j][0].remove(k)
                            tree[k][0].remove(j)
    print count
     
        
        
                    

if __name__ == "__main__":
    main()
