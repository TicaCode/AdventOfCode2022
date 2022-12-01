from typing import List

class ReadFile:
    input_lines: List

    def __init__(self, doc_name: str, split_type: str, integer: bool) -> None:
        self.doc_name = doc_name
        if split_type == 'blank_lines':
            self.split_on_blank_line(integer)
        elif split_type == 'spaces':
            self.split_on_spaces(integer)

    def split_on_spaces(self, integer: bool) -> None:
        with open(self.doc_name) as f:
            self.input_lines = [line.rstrip() for line in f]
        if integer:
            self.input_lines = [[int(y) for y in x.split(' ')] for x in self.input_lines]
        else:
            self.input_lines = [x.split(' ') for x in self.input_lines]

    def split_on_blank_line(self, integer: bool) -> None:
        with open(self.doc_name) as f:
            self.input_lines = f.read().split('\n\n')
        if integer:
            self.input_lines = [[int(x) for x in y.split('\n')] for y in self.input_lines]
        else:
            self.input_lines = [[x for x in y.split('\n')] for y in self.input_lines]

    def get_input(self) -> List:
        return self.input_lines


