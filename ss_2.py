import os
import nltk

filelist = []

for file in os.listdir("./data_in"):
    if file.endswith(".txt"):
        file = "data_in/"+file
        filelist.append(file)

print(filelist)

for file in filelist:
    try:
        f = open(file, encoding="utf-8")
    except:
        print("File not found or not readable.")
        continue

    full_text = f.read()
    f.close()

    sent_tok = nltk.sent_tokenize(full_text, language="german")
    print(file + " has been tokenized")
    filename_new = file[:-4] + "_tokenized.txt"
    print(filename_new)

    file_out = open(filename_new, "w", encoding="utf-8")
    for sentence in sent_tok:
        file_out.writelines(sentence + "\n")

    file_out.close()