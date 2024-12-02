import tiktoken
import numpy as np

tokenizer = tiktoken.get_encoding("gpt2")

with open("LeetcodeProblemsCorpus.txt", "r") as file:
    text = file.read()

tokens = tokenizer.encode(text)

np.save("tokens.npy", tokens)

# Split into training and validation sets (90/10)
train_tokens = tokens[:int(len(tokens) * 0.9)]
val_tokens = tokens[int(len(tokens) * 0.9):]

np.save("train_tokens.npy", train_tokens)
np.save("val_tokens.npy", val_tokens)
