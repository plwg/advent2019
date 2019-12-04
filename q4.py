def main():

    times = 0
    secondTimes = 0
    for i in range(347312, 805916):
        a = i // 100000
        b = (i % 100000) // 10000
        c = (i % 10000) // 1000 
        d = (i % 1000) // 100 
        e = (i % 100) // 10 
        f = i % 10
    
        if (a == b or b == c or c == d or d == e or e == f) and (a <= b <= c <= d <= e <= f):
            times += 1
        if (a <= b <= c <= d <= e <= f) and (a == b != c or (b == c != a and b == c != d) or (c == d != e and c == d != b) or (d == e != c and d == e != f) or (e == f != d)):
            secondTimes += 1
            print(i)
    print(times, secondTimes)

    return None

if __name__ == '__main__':
    main()
