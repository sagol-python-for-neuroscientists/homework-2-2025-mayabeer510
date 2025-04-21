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


def english_to_morse(input_file: str = "lorem.txt", output_file: str = "lorem_morse.txt):
    
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
  
