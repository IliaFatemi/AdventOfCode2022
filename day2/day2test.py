from day2 import RoundVerdict, userScoreRule

assert RoundVerdict('A', 'Y') == 6
assert RoundVerdict('B', 'X') == 0
assert RoundVerdict('C', 'Z') == 3

assert userScoreRule('X') == 1
assert userScoreRule('Y') == 2
assert userScoreRule('Z') == 3