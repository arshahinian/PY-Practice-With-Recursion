# Write code for algorithm 2 below
def print_count_up(a,z):
    if isinstance(a, int) and a > 0 and isinstance(z, int) and z > a:
        print(a)
        a = a + 1
        print_count_up(a,z)
    elif a == z:
        print(a)
        print("done!")
    else:
        print(f"The arguments need to be a interger above 0!: {a},{z}")
print_count_up('A',5)
print_count_up(5.5,5)
print_count_up(0,5)
print_count_up(-5,5)
print_count_up(1,5)