review = "서울의 봄은 황정민 배우가 만든 2023년 최고의 블랙 코미디 영화입니다."
tkn = review.split()
print(tkn)

# 생각해보니 단어 토큰화 자체가 띄어쓰기마다 split 함수를 사용해 흩어지도록 해놨기 때문에.. 사용하는 것이 맞다고 본다.

tkn_word = list(review)
print(tkn_word)