# calculate expected number of throws to get a sum that is a multiple of a target number

import numpy as np

if __name__ == '__main__':
    P = np.array([[1, 2, 2, 1], [1, 1, 2, 2], [2, 1, 1, 2], [0, 0, 0, 6]])
    P = np.divide(P, 6)
    P = P.T
    x = np.array([2/6, 2/6, 1/6, 1/6])
    n_limit = 1000
    E = 1 * x[3]
    l = [x[3]]

    printout = False

    for i in range(2, n_limit):
        x = np.dot(P, x)
        if i <= 20 and printout:
            print(x)
        E += i * (x[3] - l[-1])
        l.append(x[3])

    print(l[:10])
    print(E)

    n_trials = 10000
    E_N = 0

    for i in range(n_trials):
        s = 0
        n = 0
        while True:
            s += np.random.randint(1, 6, 1)
            n += 1
            if s % 4 == 0:
                E_N += n/n_trials
                break
    print(E_N)
