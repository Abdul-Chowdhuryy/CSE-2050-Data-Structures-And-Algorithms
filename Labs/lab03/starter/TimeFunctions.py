import time
def time_function(func, args, n_trials = 10):
    """Returns number of seconds to run func w args"""
    t = time.time()
    func(args)
    t_other = time.time()
    counter = t_other - t
    for i in range(n_trials + 1):
        i = t_other - t
        if counter < i:
            i = counter
    return counter 
def time_function_flexible(func, args, n_trials = 10):
    """Adds middle time to a tuple"""

    t = time.time()
    func(*args)
    t_other = time.time()
    counter = t_other - t
    for i in range(n_trials + 1):
        i = t_other - t
        if counter < i:
            i = counter
    return counter 
   
    

if __name__ == '__main__':
    # Some tests to see if time_function works
    def test_func(L):
        for item in L:
            item *= 2

    L1 = [i for i in range(10**5)]
    t1 = time_function(test_func, L1)

    L2 = [i for i in range(10**6)] # should be 10x slower to operate on every item
    t2 = time_function(test_func, L2)

    print("t(L1) = {:.3g} ms".format(t1*1000))
    print("t(L2) = {:.3g} ms".format(t2*1000))