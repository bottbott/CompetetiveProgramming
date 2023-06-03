test_cases = int(input())
scores = list()
for i in range(test_cases):
    score = [int(input) for input in input().strip().split()]
    scores.append(score)

for l_score, r_score in scores:
    if l_score > r_score:
        score1 = (l_score - l_score)/2
        score2 = score1 - l_score
        print(f'{score1} {score2}')

    else:
        print('impossible')