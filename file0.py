def normal_recursion(n):
    if n == 1:
        return 1
    else:
        return n + normal_recursion(n-1)


if __name__ == '__main__':
    normal_recursion(5)