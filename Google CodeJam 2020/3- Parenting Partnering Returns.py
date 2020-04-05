
class Node(object):
    sols = ''
    start = None
    end = None

    def __init__(self, sols, start, end):
        self.sols = sols
        self.start = start
        self.end = end



def inside(time, intervals):
    for interval in intervals:
        for i in range(len(interval)):
            if time[0]>interval[0] and time[0] < interval[1] or (interval[0] > time[0] and interval[0] < time [1]):
                return True
    return False


num_of_tests = int(input())
# num_of_tests = 1

A = []
for case in range(1, num_of_tests + 1):
    answer = []
    N = int(input())
    # N = 3
    sessions = [list(map(int, input().split())) for _ in range(N)]
    # sessions.sort()

    nodes = [Node([], session[0], session[1]) for session in sessions]
    print(nodes)
    answer = answer
    C_intervals = []
    J_intervals = []
    breaker = False

    for i in range (len(nodes)):
        elem = [nodes[i].start, nodes[i].end]
        if i == 0:
            answer.append("C")
            C_intervals.append(elem)
        else:
            if inside(elem, C_intervals):
                if J_intervals == []:
                    answer.append("J")
                    J_intervals.append(elem)
                else:
                    if inside(elem, J_intervals):
                        breaker = True
                    else:
                        answer.append("J")
                        J_intervals.append(elem)

            else:
                answer.append("C")
                C_intervals.append(elem)


    if breaker == False:
        answer = ''.join(answer)
    else:
        answer = "IMPOSSIBLE"
    A.append("Case #" + str(case) + ": " + str(answer))
for As in A:
    print(As)
