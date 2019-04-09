ending=int(input("Input the ending number : "))
if ending < 1:
    ending = int(input("Please input natural number : "))

for number in range (1, ending+1, 1):
    num=number
    log=0
    clap=0

    while 1:
        if num< 10**(log+1):
            break
        else:
            log=log+1

    for n in range(log, -1, -1):
        if num//10**n ==3 or num//10**n ==6 or num//10**n ==9:
            print("박수")
            clap=1
            num=0
        elif num >0:
            num=num - (num//10**n)*(10**n)

    if clap==0:
        print(number)
