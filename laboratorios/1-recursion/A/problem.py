import json


# TODO Complete!!
def reverse(text,textrev,cont):
    if cont==len(text)+1:
        return textrev
    else:
        textrev+=text[len(text)-cont]
        return reverse(text,textrev,cont+1)
        
     

textrev=""
cont=1
if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            text = test["text"]
            actual = reverse(text,textrev,cont)
            expected = test['result']
            assert actual == expected, f'Test {i} | expected: {expected}, actual: {actual}'
        print('OK!')
