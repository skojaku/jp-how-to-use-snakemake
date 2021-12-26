"""Program to extract text from the given Wikipedia page titles"""
import sys
from transformers import pipeline

input_file = sys.argv[1]
model = sys.argv[2]
max_length = int(sys.argv[3])
output_file = sys.argv[4]

#
# Read the input file
#
with open(input_file, "r") as f:
    text = f.read()

#
# Load model
#
summarizer = pipeline("summarization", model=model, tokenizer=model)

#
# Summarize
#
summary_text = summarizer(text[:1024], min_length=5, max_length=max_length)[0][
    "summary_text"
]

#
# Save
#
with open(output_file, "w") as f:
    f.write(summary_text)
