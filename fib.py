steps = 0

def fib(n: int):
    memoised_results = [None] * (n + 1)
    memoised_results[0] = 0
    memoised_results[1] = 1
    return memoised_fib(n, memoised_results)


def memoised_fib(n: int, memoised: [any]):
    global steps
    steps += 1
    if memoised[n] == None:
        memoised[n] = memoised_fib(n - 1, memoised) + memoised_fib(n - 2, memoised)
    
    print(f"fib({n}) = {memoised[n]}")
    return memoised[n]

# Apparently, anything above 995, will hit the maximum recursion depth this Python instance.
fib50 = fib(995)
print(f"steps: {steps}")