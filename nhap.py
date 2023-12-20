#input
import time
with open("data.txt", "r") as file:
    N, M = map(int, file.readline().split())
    d = list(map(int, file.readline().split()))
    c = list(map(int, file.readline().split()))
    K = int(file.readline())
    conflict_classes = {i: set() for i in range(N + 1)}
    for i in range(K):
        cur = tuple(map(int, file.readline().split()))
        conflict_classes[cur[0] - 1].add(cur[1] - 1)
        conflict_classes[cur[1] - 1].add(cur[0] - 1)

start_time=time.perf_counter()
#sort rooms, retain order
sorted_c=sorted([(c[i],i+1) for i in range(M)])
change={i:sorted_c[i][1] for i in range(M)}


#add null class
N+=1
d.append(0)

#keep list of class that fits in each rooms
fit=[]
for i in range(M):
    temp=[]
    for j in range(N):
        if d[j]<=sorted_c[i][0]:
            temp.append(j)
    fit.append(temp.copy())

#check conflict
def check(slot,cl,timetable,remaining):
    if cl==N-1:
        return True
    num=slot%M
    if cl in timetable or cl not in remaining:
        return False
    for i in range(slot-num,slot):
        if timetable[i] in conflict_classes[cl]:
            return False
    return True

#greedy 1st solution:
def greedy_ans(timetable):
    remaining=[i for i in range(N-1)]
    for i in timetable:
        if i in remaining:
            remaining.remove(i)
    slot=0
    while remaining!=[]:
        picked=0
        while not check(slot,fit[slot%M][picked],timetable,remaining):
            picked+=1
        chosen=fit[slot%M][picked]
        timetable.append(chosen)
        if chosen!=N-1:
            remaining.remove(chosen)
        slot+=1
    return timetable

cur_ans=greedy_ans([])
improvement=0

final_ans=[]
for i in range(len(cur_ans)):
    final_ans.append([cur_ans[i]+1,i//M +1,change[i%M]])

for i in sorted(final_ans):
    if i[0]==N:
        break
    print(*i)


end_time = time.perf_counter()
execution_time = end_time - start_time

print(f"The code executed in {execution_time} seconds.")
mof=0
for i in range(len(cur_ans)):
    mof=max(mof,i//M+1)
print(f"Minimum of objective function: ",mof)