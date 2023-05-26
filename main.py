import difflib
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def read_file(filename):
    with open(filename, 'r') as file:
        text = file.read()
    return text

def plagiarism(file1, file2):
    text1 = read_file(file1)
    text2 = read_file(file2)
    similarity_ratio = difflib.SequenceMatcher(None, text1, text2).ratio()

    return similarity_ratio * 100

threshold = 2
Tk().withdraw()
file_1 = askopenfilename(title="Select the first file")

file_2 = askopenfilename(title="Select the second file")

percentage = plagiarism(file_1, file_2)

if percentage >= threshold:
    print("Plagiarism Detected! Similarity Percentage: {:.2f}%".format(percentage))
else:
    print("No Plagiarism Detected. Similarity Percentage: {:.2f}%".format(percentage))
