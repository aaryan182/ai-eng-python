# Build a Safe File Reade Requirements: open file safely,  handle missing file,count lines, clean text, return final list, use context manager, use custom errors, return meaningful messages


class FileMissingError(Exception):
    pass

def read_clean(path):
    try:
        with open(path) as f:
            lines = f.readlines()
            return [line.strip() for line in lines]
    except FileNotFoundError:
        raise FileMissingError(f"File '{path}' not found")
    
    
try:
    data = read_clean("hello.txt")
    print(data)
except FileMissingError as e:
    print(e)