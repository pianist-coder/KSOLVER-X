# KSOLVER-X
Find PrivateKey of corresponding Pubkey using random xpoint search

KSOLVER X is a tool for solving private keys in the Bitcoin ecosystem. It is designed to efficiently search for private keys that correspond to a given public key.

## Features

- There is practically no need for RAM to work
- Only for linux, because the bloom filter uses mmap
- Utilizes the secp256k1 elliptic curve python library by iceland2k14 for efficient and fast ec operations
- Leverages the Bloom filter data structure by prashnts to quickly check for potential key matches
- Supports parallel processing using multiple CPU cores for faster computation
- Provides detailed progress information, including estimated probability of finding the key

## Usage

To use KSOLVER X, you'll need to have the following dependencies installed:

- `pybloomfiltermmap3`
- `xxhash`

You can install these dependencies using pip:

```
pip install pybloomfiltermmap3 xxhash
```

Once the dependencies are installed, you can run the KSOLVER X script with the following command-line arguments:

```
python3 bloom.py <bloom_size> <bloom_filter_file> <base_file> <range> <cores>
python3 ksolverx.py <public_key> <bloom_filter_file> <base_file> <range> <num_group_keys> <cores>
```

- `<bloom_size>`: The number of random xpoints to be added to the bloom filter.
- `<public_key>`: The public key you want to find the corresponding private key for.
- `<bloom_filter_file>`: The file containing the Bloom filter data.
- `<base_file>`: The file containing the base private key information.
- `<range>`: The bit range to search for the private key.
- `<num group keys>`: Number of continuous keys in 1 group operation.
- `<cores>`: The number of CPU cores to use for parallel processing.

For example, to run the script with the following parameters:

```
python3 bloom.py 100000000 60 60.txt 60 10
python3 ksolverx.py 04ab53fd1c7651beb0ddd9a10c071ed29ff0f59bab61c72be03741c5ed3c98985b67178dc7ccece4f71966c95bc0cef0fa5c1199375ed99fdde10a5e2b7256cc56 60 60.txt 60 1000000 10
```


This create bloom filter with 100000000 xpoints and will search for the private key corresponding to the given public key, using a Bloom filter stored in the `60` file, a base private key file `60.txt`, a key range of 59-60 bits, 1000000 continuous key and 10 CPU cores.

## Run
```
█▀▄ █░░ ▄▀▄ ▄▀▄ █▄░▄█     █▀ ▀ █░░ ▀█▀ █▀▀ █▀▀▄
█▀█ █░▄ █░█ █░█ █░█░█     █▀ █ █░▄ ░█░ █▀▀ █▐█▀
▀▀░ ▀▀▀ ░▀░ ░▀░ ▀░░░▀     ▀░ ▀ ▀▀▀ ░▀░ ▀▀▀ ▀░▀▀

by pianist (Telegram: @pianist_coder | btc: bc1q0jth0rjaj2vqtqgw45n39fg4qrjc37hcw4frcz)

[+] Program started
---------------------------------------------------------------------------------------
[+] Items: 100000000
[+] Cores: 10
---------------------------------------------------------------------------------------
[100.00 M] [469.65 Kkeys] [00:03:32.92]

[+] Bloom creating complete in 213.02 sec


█░▄▀ ▄▀▀ ▄▀▄ █░░ ▐▌░▐▌ █▀▀ █▀▀▄     █░█
█▀▄░ ░▀▄ █░█ █░▄ ░▀▄▀░ █▀▀ █▐█▀     ▄▀▄
▀░▀▀ ▀▀░ ░▀░ ▀▀▀ ░░▀░░ ▀▀▀ ▀░▀▀     ▀░▀

by pianist (Telegram: @pianist_coder | btc: bc1q0jth0rjaj2vqtqgw45n39fg4qrjc37hcw4frcz)

[+] Program started
---------------------------------------------------------------------------------------
[+] Pubkey:          02AB53FD1C7651BEB0DDD9A10C071ED29FF0F59BAB61C72BE03741C5ED3C98985B
[+] Bloom items:     100000000
[+] Key range:       59 bit
[+] Cores:           10
[+] Bloom collision: 0
---------------------------------------------------------------------------------------
[2^25.58] [17.19 Mkeys] [00:00:02.91] [Prob: 0.86361100810615765155%]
[+] Bloom collision...
[2^26.42] [16.20 Mkeys] [00:00:05.56] [Prob: 1.54912678225391786668%]
[+] Core#7 solved key by addition with step f4beb6aabc588b

-----------------------------------------------------
aa6abb5226660bf
-----------------------------------------------------
```
## How it Works

KSOLVER X uses a combination of techniques to efficiently search for private keys:

1. **Bloom Filter**: The script uses a Bloom filter to quickly check if a potential private key matches the given public key. This allows the script to avoid performing expensive cryptographic operations for keys that are unlikely to match.
2. **Parallel Processing**: The script utilizes multiple CPU cores to search for private keys in parallel, significantly speeding up the computation.
3. **Incremental and Decremental Search**: The script performs both incremental and decremental searches around the base private key, increasing the chances of finding the correct key.
4. **Progress Reporting**: The script provides detailed progress information, including the estimated probability of finding the key, the current search speed, and the elapsed time.

## Donations
If you find this project useful, please consider donating to the author's Bitcoin address:

`bc1q0jth0rjaj2vqtqgw45n39fg4qrjc37hcw4frcz`
