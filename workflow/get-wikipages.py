"""Program to extract text from the given Wikipedia page titles"""
import wikipediaapi
import re
import sys

#
# Input & Output
#
output_file = sys.argv.pop()
page_names = sys.argv[1:]

#
# Set up wikippedia API
#
wiki_wiki = wikipediaapi.Wikipedia(
    language="en", extract_format=wikipediaapi.ExtractFormat.WIKI
)

#
# Extract page content
#
extracted_text = ""
for name in page_names:
    p_wiki = wiki_wiki.page(name)
    text = p_wiki.text
    cleaned_text = re.sub("[^a-zA-Z0-9]", " ", text)
    extracted_text += " " + cleaned_text

#
# Remove double spaces
#
extracted_text = re.sub("\s+", " ", extracted_text)

#
# Save
#
with open(output_file, "w") as f:
    f.write(extracted_text)
