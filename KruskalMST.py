import operator
from enum import unique

def getpoint(L):
    # point갯수 파악
    point = []
    u1 = ""
    for list in L:
        u, v, weight = list
        if u1 != u:
            u1 = u
            point.append(u)
    for list in L:
        u, v, weight = list
        if v not in point:
            point.append(v)
    point_count = len(point)  # point 갯수
    print("point", point)
    return  point,point_count

def getlink_point(L, point, point_count):
    # 한 점과 연결된 점들 찾기
    link_point = []
    for i in range(0, point_count):
        link_point.append([])
        for list in L:
            u, v, weight = list
            if (point[i] == u):
                link_point[i].append(v)
            elif (point[i] == v):
                link_point[i].append(u)
    print("link_point", link_point)
    return link_point


def mst(L,point,link_point):
    # 가중치기준으로 오름차순정렬
    L.sort(key=lambda L:L[2])
    print("가중치 오름차순된 선분", L)

    T = []
    i=0
    while (len(T) < point_count):
        # L[i]를 T에 넣는다.
        T.append(L[i])
        i=i+1
        makecycle(T, link_point, point)
        # T list를 확인해서 사이클이 만들어지는지 확인한다.
        """if (makecycle(T,link_point,point)):
            T.pop(L[i])"""
        # 사이클이 만들어진다면 pop한다.
        # 그렇지 않는다면 계속 point갯수-1 한 만큼 돌도록 한다.

    print(T)
    return T

def makecycle(T,link_point,point):
    if(len(T)>2):
        """
        여기서는 사이클이 발생되는지 확인
        """
        for t_list in T:
            u,v=t_list
            if (point.index(u),point,index(v)) in :

        """for path in [T[i][0] for i in range(2, len(T))]:
            path.split("-")
            s1_index=point.index(path[0])
            s2_index=point.index(path[2])
            #link_point[s1_index].index(path[0])
            #link_point[s2_index].index(path[2])
            print(path[0],"//",path[2])
            while(link_point[s1_index].index(path[0])):
                pass
            while (link_point[s1_index].index(path[2])):
                pass """
    return



L=[("a","e",4),("a","b",8),("a","d",2),("b","d",4),("b","f",2),("b","c",1),("c","f",1),("d","f",7),("d","e",3),("e","f",9)]
print("가중치 오름차순되기 전 선분",L)

point,point_count=getpoint(L)
link_point=getlink_point(L,point,point_count)
T=mst(L,point,link_point)

print("kruskalMST :",T)