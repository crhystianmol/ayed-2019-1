import json


# TODO Complete!
def arrange(numbers):
    listanew=[]
    for i in numbers:
        if i%2==0:
            listanew.append(i)
    for l in numbers:
        if l%2!=0:
            listanew.append(l)
    print(listanew)
    return listanew


if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            numbers = test["numbers"]
            actual = arrange(numbers)
            expected = test['result']
            assert actual == expected, f'Test {i} | expected: {expected}, actual: {actual}'
        print('OK!')
