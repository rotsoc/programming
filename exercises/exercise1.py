def main():
    n = int(input('sum> '))
    s = 0.0
    for i in range(2, n+2):
        s += (i-1)/i
    print(round(s,2))

if __name__ == "__main__":
    main()
