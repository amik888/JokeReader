# JokeReader.py
# 
# Reads and prints an entire joke file and the last line of a punchline file.


jokeRead = open("Joke.txt", "r")
print (jokeRead.read())
# Reads and prints the contents of the joke file

jokeRead.close()

# Read punchline file and appends a list with each line
# as an element of the list.
punchlineRead = open("punchline.txt", "r")
punchlineList = []
for line in punchlineRead:
    punchlineList.append(punchlineRead.readline())
    
punchlineRead.close()

# Prints the last element of the punchline file
print(punchlineList[-1])
