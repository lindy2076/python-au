import time
import associative, associative_jit

def main():
    associative_jit.count(1)
    t = time.time()
    k = 4
    print("This program counts associative operations on all " + str(k) + "-len sets.")
    assoc_ops = associative.count(k)
    print("default python res: " + str(assoc_ops) + " associative operations. Time:" + str(time.time() - t))
    t = time.time()
    assoc_ops = associative_jit.count(k)
    print("numba res: " + str(assoc_ops) + " associative operations. Time:" + str(time.time() - t))
    
    # k = 4: default python res: 3492 associative operations. Time:15617.335844516754
    #        numba res: 3492 associative operations. Time:680.3980700969696

if __name__ == "__main__":
    main()
