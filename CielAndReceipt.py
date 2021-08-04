for _ in range(int(input())):

    i = int(input())

    cnt=0

    if (i%2048 == 0):

        print(i//2048)

    elif (i > 2048) and (i%2048 != 0):

        while i>2048:

            cnt+=1

            i=i-2048

        cnt+=(bin(i).replace("0b","")).count("1")

        print(cnt)

    else:

        print((bin(i).replace("0b","")).count("1"))