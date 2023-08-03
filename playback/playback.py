def playback():
    user_input = input("Enter a sentence: ")

    words = user_input.split()
    
    sentence_with_words = "...".join(words)
    print(sentence_with_words)

playback()