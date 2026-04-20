def main():
    for i in range(1,12):
        for j in range(1,12):
            print(str(i*j).ljust(3), end=" ")
        print()

if __name__=="__main__":
    main()