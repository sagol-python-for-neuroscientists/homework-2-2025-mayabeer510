MORSE_CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
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

              '.': '.-.-.-', ',': '--..--', ':': '---...',
              "'": '.----.', '-': '-....-',
              }


def english_to_morse(input_file: str = "lorem.txt", output_file: str = "lorem_morse.txt"):

    # Read the file
    with open(input_file, 'r') as file:
        text = file.read()

    text = text.upper()
    words = text.split()    
    
    # Convert to morse
    morse_words = []
    for word in words:
        morse_chars = []
        for char in word:
            if char in MORSE_CODE:
                morse_chars.append(MORSE_CODE[char])
        morse_word = ''.join(morse_chars)
        morse_words.append(morse_word)

    morse_result = '\n'.join(morse_words)

    # Write the file
    with open(output_file, 'w') as file:
        file.write(morse_result)

if __name__ == "__main__":
    english_to_morse("lorem.txt", "lorem_morse.txt")

# test

""" Tests for question 1 - Morse code translator """
from pathlib import Path

OUTPUT_FILE_NAME = "lorem_morse.txt"
OUTPUT_PATH = Path(__file__).parent / OUTPUT_FILE_NAME


def test_file_exists():
    assert OUTPUT_PATH.exists()


def test_file_valid():
    data = Path(OUTPUT_FILE_NAME).read_text()
    assert data.count("-") == 2748
    assert data.count(".") == 4175
    assert data.count("\n") == 453


def test_individual_lines():
    with open(OUTPUT_FILE_NAME) as f:
        data = f.readlines()
    assert len(data) == 454
    assert data[-1] == ".-....--.-.-..-....-.-.-"
    assert data[3].startswith(".....-")


if __name__ == "__main__":
    methods = ["test_file_exists", "test_file_valid", "test_individual_lines"]
    errors = []

    for method in methods:
        try:
            eval(method)()
        except AssertionError as e:
            errors.append(f"Failed when testing method 'test_{method}': {e}")
            break

    if errors:
        raise AssertionError(errors)
    else:
        print("Tests pass successfully.")
        

