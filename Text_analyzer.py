def read_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            return content
    except FileNotFoundError:
        return "File not found"
    
def analyze_text(text):
    lines_count=len(text.splitlines())
    words_count=len(text.split())
    characters_count=len(text)
    result={"lines:":lines_count,
            "words:":words_count,
            "characaters:":characters_count}
    return result
    

def main():  
    file_path=input("Enter the file location:")
    text = read_file(file_path)
    final=analyze_text(text)
    print(final)
    
    
if __name__=="__main__":
    main()