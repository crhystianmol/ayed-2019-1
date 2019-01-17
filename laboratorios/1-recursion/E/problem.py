import json


# TODO Complete!
def super_digit(n, k):
    p=(str(n)*k)
    cont=0
    for i in p:
      
        cont+=int(i)
    if cont>=10:
        return super_digit(cont, 1)
    else:
        return cont
        
        


if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            n = test["n"]
            k = test["k"]
            actual = super_digit(n, k)
            expected = test['result']
            assert actual == expected, f'Test {i} | n: {n} | k: {k} | expected: {expected}, actual: {actual}'
        print('OK!')
