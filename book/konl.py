from konlpy.tag import Okt
okt = Okt()

sentence = "나는 대학원생입니다."

noun = okt.nouns(sentence)
phrase = okt.phrases(sentence)
morph = okt.morphs(sentence)
pos = okt.pos(sentence)

print("명사 :", noun)
print("구 :", phrase)
print("형태소 :", morph)
print("품사 태깅 :", pos)