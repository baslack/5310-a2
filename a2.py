from backtracking import *

if __name__ == "__main__":
    with open("n-queens_test.csv", "w") as f:
        f.truncate()


        n_s = [4, 5, 8, 9, 10]
        # n_s = [4,5]
        for this_n in n_s:
            print("--------")
            print("n-queens, n = {0}".format(this_n))
            x = list()
            for i in range(this_n):
                x.append(None)
            # sans optimization
            print("----")
            print("no optimization")
            print("----")
            ret = nqueens(x, 0, this_n, start=-1)
            print(ret)
            f.write("{0}, {1}, {2}\n".format(this_n, ret["node_count"],  ret["sol_count"]))

            # with optimization, start at first element
            print("----")
            print("w/ optimization, start k at index 0")
            print("----")
            for i in range(this_n):
                x[i] = None
            ret = nqueens(x, 0, this_n, start=0)
            print(ret)
            f.write("{0}, {1}, {2}\n".format(this_n, ret["node_count"],  ret["sol_count"]))

            # with optimization, start at second element
            print("----")
            print("w/ optimization, start k at index 1")
            print("----")
            for i in range(this_n):
                x[i] = None
            ret = nqueens(x, 0, this_n, start=1)
            print(ret)
            f.write("{0}, {1}, {2}\n".format(this_n, ret["node_count"],  ret["sol_count"]))

            print("--------")
            print("")
