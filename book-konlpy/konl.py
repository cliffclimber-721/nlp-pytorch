from konlpy.tag import Okt
okt = Okt()

sentence = "서울의 봄은 황정민 배우가 만든 2023년 최고의 블랙 코미디 영화입니다."

noun = okt.nouns(sentence)
phrase = okt.phrases(sentence)
morph = okt.morphs(sentence)
pos = okt.pos(sentence)

print("명사 :", noun)
print("구 :", phrase)
print("형태소 :", morph)
print("품사 태깅 :", pos)