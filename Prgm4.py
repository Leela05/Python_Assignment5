# Write a Python program to copy the contents of a file to another file

with open("First.txt") as f:
    with open("second.txt", "w") as f1:
        for text in f:
            f1.write(text)