from typing import List
arr = [1,2,3,4]
visit = [False for _ in range(len(arr))]
answer:List[int] = []

def brute_foce(count:int):
    if count == 4:
        print("End")
        return
    for i in range(len(arr)):
        if not visit[i]:
            answer.append(arr[i])
            brute_foce(count+1)
            answer.remove(arr[i])


brute_foce(4)
