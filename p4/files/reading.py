
# Read and print the names in the file

try:
    namesFile = open("./names.txt", "r")
    data = namesFile.read()
    print(data)
except FileNotFoundError:
    print("File was not found")

