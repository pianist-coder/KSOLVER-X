#-------------------------------------------------------------------------
# Name:        KSOLVER X
# Author:      pianist (Telegram: @pianist_coder)
# Credit:      iceland
# Created:     24.05.2024
# Copyright:   (c) pianist 2022-2024
#-------------------------------------------------------------------------

import sys, time, xxhash, pybloomfilter, os
import secp256k1 as btc
import random
from multiprocessing import Event, Process, Queue, Value, cpu_count
from math import log2

#=========================================================================
splash = """
█░▄▀ ▄▀▀ ▄▀▄ █░░ ▐▌░▐▌ █▀▀ █▀▀▄     █░█ 
█▀▄░ ░▀▄ █░█ █░▄ ░▀▄▀░ █▀▀ █▐█▀     ▄▀▄ 
▀░▀▀ ▀▀░ ░▀░ ▀▀▀ ░░▀░░ ▀▀▀ ▀░▀▀     ▀░▀ 
"""
sp = """
-----------------------------------------------------
{0:x}
-----------------------------------------------------
{1}
{2}
-----------------------------------------------------"""
#=========================================================================
class color:
    GREEN = "\033[32m"
    RED = "\033[31m"
    X = "\033[5m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"
#=========================================================================
k, blname, basefile, rng, c = sys.argv[1:]

bloom = pybloomfilter.BloomFilter.open(blname)
a = btc.pub2upub(k)
l = bloom.capacity
st = time.time()
rng = int(rng)
c = int(c)
start = 2 ** (rng - 1)
end = 2 ** rng - 1
#=========================================================================

def p_2(num):
    return f'{log2(num):.2f}'

def pr(fc):
    os.system("cls||clear")
    printc(color.GREEN, splash)
    printc(color.RED, "by pianist (Telegram: @pianist_coder | btc: bc1q0jth0rjaj2vqtqgw45n39fg4qrjc37hcw4frcz)")
    printc(color.BOLD, "\n[+] Program started")
    print("-"*87)
    print(f"[+] Pubkey:          {btc.point_to_cpub(a).upper()}")
    print(f"[+] Bloom items:     {l}")
    print(f"[+] Key range:       {rng - 1} bit")
    print(f"[+] Cores:           {c}")
    print(f"[+] Bloom collision: {fc}")
    print("-"*87)

def printc(colors, message):
    print(colors + message + color.END)
    
def speedup_prob(st, counter, l, rng):
    elapsed_time = time.time() - st
    speed = counter / elapsed_time
    prob = 100 * (1 - (1 - l / 2 ** (rng - 1)) ** counter)
    print(f"[2^{p_2(counter)}] [{scan_str(speed)}keys] [{display_time(elapsed_time)}] [Prob: {prob:.20f}%]     ", end="\r")

def scan_str(num):
    suffixes = ["", "K", "M", "B", "T"]
    exponent = 0
    while abs(num) >= 1000 and exponent < 4:
        num /= 1000
        exponent += 1
    return f"{num:.2f} {suffixes[exponent]}"

def display_time(seconds):
    hours, rem = divmod(seconds, 3600)
    minutes, seconds = divmod(rem, 60)
    return f"{int(hours):02d}:{int(minutes):02d}:{seconds:05.2f}"

def find(word, file):
    with open(file, "r") as f:
        for line in f:
            if word in line:
                return int(line.split(";")[0], 16)
    return None

def chunks(s):
    for start in range(0, 66560, 65):
        yield s[start : start + 65]

def key_solver(cores="all"):
    available_cores = cpu_count()
    if cores == "all": cores = available_cores
    elif 0 < int(cores) <= available_cores: cores = int(cores)
    else: cores = 1
    counter = Value("Q")
    fc = Value("L")
    match = Event()
    queue = Queue()
    workers = []
    for r in range(cores):
        p = Process(target=solve_keys, args=(counter, fc, match, queue, r))
        workers.append(p)
        p.start()
    for worker in workers:
        worker.join()
    private_key = queue.get()
    print(sp.format(private_key, btc.privatekey_to_address(0, True, private_key), btc.btc_pvk_to_wif(private_key)))
    printc(color.BOLD, f"[+] Complete in {time.time() - st:.2f} sec")

def solve_keys(counter, fc, match, queue, r):
    while not match.is_set():
        step = random.randint(2**(rng-5), 2**(rng-4))
     #   step = random.randint(2**(rng-6), 2**(rng-5)) ### do not go beyond the range
        a_ = btc.point_subtraction(a, btc.scalar_multiplication(step))
     #   with open('possible.txt', 'a') as found: ### you may save result xpoints for future
     #       found.write(f'{a_.hex()[2:66]} # + {step:x}\n')
        with counter.get_lock():
            counter.value += 2048
        for i1, item in enumerate(chunks(btc.point_sequential_increment(1024, a_))):
            if item in bloom:
                process_collision(item, i1 + 1, counter, fc, match, queue, r, basefile, "addition", step)
                if match.is_set(): return
        for i2, item in enumerate(chunks(btc.point_sequential_decrement(1024, a_))):
            if item in bloom:
                process_collision(item, i2 + 1, counter, fc, match, queue, r, basefile, "subtraction", step)
                if match.is_set(): return
        if counter.value % 1000000 == 0:
            speedup_prob(st, counter.value, l, rng)

def process_collision(item, i, counter, fc, match, queue, r, basefile, sign, step):
    with counter.get_lock():
        fc.value += 1
    printc(color.BOLD, "\n[+] Bloom collision...")
    p1 = find(xxhash.xxh64(item).hexdigest(), basefile)
    if p1:
        offset = p1 - i + step if sign == "addition" else p1 + i + step
        with open('FOUND.txt', 'a') as found:
            found.write(f'{a.hex()};{offset:x}\n')
        printc(color.BOLD, f"\n[+] Core#{r} solved key by {sign} with step {step:x}")
        match.set()
        queue.put_nowait(offset)
    else:
        printc(color.BOLD, "\n[+] The key is not found...\n")
        pr(fc.value) 

#=========================================================================
pr(0)
key_solver(cores=c)

'''

use:

pip install pybloomfiltermmap3
pip install xxhash
python3 ksolverx.py 030c7557639c597ba58ab73d9e4f78621e14a247ed805c215b8dbfa085a0ad8487 60 60.txt 60 10

'''
