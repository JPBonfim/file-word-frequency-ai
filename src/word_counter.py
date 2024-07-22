import ebooklib
from bs4 import BeautifulSoup
from ebooklib import epub
from pypdf import PdfReader

from src.natural_language_processor import NLP


class WordCounter:
    def __init__(
        self,
        file: str,
        encoding: str,
        natural_language_processor: NLP,
    ):
        self.__readers = {
            "txt": self._read_text,
            "pdf": self._read_pdf,
            "epub": self._read_epub,
            "html": self._read_html,
        }
        file_extension = file.strip().split(".")[-1]
        reader = self.__readers.get(file_extension)
        if reader is None:
            raise TypeError(f"File format not supported: {file_extension}")

        self.file_name = file
        self.encoding = encoding
        self.nlp = natural_language_processor
        self.file_text = ""
        self.words = []
        self.words_frequency = {}
        self.words_frequency_list_sorted = []
        reader()
        self.nlp.read_text(self.file_text)

    def _read_text(self):
        with open(self.file_name, "r", encoding=self.encoding) as file:
            self.file_text = file.read()

    def _read_pdf(self):
        pdf_reader = PdfReader(self.file_name)
        pages = pdf_reader.pages
        for page in pages:
            self.file_text += "\n" + page.extract_text()

    def _read_epub(self):
        book = epub.read_epub(self.file_name)
        pages = book.get_items_of_type(ebooklib.ITEM_DOCUMENT)
        for page in pages:
            html_parser = BeautifulSoup(page.get_content(), "html.parser")
            self.file_text += "\n" + html_parser.get_text()

    def _read_html(self):
        self._read_text()
        html_parser = BeautifulSoup(self.file_text, "html.parser")
        self.file_text = html_parser.get_text()

    def get_file_words(
        self,
        convert_words_to_base_form: bool = False,
        ignore_case: bool = False,
        ignore_proper_nouns: bool = False,
    ):
        if convert_words_to_base_form:
            self.words = self.nlp.extract_base_words(ignore_proper_nouns)
        else:
            self.words = self.nlp.extract_words(ignore_proper_nouns)

        if ignore_case:
            for i in range(len(self.words)):
                self.words[i] = self.words[i].lower()

    def count_words_frequency(self):
        for word in self.words:
            word_frequency = self.words_frequency.get(word)
            if word_frequency is None:
                self.words_frequency[word] = 1
            else:
                self.words_frequency[word] = word_frequency + 1

    def sort_words_by_frequency(self):
        word_frequency_list = []
        for word, frequency in self.words_frequency.items():
            word_frequency_list.append([word, frequency])

        self.words_frequency_list_sorted = sorted(
            word_frequency_list, key=lambda x: x[1], reverse=True
        )
