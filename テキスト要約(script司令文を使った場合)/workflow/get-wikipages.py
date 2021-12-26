"""Program to extract text from the given Wikipedia page titles"""
import wikipediaapi
import re
import sys

#
# Input & Output
#
if "snakemake" in sys.modules:
    page_name = snakemake.params["wikititle"]
    output_file = snakemake.output["output_file"]
else:
    page_name = "Sapporo"
    output_file = "../data/wikititle=Sapporo.txt"

#
# Set up wikippedia API
#
wiki_wiki = wikipediaapi.Wikipedia(
    language="en", extract_format=wikipediaapi.ExtractFormat.WIKI
)

#
# Extract page content
#
p_wiki = wiki_wiki.page(page_name)
text = p_wiki.text
cleaned_text = re.sub("[^a-zA-Z0-9.]", " ", text)
extracted_text = " " + cleaned_text

#
# Remove double spaces
#
extracted_text = re.sub("\s+", " ", extracted_text)

#
# Save
#
with open(output_file, "w") as f:
    f.write(extracted_text)
