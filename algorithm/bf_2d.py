blocks = [i + 1 for i in range(5)]

three_by_three = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#print(list(zip(*(three_by_three[0:2]))))




def bf_search(cnt=0):
    if cnt >= len(blocks):
        print(three_by_three)
        return
    for i in range(len(three_by_three)):
        for j in range(len(three_by_three[0])):
            if three_by_three[i][j] == 0:
                # try to put box -> 1. if small, just check the postion else try 4 directions
                # go into scope
                # go back to before

                if cnt < 2:
                    three_by_three[i][j] = blocks[cnt]
                    bf_search(cnt + 1)
                    three_by_three[i][j] = 0
                elif cnt == 4:  # 3*1
                    # right
                    if j + 2 < 3 and sum(three_by_three[i]) == 0:
                        three_by_three[i][j] = blocks[cnt]
                        three_by_three[i][j + 1] = blocks[cnt]
                        three_by_three[i][j + 2] = blocks[cnt]
                        bf_search(cnt + 1)
                        three_by_three[i][j] = 0
                        three_by_three[i][j + 1] = 0
                        three_by_three[i][j + 2] = 0
                    elif i + 2 < 3 and sum(list(zip(*three_by_three))[j]) == 0:  # down
                        three_by_three[i][j] = blocks[cnt]
                        three_by_three[i + 1][j] = blocks[cnt]
                        three_by_three[i + 2][j] = blocks[cnt]
                        bf_search(cnt + 1)
                        three_by_three[i][j] = 0
                        three_by_three[i + 1][j] = 0
                        three_by_three[i + 2][j] = 0
                else:  # 2*1
                    if j + 1 < 3 and sum(three_by_three[i][j:j+2]) == 0:
                        three_by_three[i][j] = blocks[cnt]
                        three_by_three[i][j + 1] = blocks[cnt]
                        bf_search(cnt + 1)
                        three_by_three[i][j] = 0
                        three_by_three[i][j + 1] = 0
                    elif i + 1 < 3 and sum(list(zip(*three_by_three[i:i+2]))[j]) == 0:  # down
                        three_by_three[i][j] = blocks[cnt]
                        three_by_three[i + 1][j] = blocks[cnt]
                        bf_search(cnt + 1)
                        three_by_three[i][j] = 0
                        three_by_three[i + 1][j] = 0

    return



bf_search()
