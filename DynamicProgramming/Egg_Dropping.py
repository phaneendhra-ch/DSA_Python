"""

Given 'E' eggs and 'N' floors

To-Do : Returns the high enough floor to break the eggs with minimal tries/attempts.

Formulae :

    F(N,E) = [max(F(N-X,E), F(X-1,E-1)) + 1]

    i. F(N-X,E) = The no.of floors left where the egg didn't broke.
                we are left with N-X floors and E eggs

   ii. F(X-1,E-1) = The total no.of floors remaining where the egg broke.
                 we are left with (X-1) floors and (E-1) Eggs

   Using Dynamic Programming - Bottom Up

"""

INT_MAX = 32767

def Egg_drops(N,K):

    # create a 2D Matrix
    eggfloor = [[0 for j in range(K+1)] for i in range(N+1)]

    #here the (row,col) is filled with (0,0)
    #and for X eggs can be broken from floor-1, hence (row,1) = 1
    for i in range(1,N+1):
        eggfloor[i][1] = 1
        eggfloor[i][0] = 0

    # for one egg / one egg can break from each floor
    # therefore we are simply assigning floor value to that index
    for j in range(1,K+1):
        eggfloor[1][j] = j

    for i in range(2, N + 1):
        for j in range(2, K + 1):

            eggfloor[i][j] = INT_MAX        # by default each cell consists the max value

            for x in range(1, j + 1):

                res = 1 + max(eggfloor[i-1][x-1], eggfloor[i][j-x])     #applying both (i) and (ii)
                if res < eggfloor[i][j]:
                    eggfloor[i][j] = res

    for i in range(N+1):
        for j in range(K+1):
            print(eggfloor[i][j],end=" ")
        print()

    return eggfloor[N][K]

if __name__ == '__main__':
    N = 2       # no.of eggs
    K = 5      # no. of floors
    print(f"Threshold floor that breaks all eggs with minimal attempts : {Egg_drops(N,K)}")
