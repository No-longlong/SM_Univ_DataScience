def list_max(numlist) :
    max_score = 0

    for number in numlist :
        if number > max_score :
            max_score = number

    return max_score

score_a = int(input('점수를 입력하시오'))
score_b = int(input('점수를 입력하시오'))
score_c = int(input('점수를 입력하시오'))
score_d = int(input('점수를 입력하시오'))
score_e = int(input('점수를 입력하시오'))
score_f = int(input('점수를 입력하시오'))

score = []
score += [score_a]
score += [score_b]
score += [score_c]
score += [score_d]
score += [score_e]
score += [score_f]


print(list_max(score))

