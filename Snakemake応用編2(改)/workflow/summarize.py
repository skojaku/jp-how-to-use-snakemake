"""Program to extract text from the given Wikipedia page titles"""
import sys
from transformers import pipeline

if "snakemake" in sys.modules:
    input_file = snakemake.input["input_file"]
    output_file = snakemake.output["output_file"]
    max_length = int(snakemake.params["max_length"])
    model = snakemake.params["model"]
else:
    input_file = "../data/wiki_text.txt"
    output_file = "../data/"
    max_length = 50

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
