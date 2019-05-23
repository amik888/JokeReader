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

# Reverses the list and prints the first line of the punchline
# file by printing the new first element of the list.
punchlineList.reverse()
print(punchlineList[0])