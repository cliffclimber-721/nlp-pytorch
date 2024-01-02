from nltk import tag, tokenize

sent = "Focus on making yourself better, not on thinking that you are better."

word = tokenize.word_tokenize(sent)
sents = tokenize.sent_tokenize(sent)

pos = tag.pos_tag(word)

print(word)
print(sents)
print(pos)