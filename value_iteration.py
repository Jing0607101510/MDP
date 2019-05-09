#初始化V
V = {}
for i in range(3):
    for j in range(4):
        V[(i,j)] = 0

policy = {}

actions = {
    (0,1) : {(0,1):0.8, (1,0):0.1, (-1,0):0.1},#向右
    (0, -1) : {(0, -1):0.8, (1, 0):0.1, (-1,0):0.1},#向左
    (1, 0) : {(1,0):0.8, (0,1):0.1, (0,-1):0.1},#向下
    (-1,0) : {(-1,0):0.8, (0,1):0.1, (0,-1):0.1}
}

#Q与s和a相关
Q = {}
y = 1

for i in range(3):
    for j in range(4):
        Q[(i,j)] = {}
        for action in actions.keys():
            Q[(i,j)][action] = 0 #(i,j)状态，action动作

#初始化R
R = {}
for i in range(3):
    for j in range(4):
        R[(i,j)] = {}
        for action in actions:
            next_s = (i+action[0], j+action[1])
            if next_s[0]<0 or next_s[0]>=3 or next_s[1]<0 or next_s[1]>=4 or next_s==(1,1):
                next_s = (i, j)
            if next_s==(0,3):
                R[(i,j)][next_s] = 1
            elif next_s==(1,3):
                R[(i,j)][next_s] = -1
            else:
                R[(i,j)][next_s] = -0.03

def calc_q(i, j, direct_pr):
    q = 0
    for direct, pr in direct_pr.items():
        next_s = (i+direct[0], j+direct[1])
        if next_s[0]<0 or next_s[0]>=3 or next_s[1]<0 or next_s[1]>=4 or next_s==(1,1):
            next_s = (i, j)
        q += (R[(i,j)][next_s] + y * V[next_s]) * pr
    return q
        


def update_v():
    tmp = {}
    for i in range(3):
        for j in range(4):
            if (i,j)!=(0,3) and (i,j)!=(1,3) and (i,j)!=(1,1):
                max_q = float("-inf")
                for want_direct, true_direct in actions.items():
                    q = calc_q(i, j, true_direct)
                    Q[(i,j)][want_direct] = q
                    if q > max_q:
                        max_q = q
                tmp[(i,j)] = max_q
            else:
                tmp[(i,j)] = V[(i,j)]
    return tmp

def converge(tmp, V):
    for i in range(3):
        for j in range(4):
            if(abs(tmp[(i,j)]-V[(i,j)])>0.01):
                return False
    return True

def get_policy():
    for i in range(3):
        for j in range(4):
            if (i,j)!=(0,3) and (i,j)!=(1,3) and (i,j)!=(1,1):
                policy[(i,j)] = max(Q[(i,j)], key=Q[(i,j)].get)

def output_result():
    for i in range(3):
        for j in range(4):
            if (i,j)==(1,1):
                print("口",end="")
            elif (i,j)==(0,3):
                print("+1",end="")
            elif (i,j)==(1,3):
                print("-1",end="")
            else:
                if policy[(i,j)] == (0,1):
                    print("→",end="")
                elif policy[(i,j)] == (0,-1):
                    print("←",end="")
                elif policy[(i,j)] == (1,0):
                    print("↓",end="")
                else:
                    print("↑",end="")
        print()

if __name__ == "__main__":
    while True:
        tmp = V
        V = update_v()
        if converge(tmp, V):
            break
    get_policy()
    output_result()