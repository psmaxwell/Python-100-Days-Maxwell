"""
定义和使用字典

Version: 0.1
Author: Maxwell
Date: 2024-04-30
"""

def main():
    scores = {'Maxwell': 90, 'Apple': 75, 'Alex': 86}
    print(scores['Maxwell'])
    print(scores['Alex'])
    for elem in scores:
        print('%s\t---->\t%d' % (elem, scores[elem]))
    scores['Apple'] = 65
    scores['Chris'] = 71
    scores.update(Joy=65, Tommy=85)
    print(scores)
    if 'Tommy' in scores:
        print(scores['Tommy'])
    print(scores.get('Tommy'))
    print(scores.get('Tommy', 75))
    print(scores.popitem())
    print(scores.popitem())
    print(scores.pop('Maxwell', 100))
    scores.clear()
    print(scores)

if __name__ == '__main__':
    main()