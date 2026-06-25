# Print a name n times
def print_n_times(name, n):
    if n == 0:
        return
    else:
        print(name)
    print_n_times(name, n-1)
