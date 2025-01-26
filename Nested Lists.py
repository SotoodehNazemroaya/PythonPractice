#https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == '__main__':
    students = []
    scores = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append((name, score)) 
        scores.add(score)  

    second_lowest_score = sorted(scores)[1]

    result = [s[0] for s in students if s[1] == second_lowest_score]
    for name in sorted(result):
        print(name)
