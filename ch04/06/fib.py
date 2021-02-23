def fib(n):   # フィボナッチ級数をnまで書き出す
    """ nまでのフィボナッチ級数を表示する"""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(2000)
