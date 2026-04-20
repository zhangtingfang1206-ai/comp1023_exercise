def func(x):
    x = [1,2,3]
    return x

if __name__ == "__main__":
    nums = [2,3,4]
    ret = func(nums)    # after the function, nums = [1,2,3] is killed
    print(nums)      # 2,3,4
    print(ret)       # 1,2,3
    print(ret == nums)
    print(ret is nums)


def main():
    nums = [2,3,4]
    ret = func(nums)    # after the function, nums = [1,2,3] is killed
    print(nums)      # 2,3,4
    print(ret)       # 1,2,3
    print(ret == nums)
    print(ret is nums)
if __name__ == "__main__":
    main()