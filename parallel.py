from multiprocessing import Pool

def f(x):
    print x
    return x**2

if __name__ == '__main__':
    # 8 processors
    p = Pool(8)
    a = range(100)
    b = p.map(f, a)

