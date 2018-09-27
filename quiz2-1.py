def ngram_probs(filename='raw_sentences.txt'):
    f = open(filename, 'r')
    str=f.read().lower()
    str=str.split()
    print(str)
    for index in range(len(str)):
        count=0

    return bigram_probs, trigram_probs




cnt2, cnt3 = ngram_probs()
#print(cnt2[('we', 'are')])
