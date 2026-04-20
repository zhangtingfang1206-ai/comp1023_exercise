from itertools import count    #writing for loop in a infinite way

def main():
    for i in count():
        print("comp 1023 is a python cource")
        if i >= 10: # you can still stop the loop yourself
            break       #run 10 times

if __name__=="__main__":
    main()