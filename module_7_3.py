class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names

    @staticmethod
    def replace_symbols(string):
        """ В строке string удалить символы из списка to_replace """
        to_replace = [
            ',', '.', '=', '!', '?', ';', ':', ' - '
        ]
        for i in to_replace:
            string = string.replace(i, '')
        return string

    def get_all_words(self):
        all_words = dict()
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                # Прочитать файл values - строка
                values = file.read()
                # Привести строку к нижнему регистру
                values = values.lower()
                # Избавиться от пунктуации
                values = self.replace_symbols(values)
                # Преобразовать строку в список из слов
                values = values.split()
                # Записать данные в словарь. Ключ - название файла,
                # значение - список из слов этого файла
                all_words[file_name] = values
        return all_words

    def find(self, word):
        dict_ = dict()
        words_in_file = self.get_all_words()
        for name, words in words_in_file.items():
            dict_[name] = words.index(word) + 1
        return dict_

    def count(self, word):
        dict_ = dict()
        words_in_file = self.get_all_words()
        for name, words in words_in_file.items():
            dict_[name] = words.count(word)
        return dict_


finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))

