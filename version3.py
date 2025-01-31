import multiprocessing
from itertools import permutations, filterfalse
import time

NUMBERS = list(range(1, 20))
TARGET_SUM = 38

def get_sets(size):
    comb = permutations(NUMBERS, size)
    flist = filterfalse(lambda i: sum(i) != TARGET_SUM, comb)
    return set(flist)

def fives_common_center(n):
    result = set()
    fives = get_sets(5)
    flist = list(filter(lambda i: i[2] == n, fives))

    for f in flist:
        if f not in result:
            result.add(f)
    return result

def solve(n):
    all = set(range(1, 20))
    fives = list(fives_common_center(n))
    for a in range(len(fives)):
        if done.value == True:
            return False
        fa = fives[a]
        sfa = set(fa)
        for b in range(len(fives)):
            fb = fives[b]
            sfb = set(fb)
            sfab = sfa.union(sfb)
            if len(sfab) != 9:
                continue

            for c in range(len(fives)):

                fc = fives[c]
                sfc = set(fc)
                sfabc = sfab.union(sfc)
                if len(sfabc) != 13:
                    continue

                remaining = all - sfabc
                used = set()

                one = 38 - fa[0] - fc[0]
                if one > 19:
                    continue
                if one not in remaining:
                    continue
                used.add(one)

                two = 38 - fc[0] - fb[4]
                if two > 19:
                    continue
                if two in used:
                    continue
                if two not in remaining:
                    continue
                used.add(two)

                three = 38 - fb[4] - fa[4]
                if three > 19:
                    continue
                if three in used:
                    continue
                if three not in remaining:
                    continue
                used.add(three)

                four = 38 - fa[4] - fc[4]
                if four > 19:
                    continue
                if four in used:
                    continue
                if four not in remaining:
                    continue
                used.add(four)

                five = 38 - fc[4] - fb[0]
                if five > 19:
                    continue
                if five in used:
                    continue
                if five not in remaining:
                    continue
                used.add(five)

                six = 38 - fb[0] - fa[0]
                if six > 19:
                    continue
                if six in used:
                    continue
                if six not in remaining:
                    continue

                if one + fc[1] + fb[3] + three != 38:
                    continue
                if six + fb[1] + fc[3] + four != 38:
                    continue
                if one + fa[1] + fb[1] + five != 38:
                    continue
                if two + fb[3] + fa[3] + four != 38:
                    continue
                if six + fa[1] + fc[1] + two != 38:
                    continue
                if five + fc[3] + fa[3] + three != 38:
                    continue

                print("Solution Found")
                display_hex(fa, fb, fc, (one, two, three, four, five, six))
                done.value = True
                return True
    return False

def display_hex(a, b, c, rest):
    print(f'    {c[0]}  {rest[1]}  {b[4]}  ')
    print(f'  {rest[0]}   {c[1]}   {b[3]}   {rest[2]} ')
    print(f'{a[0]}   {a[1]}   {a[2]}   {a[3]}   {a[4]}')
    print(f'  {rest[5]}   {b[1]}   {c[3]}   {rest[3]} ')
    print(f'    {b[0]}  {rest[4]}  {c[4]}  ')

def init_pool_processes(shared_value):
    global done
    done = shared_value

if __name__ == '__main__':
    from ctypes import c_bool
    done = multiprocessing.Value(c_bool, False)
    pool = multiprocessing.Pool(initializer=init_pool_processes, initargs=(done,), processes=3)

    start = time.time()
    solved = pool.map(solve, range(1, 20))
    end = time.time()
    elapsed = (end - start)

    elapsed_mins = int(elapsed // 60)
    elapsed_secs = int(elapsed % 60)

    print(f'{elapsed_mins} mins {elapsed_secs} secs')
