def read_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            return content
    except FileNotFoundError:
        return "File not found"

try: → attempts to execute the code that might fail.

open(filename, 'r') as f: → opens the file in read mode, f acts like a file reader object.

f.read() → reads the entire content of the file into the variable content.

return content → passes the file content back to where the function was called.

except FileNotFoundError: → if the file doesn’t exist, this block runs instead of crashing.

return "File not found" → gives a friendly message.

Basic error handling in Python.
***************************************************************************************

lines_count = len(text.splitlines())
words_count = len(text.split())
characters_count = len(text)

text.splitlines() → splits the text at each newline \n → returns a list of lines → len(...) counts the lines.

text.split() → splits the text at every whitespace (space, tab, newline) → returns a list of words → len(...) counts the words.

len(text) → counts all characters including spaces and punctuation.

Then you put these counts into a dictionary

****************************************************************************************
result = {"lines": lines_count, "words": words_count, "characters": characters_count}

return result → gives this dictionary back to the caller
