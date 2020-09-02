#(27) 후보키

from itertools import combinations

def solution(data):
    result = 0
    col_cnt=len(data[0])
    lst=list(range(0,col_cnt))
    c_lst=[]
    final=[]
    for i in range(1,col_cnt+1):
        c=combinations(lst,i)
        c_lst.extend(c)
    for i in c_lst:
        final_tmp=[]
        for row in range(0,len(data)):
            tmp_lst=[]
            for t in i:
                tmp_lst.append(data[row][t])
            final_tmp.append(tuple(tmp_lst))
        if len(set(final_tmp)) == len(data): 
            final.append(i)
    final_set=set(final)
    for i in range(0,len(final)-1):
        for j in range(i+1,len(final)):
            if set(final[i]) == set(final[i]) & set(final[j]):
                final_set.discard(final[j])

    result = len(final_set)

    return result