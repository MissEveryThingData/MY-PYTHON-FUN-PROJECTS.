def main():
    word_dictionary = {
        'leg': 'An organ in a body used for walking',
        'eye': 'An organ in a body used for seeing',
        'head': 'Is the part of the body above the neck',
    }
while True:
  word = input("enter the word: ")
  if word == "":
    break
  if word in word_dictionary:
     print(word,":", word_dictionary [word])

main()
