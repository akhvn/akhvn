from zipfile import ZipFile
import os
import string
import shutil
import re


class TextLoader(ZipFile):

    def __init__(self, file, path):  # file - from where to extract, path - to where
        super().__init__(file)
        self.file_in_dir = None
        self.extractall(path)
        self.path = path
        self.path_of_file = path + "\\sample\\"  # Now path to the files is stored in path
        self.iter = iter(os.listdir(self.path_of_file))

    def __enter__(self):  # Making my own context manager so that it could work with open()
        """
        ��������� ����������� � ������� ������
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        ��������� �����������.
        """
        self.close()

    def __len__(self):
        file_count = len(os.listdir(self.path_of_file))
        return file_count

    def __iter__(self):
        return self

    def normalize(self, string):
        s = re.sub(r'[^\w\s]', '', string)
        s = re.sub(r'[\n]', ' ', s)
        s = re.sub(r'  ', ' ', s)
        s = s.strip(' ').lower()
        return s

    def __getstate__(self):
        print("I'm being pickled")
        return self.__dict__

    def __del__(self):
        shutil.rmtree(self.path)

    def __next__(self):
        self.file_in_dir = next(self.iter)
        file = self.path_of_file + self.file_in_dir
        a = []
        with open(file, 'r', encoding='utf8') as f:
            for line in f:
                l = line.translate(str.maketrans('', '', string.punctuation))
                l = l.lower()
                a.append(l)

        with open(file, 'w', encoding='utf8') as f:
            f.writelines(a)

        f = open(file, 'r', encoding='utf8')
        return f


if __name__ == "__main__":
    # where_from = r'C:/Users/User/Downloads/sample.zip'
    # where_to = r'C:\Users\User\PycharmProjects\MIPTStudies\w9\Archive'
    # text_loader = TextLoader(where_from, where_to)
    # print(len(text_loader))
    # counter = 0
    # for file in text_loader:  # To see that it is working
    #     counter += 1
    # print(counter)