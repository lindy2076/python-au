import time
import associative, associative_jit


def main():
    associative_jit.count(1)
    t = time.time()
    k = 3
    assoc_ops = associative.count(k)
    print("This program counts associative operations on all " + str(k) + "-len sets.")
    print("default python res: " + str(assoc_ops) + " associative operations. Time:" + str(time.time() - t))
    '''для k = 4 обрабатывается где-то 100000 таблиц в секунду, 
       таблиц около 4 млрд, значит около 11 часов должно считать.'''
    t = time.time()
    assoc_ops = associative_jit.count(k)
    print("numba res: " + str(assoc_ops) + " associative operations. Time:" + str(time.time() - t))


if __name__ == "__main__":
    main()
