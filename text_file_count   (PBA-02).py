file = open("sample.txt", "r")

data = file.read()

characters = len(data)
words = len(data.split())
lines = len(data.splitlines())

print("Total Characters:", characters)
print("Total Words:", words)
print("Total Lines:", lines)

file.close()
