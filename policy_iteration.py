y = 1
#初始化V
V = {}
for i in range(3):
    for j in range(4):
        V[(i, j)] = 0


#动作及其转化的状态的概率
actions = {
    (0,1) : {(0,1):0.8, (1,0):0.1, (-1,0):0.1},#向右
    (0, -1) : {(0, -1):0.8, (1, 0):0.1, (-1,0):0.1},#向左
    (1, 0) : {(1,0):0.8, (0,1):0.1, (0,-1):0.1},#向下
    (-1,0) : {(-1,0):0.8, (0,1):0.1, (0,-1):0.1}
}

#初始化R
R = {}
for i in range(3):
    for j in range(4):
        R[(i,j)] = {}
        for direct in actions:
            next_s = (i+direct[0], j+direct[1])
            if next_s[0]<0 or next_s[1]<0 or next_s[0]>=3 or next_s[1]>=4 or next_s==(1,1) or next_s==(1,1):
                next_s = (i,j)
            if next_s==(0,3):
                R[(i,j)][next_s] = 1
            elif next_s == (1,3):
                R[(i,j)][next_s] = -1
            else:
                R[(i,j)][next_s] = -0.03


#初始；policy
policy = {}
for i in range(3):
    for j in range(4):
        policy[(i,j)] = {}
        if (i,j) != (0,3) and (i,j)!=(1,3) and (i,j)!=(1,1):
            policy[(i,j)] = (-1,0)

def calc_q(i, j, action):
    q = 0
    for direct, pr in actions[action].items():
        next_s = (i+direct[0], j+direct[1])
        if next_s[0]<0 or next_s[1]<0 or next_s[0]>=3 or next_s[1]>=4 or next_s==(1,1):
            next_s = (i, j)
        q += (R[(i,j)][next_s] + y * V[next_s]) * pr
    return q

def update_v():
    tmp = {}
    for i in range(3):
        for j in range(4):
            if (i,j) != (1,3) and (i,j)!=(0,3) and (i,j)!=(1,1):
                action = policy[(i,j)]
                tmp[(i,j)] = calc_q(i,j,action)
            else:
                tmp[(i,j)] = V[(i,j)]
    return tmp

def converge_v(tmp, V):
    for i in range(3):
        for j in range(4):
            if(abs(tmp[(i,j)]-V[(i,j)])>0.01):
                return False
    return True

def update_policy():
    tmp = {}
    for i in range(3):
        for j in range(4):
            if (i,j) != (1,3) and (i,j)!=(0,3) and (i,j)!=(1,1):
                max_q = float("-inf")
                max_index = None

                for want_direction, true_direction in actions.items():
                    q = calc_q(i,j,want_direction)
                    if q > max_q:
                        max_q = q
                        max_index = want_direction
                tmp[(i,j)] = max_index
    return tmp

def converge_policy(tmp, policy):
    for i in range(3):
        for j in range(4):
            if (i,j) != (1,3) and (i,j)!=(0,3) and (i,j)!=(1,1):
                if tmp[(i,j)] != policy[(i,j)]:
                    return False
    return True

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

        while True:
            tmp = V
            V = update_v()
            if converge_v(tmp, V):
                break
        
        tmp_policy = policy
        policy = update_policy()
        if converge_policy(tmp_policy, policy):
            break
    
    output_result()



