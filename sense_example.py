from spelling_corrector import spelling_corrector


with open("test.txt") as f:
    text_string = f.read()
output = spelling_corrector(text_string, "english.txt")
f = open("output.txt", "w")
f.write(output)
f.close()
