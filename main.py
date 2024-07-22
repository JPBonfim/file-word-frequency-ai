from src.natural_language_processor import NLP
from src.word_counter import WordCounter


def generate_file_with_word_frequency(
    source_file: str,
    nlp_model: str,
    source_file_encoding: str = "utf8",
    output_file_encoding: str = "utf8",
    convert_words_to_base_form: bool = False,
    ignore_case: bool = False,
    ignore_proper_nouns: bool = False,
):
    """
    Given the path of an input file, generate a text file with all the words in the input file
    ordered from highest to lowest frequency. The file is generated in the directory where the program was run.

    :param source_file:
    Path to the file to be analyzed.
    :param nlp_model:
    The spaCy model to be used.
    :param source_file_encoding:
    The text encoding used in the source file. Default is "utf8".
    :param output_file_encoding:
    The encoding to be used in the output files. Default is "utf8".
    :param convert_words_to_base_form:
    If True, the program will convert all words to their base form, that is, it will not consider inflections as
    different words. Default is False.
    :param ignore_case:
    If True, the program will convert all words to lower case. Default is False.
    :param ignore_proper_nouns:
    If True, the program will not consider proper nouns as words. Default is False.
    """

    nlp = NLP(nlp_model)
    word_counter = WordCounter(
        file=source_file,
        encoding=source_file_encoding,
        natural_language_processor=nlp,
    )

    word_counter.get_file_words(
        convert_words_to_base_form=convert_words_to_base_form,
        ignore_case=ignore_case,
        ignore_proper_nouns=ignore_proper_nouns,
    )
    word_counter.count_words_frequency()
    word_counter.sort_words_by_frequency()

    with open("word_frequency.txt", "w", encoding=output_file_encoding) as file:
        for item in word_counter.words_frequency_list_sorted:
            file.write(f"{item[0]} {item[1]}\n")
