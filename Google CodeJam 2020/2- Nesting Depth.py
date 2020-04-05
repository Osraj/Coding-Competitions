
A = []
num_of_tests = int(input())
for case in range(1, num_of_tests + 1):
    answer = []
    N = str(input())
    answer.append("(" * int(N[0]))

    for index in range(len(N)-1):
        num1 = int(N[index])
        num2 = int(N[index+1])

        answer.append(str(num1))

        if num1 > num2:
            answer.append(")" * (num1 - num2))

        if num1 < num2:
            answer.append("(" * (num2 - num1) )


    answer.append(N[-1])
    answer.append(")" * int(N[-1]))


    answer = ''.join(answer)
    # print(f'Case #{case}: {answer}')
    A.append("Case #" + case + ": " + answer)
#     A.append(f'Case #{case}: {answer}')
for As in A:
    print(As)
