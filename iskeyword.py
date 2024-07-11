import keyword

def contains_keyword(keys):
    
    keys = ["for", "let", "elif", "elseif", "cat",
        "assert", "dog", "True", "False", "deb", 
        "keys", "break", "turd", "lambda", "tae",
        "try", "poop"]
    
    for i in range(len(keys)):
        if keyword.iskeyword(keys[i]):
            print(keys[i] + " is python keyword")
        else:
            print(keys[i] + " is not a python keyword")

print(contains_keyword(0))