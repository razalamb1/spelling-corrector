from spelling_corrector import spelling_corrector


with open("text_files/test.txt") as f:
    text_string = f.read()
output = spelling_corrector(text_string, "text_files/english.txt")
f = open("text_files/output.txt", "w")
f.write(output)
f.close()
