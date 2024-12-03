# .csv - comma separated value
# .txt - text file

with open('message.txt', 'r') as file:
    # file.write("I love you, Python\n")
    text = file.read()
    print(text)