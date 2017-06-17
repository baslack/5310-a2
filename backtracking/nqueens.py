def place(x, k ,i):
    """
    n-queens place function. Determines whether or no
    we can place a queen at a give location, depending
    on the other queens already on the board
    :type x: list[int]
    :param x: the solution vector
    :type k: int
    :param k: the queen we're trying to place
    :type i: int
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


def nqueens(x, k, n, node_count = 0, sol_count = 0, start = 1):
    """
    returns all solution vectors to the n-queens
    problem using a backtracking algorithm
    :type x: list[int]
    :param x: the solution vector
    :type k: int
    :param k: index of the queen we want to place
    :type n: int
    :param n: number of columns, rows and queens
    :type node_count: int
    :param node_count: accumulates the count of backtracking tree nodes
    :type sol_count: int
    :param sol_count: accumulates the number of solutions found
    :type start: int
    :param start: determine whether or not the non-mirror solutions
        optimization is in effect. -1, no optimization, 1, n//2 and
        start at second index, 0, n//2 and start at first index
    :rtype : dict
    :return: (node_count, sol_count)
    """

    # if start comes is with -1, skip
    #the optimization
    if start != -1:
        # no mirror optimization
        # if we're dealing with the first
        # queen to be placed, half the range
        # and offset the starting position
        # according the the passed index for start
        if k == 0:
            m = n//2
        #otherwise, iterate as normal
        else:
            start = 0
            m = n
    else:
        start = 0
        m = n

    rng = range(start, m)

    # iterate through each possible column
    for i in rng:
        # each time we test the bound, we're checking a node
        node_count += 1
        # bounding function, test can we place queen k in location i
        if place(x, k, i):
            # place the queen on the board in the tested location
            x[k] = i
            # if we have a complete solution vector, print it
            if k == n - 1:
                if n in [4,5]:
                    print(x)
                #solution found, increment the solution count
                sol_count += 1
            # else, continue backtracking for the next queen
            else:
                ret_counts = nqueens(x, k + 1, n, node_count, sol_count)
                node_count = ret_counts["node_count"]
                sol_count = ret_counts["sol_count"]
    return {"node_count":node_count, "sol_count":sol_count}


if __name__ == "__main__":
    x = list()
    n = 4
    for i in range(n):
        x.append(-1)
    print (nqueens(x, 0, n, start=-1))