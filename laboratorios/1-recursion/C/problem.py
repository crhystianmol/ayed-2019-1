import json


# TODO Complete!
def has_more_vowels(s,vocales):
    numvoc=0
    
    for i in s:
        for k in vocales:
            if str.lower(k)==str.lower(i):
                numvoc+=1
    
    if numvoc > len(s)-numvoc:
        return True
    else:
        return False
        
    

vocales=["a","e","i","o","u"]
if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            s = test["s"]
            actual = has_more_vowels(s,vocales)
            expected = test['result']
            assert actual == expected, f'Test {i} | expected: {expected}, actual: {actual}'
        print('OK!')
