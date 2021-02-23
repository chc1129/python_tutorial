def fib2(n):    # nまでのフィボナッチ級数を書き出す
    """nまでのフィボナッチ級数から成るリストを返す"""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

f100 = fib2(100)
print(f100)
