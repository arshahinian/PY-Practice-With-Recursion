# Write code for algorithm 1 below

def the_final_countdown(n):
    if isinstance(n, int) and n > 0:
        print(n)
        n = n - 1
        the_final_countdown(n)
    elif n == 0:
        print("launch!")
    else:
        print(f"The argument has to be a interger above -1!: {n}")
the_final_countdown('A')
the_final_countdown(5.5)
the_final_countdown(0)
the_final_countdown(-5)
the_final_countdown(5)

