x = list()

def place(k,i):
    """
    n-queens place function. Determines whether or no
    we can place a queen at a give location, depending
    on the other queens already on the board
    :param k: the queen we're trying to place
    :param i: the location we're trying to place it in
    :rtype : bool
    :return: true if we can place here, false else
    """
    j = 0
    while j <= k - 1:
        #x[j] == i, same column
        #abs test, same diagonal
        if (x[j] == i) or (abs(x[j] - i) == abs(j - k)):
            return False
        j += 1
    return True


def nqueens(k, n):
    """

    :param k: index of the queen we want to place
    :param n: number of columns, rows and queens
    :return: None
    """
    #iterate through each possible column
    for i in range(n):
        #bounding function, test can we place queen k in location i
        if place(k, i):
            #place the queen on the board in the tested location
            x[k] = i
            #if we have a complete solution vector, print it
            if k == n - 1:
                print(x)
            #else, continue backtracking for the next queen
            else:
                nqueens(k + 1, n)


if __name__ == "__main__":
    n = 4
    for i in range(n):
        x.append(-1)
    nqueens(0,n)