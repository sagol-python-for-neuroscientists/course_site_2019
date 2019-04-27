import pathlib


class EnglishToMorse:
    """
    Convert a text file to Morse code file.
    One change I made to the CODE dictionary is to add
    the '\n' value to it, to account for the empty lines
    in the original text. This helps us recreate the
    text *exactly* as it was before translation to Morse.

    I've also created a miniature "pipeline" in this class,
    dividing each functionality into a short, clear function
    which does only one thing.

    Another "cool" feature shown here is the way I combine
    the two dictionaries - lower case and upper case - into
    one, using the ** operator.
    """
    def __init__(self, file):
        self.file = pathlib.Path(str(file))
        if not self.file.exists():
            raise ValueError(f"File {self.file} doesn't exist.")
        self.data = None
        CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
                'D': '-..',    'E': '.',      'F': '..-.',
                'G': '--.',    'H': '....',   'I': '..',
                'J': '.---',   'K': '-.-',    'L': '.-..',
                'M': '--',     'N': '-.',     'O': '---',
                'P': '.--.',   'Q': '--.-',   'R': '.-.',
                'S': '...',    'T': '-',      'U': '..-',
                'V': '...-',   'W': '.--',    'X': '-..-',
                'Y': '-.--',   'Z': '--..',

                '0': '-----',  '1': '.----',  '2': '..---',
                '3': '...--',  '4': '....-',  '5': '.....',
                '6': '-....',  '7': '--...',  '8': '---..',
                '9': '----.',

                ' ': '\n', '.': '.-.-.-', ',': '--..--',
                ':': '---...', "'": '.----.', '-': '-....-',
                }
        code_ord_upper = {ord(key): val for key, val in CODE.items()}
        code_ord_lower = {ord(key.lower()): val for key, val in CODE.items()}
        self.new_code = {**code_ord_lower, **code_ord_upper}

    def run(self):
        """ Main pipeline """
        self.convert()
        self.to_disk()

    def convert(self):
        """ Convert self.file to one-word-in-line Morse """
        with open(self.file) as f:
            data = f.read()
        self.data = data.translate(self.new_code)

    def to_disk(self, fname='lorem_morse.txt'):
        """ Writes self.data to the disk with filename == fname """
        try:
            with open(fname, 'w') as f:
                f.write(self.data)
        except PermissionError as e:
            print(f"Error: {e}. Data is still accessible in self.data.")


if __name__ == '__main__':
    morse = EnglishToMorse('lorem.txt')
    morse.run()

