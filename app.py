from flask import Flask
import random
app = Flask(__name__)

@app.route('/')
def home():
    return 'hello'

# 1. 주문서를 만들고,
# 2. 해당 주문이 들어왔을 때 무엇을 할지 정의

@app.route('/name')
def name():
    return '최찬종'

@app.route('/hello/<name>')
def hello(name):
   # return 'hello ' + name
   # return 'hello {}'.format(name)
    return f'hello {name}'         # 오늘날 많이 사용한다.

@app.route('/square/<int:num>')
def square(num):
    # number를 제곱하여 반환
    return str(num ** 2)

@app.route('/menu')
def menu():
    foods = ['바스버거','대우식당','진가와','고갯마루']
    food = random.choice(foods)
    return food

@app.route('/lotto')
def lotto():
    winner = [3,5,12,13,33,39]
    numbers = range(1,46)
    result = random.sample(numbers, 6)

    # 만약 6개가 일치하면 -> 1등
    # 만약 5개가 일치하면 -> 3등
    # 만약 4개가 일치하면 -> 4등
    # 만약 3개가 일치하면 -> 5등

    # cnt = 0
    # for i in result:
    #     if i in winner:
    #         cnt += 1

    cnt = set(winner) & set(result) # 교집합을 뜻한다. 집합 자료형

    rank = '꽝'
    if cnt == 6:
        rank = '1등'
    elif cnt == 5:
        rank = '3등'
    elif cnt == 4:
        rank = '4등'
    elif cnt == 3:
        rank = '5등'
        
    return str(sorted(result)) + rank         # 원본은 건들이지 않고 정렬한다.
