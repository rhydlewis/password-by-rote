# Password by Rote

A *very* noddy Python script that allows you to type a password repeatedly in attempt to remember it.

## Usage

1. Hash your password then add to the file password-hash.txt

Example:

    python hash.py
    Password: my simple passsword
    003c9a574fe7abe498ad265712d734dd80fabbee85a78a99e153d89a005fbfff
  
2. Run rote-password.py

Example:

    python rote-password.py
    Password: this is clearly incorrect
    Incorrect: 0/1 (0.0% success)
    
    Password: my simple password
    Correct: 1/1 (50.0% success)
    
    Password: q
    Quit

And that's it. I'm not even sure if there's much benefit in hashing a password and then saving it to a file. But, still. It works.