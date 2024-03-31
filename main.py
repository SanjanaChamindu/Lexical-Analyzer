import re

class Lexer:
    def __init__(self):
        self.tokens = {
            'IDENTIFIER': r'[A-Za-z][A-Za-z0-9-]*',
            'INTEGER': r'[0-9]+',
            'OPERATOR': r'[+<&@:=~?]+',
            'STRING': r'\\|.+\\|',
            'COMMENT': r'//.*',
            'PUNCTUATION': r'[(),]',
            'SPACES': r'\s+'
        }

    def tokenize(self, text):
        token_regex = '|'.join('(?P<%s>%s)' % pair for pair in self.tokens.items())
        for match in re.finditer(token_regex, text):
            if match.group():
                yield match.lastgroup, match.group()

with open("RPAL_Lex.txt", "r") as file:
    content = file.read()

lexer = Lexer()

tokens = list(lexer.tokenize(content))

for token in tokens:
    print(token)
