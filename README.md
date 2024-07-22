# file-word-frequency-ai
A program to count the number of occurrences of words in a file and organize them by frequency.
Word extraction is done with natural language processing (NLP), using the [spaCy](https://spacy.io/) library.

# Usage
Before running the code, install the dependencies with:
~~~
pip install -r requirements.txt
~~~

You will also need to download a natural language processing (NLP) model from [spaCy](https://spacy.io/) that will be used
to parse the text.

The models can be consulted on this [page](https://spacy.io/usage/models#download).

Each language has different models, which can be small, medium or large. The larger the model, the greater the accuracy of the analysis, but the slower the process.

Example:
~~~
python -m spacy download en_core_web_sm
~~~

To use the program, call the function `generate_file_with_word_frequency` in the file `main.py` 
with the desired parameters. The function will generate a text file with all the words in the input file 
ordered from highest to lowest frequency. The file is generated in the directory where the program was run.

Example:
~~~python
def generate_file_with_word_frequency(
    source_file: "hamlet.epub",
    nlp_model: "en_core_web_sm",
    convert_words_to_base_form = True,
):
~~~

# Documentation
To use the program it is necessary to call just one function, `generate_file_with_word_frequency`,
whose details are explained below.

~~~python
def generate_file_with_word_frequency(
    source_file: str,
    nlp_model: str,
    source_file_encoding: str = "utf8",
    output_file_encoding: str = "utf8",
    convert_words_to_base_form: bool = False,
    ignore_case: bool = False,
    ignore_proper_nouns: bool = False
):
~~~

## Parameters
### `source_file`
Path to the file to be analyzed.
### `nlp_model`
The spaCy model to be used.
### `source_file_encoding`
The text encoding used in the source file. Default is "utf8".
### `output_file_encoding`
The encoding to be used in the output files. Default is "utf8".
### `convert_words_to_base_form`
If True, the program will convert all words to their base form, that is, it will not consider inflections as
different words. Default is False.
### `ignore_case`
If True, the program will convert all words to lower case. Default is False.
### `ignore_proper_nouns`
If True, the program will not consider proper nouns as words. Default is False.