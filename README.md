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
python3 ksolverx.py <public_key> <bloom_filter_file> <base_file> <range> <cores>
```

- `<bloom_size>`: The number of random xpoints to be added to the bloom filter.
- `<public_key>`: The public key you want to find the corresponding private key for.
- `<bloom_filter_file>`: The file containing the Bloom filter data.
- `<base_file>`: The file containing the base private key information.
- `<range>`: The bit range to search for the private key.
- `<cores>`: The number of CPU cores to use for parallel processing.

For example, to run the script with the following parameters:

```
python3 bloom.py 5000000 50 50.txt 50 5
python3 ksolverx.py 02ae959a3b18d878940aa33aaa0fde5b8160bd51f4cf8c772f27df010af1cc2da4 50 50.txt 50 5
```

This will search for the private key corresponding to the given public key, using a Bloom filter stored in the `50` file, a base private key file `50.txt`, a key range of 49-50 bits, and 5 CPU cores.

## Run
```
█▀▄ █░░ ▄▀▄ ▄▀▄ █▄░▄█     █▀ ▀ █░░ ▀█▀ █▀▀ █▀▀▄
█▀█ █░▄ █░█ █░█ █░█░█     █▀ █ █░▄ ░█░ █▀▀ █▐█▀
▀▀░ ▀▀▀ ░▀░ ░▀░ ▀░░░▀     ▀░ ▀ ▀▀▀ ░▀░ ▀▀▀ ▀░▀▀

by pianist (Telegram: @pianist_coder | btc: bc1q0jth0rjaj2vqtqgw45n39fg4qrjc37hcw4frcz)

[+] Program started
---------------------------------------------------------------------------------------
[+] Items: 5000000
[+] Cores: 5
---------------------------------------------------------------------------------------
[5.00 M] [365.02 Kkeys] [00:00:13.70]

[+] Bloom creating complete in 13.82 sec


█░▄▀ ▄▀▀ ▄▀▄ █░░ ▐▌░▐▌ █▀▀ █▀▀▄     █░█
█▀▄░ ░▀▄ █░█ █░▄ ░▀▄▀░ █▀▀ █▐█▀     ▄▀▄
▀░▀▀ ▀▀░ ░▀░ ▀▀▀ ░░▀░░ ▀▀▀ ▀░▀▀     ▀░▀

by pianist (Telegram: @pianist_coder | btc: bc1q0jth0rjaj2vqtqgw45n39fg4qrjc37hcw4frcz)

[+] Program started
---------------------------------------------------------------------------------------
[+] Pubkey:          02AE959A3B18D878940AA33AAA0FDE5B8160BD51F4CF8C772F27DF010AF1CC2DA4
[+] Bloom items:     5000000
[+] Key range:       49 bit
[+] Cores:           5
[+] Bloom collision: 0
---------------------------------------------------------------------------------------
[2^26.52] [8.54 Mkeys] [00:00:11.24] [Prob: 57.37167666834665880060%]
[+] Bloom collision...

[+] Core#3 solved key by subtraction with step 38d9f9562f50

-----------------------------------------------------
31ca2ab2f0ccc
-----------------------------------------------------
15FgeY1wMD5dPYyFT6dRkJ88joz1VktFSg
KwDiBf89QgGbjEhKnhXJuH7LrciVrZi3qYjggYtmF5f7EXzp4Zdo
-----------------------------------------------------
[+] Complete in 11.67 sec
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
