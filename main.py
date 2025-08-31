from collections import Counter, deque

string = "Hello, world!"

# 1. Process Unencoded String:
processed_string = []

for i, char in enumerate(string):
    if char == ' ' and i != 0:
        # 'Ġ' = <space> (GPT-2 BPE Implementation):
        processed_string.append('Ġ')
    elif char != ' ':
        # Appends character to char[]:
        processed_string.append(char)

# Converts char[] to string:
processed_string = "".join(processed_string)
print(f"Processed String: \"{ processed_string }\"")

# 2. Vocab Data Set: (Array of needed UTF-8 characters)
vocab_data_set = []

for i in range(256):
    char_code = chr(i) # UTF-8 Char Code
    vocab_data_set.append(char_code)

# Add characters to vocab_data_set from processed_string:
vocab_data_set.extend(
    char for char in sorted(set(processed_string))
    if char not in vocab_data_set
)

""" C/C++ type way:
for char in sorted(set(processed_string)):
    if char not in vocab_data_set:
        vocab_data_set.extend(char)
"""

# If there is no spaces in processed_string, add to vocab_data_set manually:
if 'Ġ' not in vocab_data_set:
    vocab_data_set.append('Ġ')

# 3. Store to Dictionaries:
vocab_dict = { i: char for i, char in enumerate(vocab_data_set) } # { 123456: "bpe" }
inverse_vocab_dict = { char: i for i, char in vocab_dict.items() } # { "bpe": 123456 }

# 4. Add Special Tokens:
special_tokens = ["<|endoftext|>"]

for token in special_tokens:
    if token not in inverse_vocab_dict:
        token_id = len(vocab_data_set)
        vocab_dict[token_id] = token
        inverse_vocab_dict[token] = token_id

# 5. Lex processed_text to token ids:
token_ids = [ inverse_vocab_dict[char] for char in processed_string ]
print(f"Processed Tokens: { token_ids }")

# 6. Merge common slices: (Reference: https://en.wikipedia.org/wiki/Byte-pair_encoding)
merge_vocab_size = 1000 # This can be increased for token id array contraction
merge_vocab_dict = {} # Dictionary of all merged vocabs
for token_id in range(len(vocab_data_set), merge_vocab_size):
    pairs = Counter(zip(token_ids, token_ids[1:])) # token_ids[1:] - pops the first element (i = 0)

    if not pairs:
        break

    pair_id = max(pairs.items(), key=lambda x: x[1])[0]
    dq = deque(token_ids)
    replaced = []

    while dq:
        current = dq.popleft()

        if dq and (current, dq[0]) == pair_id:
            replaced.append(token_id)
            dq.popleft()
        else:
            replaced.append(current)

    token_ids = replaced
    merge_vocab_dict[pair_id] = token_id

print(f"Merged Tokens: { token_ids }")
print(f"Merge Dictionary: { merge_vocab_dict }")