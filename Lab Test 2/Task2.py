def check_stream_in_corpus(corpus, stream):
    #Optimize membership checks using a senario
    # Convert the corpus list to a set for faster lookup
    corpus_set = set(corpus)
    # For each item in the stream, check if it exists in the corpus_set and return a list of boolean values
    return [item in corpus_set for item in stream]

# Take input from user
corpus = list(map(int, input("Enter corpus (space-separated integers): ").split()))
stream = list(map(int, input("Enter stream (space-separated integers): ").split()))

output = check_stream_in_corpus(corpus, stream)
print(output)