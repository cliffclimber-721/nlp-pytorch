from konlpy.tag import Kkma

kkma = Kkma()
sent = "서울의 봄은 황정민 배우가 만든 2023년 최고의 블랙 코미디 영화입니다."

noun = kkma.nouns(sent)
sents = kkma.sentences(sent)
morph = kkma.morphs(sent)
pos = kkma.pos(sent)

print("명사 :", noun)
print("문장(구문) :", sents)
print("형태소 :", morph)
print("품사 태깅 :", pos)