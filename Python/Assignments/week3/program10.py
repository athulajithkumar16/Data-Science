ip = list(map(int, input().split()))
print(ip)

for i in range(5):
    ip[-1] = ip[-1] + 1
    if ip[-1] == 256:
        ip[-1] = 0
        ip[-2] += 1

        if ip[-2] == 256:
            ip[-2] = 0
            ip[-3] += 1

            if ip[-3] == 256:
                ip[-3] = 0
                ip[-4] += 1

                if ip[-4] == 256:
                    print('IP address out of range')
                    break  

    print(ip)