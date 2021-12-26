"""Count words in a text file"""
import sys
import pandas as pd
from collections import Counter

input_file = sys.argv[1]
output_file = sys.argv[2]

#
# Read the input file
#
with open(input_file, "r") as f:
    text = f.read()

#
# Count words
#
words = text.split(" ")
counter = Counter(words)

#
# Save
#
df = pd.DataFrame.from_dict(counter, orient="index").reset_index()
df = df.rename(columns={"index": "word", 0: "count"})
df.to_csv(output_file, index=False)

