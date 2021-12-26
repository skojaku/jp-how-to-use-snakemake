from os.path import join 


WIKI_PAGE_TITLE = "Sapporo"
TEXT_DATA = join("data", "wiki_text.txt")
WORD_COUNT_DATA = join("data", "word_count.csv")
WORD_COUNT_FIG = join("figs", "word_count.pdf")


rule all:
    input:
        WORD_COUNT_FIG
       
rule retrieve_wiki_text:
    output:
        TEXT_DATA
    shell:
        "python workflow/get-wikipages.py {WIKI_PAGE_TITLE} {output}"

        
rule word_count:
    input:
        TEXT_DATA
    output:
        WORD_COUNT_DATA
    shell:
        "python workflow/count-words.py {input} {output}"
       

rule plot_word_count:
    input:
        WORD_COUNT_DATA
    output:
        WORD_COUNT_FIG
    shell:
        "python workflow/plot-word-frequency.py {input} {output}"
