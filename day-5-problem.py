# create a generator pipeline that reads line from file, cleans them, converts them to uppercase, streams them to console

def read_file(path):
    with open(path) as f:
        for line in f:
            yield line.strip()
            
def clean_text(lines):
    for line in lines:
        yield line.replace(",", "").replace(".", "").strip()

def upper_case(lines):
    for line in lines:
        yield line.upper()

pipeline = upper_case(clean_text(read_file("data.txt")))

for line in pipeline:
    print(line)


