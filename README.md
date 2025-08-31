# bpe.py
Byte Pair Encoding (BPE) in Python from scratch without any libraries.

## References
1. <a href="https://en.wikipedia.org/wiki/Byte-pair_encoding">Wikipedia: Byte Pair Encoding</a>
2. <a href="https://github.com/rasbt/LLMs-from-scratch/blob/main/ch02/05_bpe-from-scratch/bpe-from-scratch.ipynb">GitHub (rasbt): LLMs from Scratch</a>

## Build and Run
As this repository is completely written in Python 3, there is no build mechanism required.
To run, clone this Git repository, navigate to the local cloned repository and run `main.py` (where the byte pair encoding code is written in) with the Python interpreter.
```console
$ git clone github.com/BestMat/bpe.py
$ cd bpe.py
$ python3 main.py
```

## Output
Output when `main.py` is run (`$ python3 main.py`):
```console
Processed String: "Hello,Ġworld!"
Processed Tokens: [72, 101, 108, 108, 111, 44, 256, 119, 111, 114, 108, 100, 33]
Merged Tokens: [268]
Merge Dictionary: {(72, 101): 257, (257, 108): 258, (258, 108): 259, (259, 111): 260, (260, 44): 261, (261, 256): 262, (262, 119): 263, (263, 111): 264, (264, 114): 265, (265, 108): 266, (266, 100): 267, (267, 33): 268}
```

## License
This project is licensed under **MIT License**. Go to `LICENSE` for more information.