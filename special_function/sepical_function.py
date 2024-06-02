from scipy import special as sp

if __name__ == '__main__':
    premutation = sp.perm(10, 3)
    print(f"Premutation -> {premutation}")

    combination = sp.comb(10, 7)
    print(f"Combination ->{combination}")

    log_sum = sp.exp10([2, 3])
    print(f"log expo-> {log_sum}")

    cube_root = sp.cbrt([8, 64])
    print(f"Cube root -> {cube_root}")
