# import time
#
# current_time = time.time()
#
#
# # print(current_time)  # seconds since Jan 1st, 1970
#
# def speed_calc_decorator(function):
#     def wrapper_function():
#         beforetime = time.time()
#         function()
#         aftertime = time.time()
#         execution_time = aftertime - beforetime
#         print(execution_time)
#
#     return wrapper_function
#
#
# @speed_calc_decorator
# def fast_function():
#     for i in range(1000000):
#         i * i
#
# @speed_calc_decorator
# def slow_function():
#     for i in range(10000000):
#         i * i
#
# fast_function()
# slow_function()

# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route('/')
# def hello():
#     return "Hello World"
#
# @app.route('/bye')
# def bye():
#     return "bye"
#
# if __name__ == '__main__':
#     app.run()

# -------------------------------Higher-Lower URLs-----------------------------------

from flask import Flask
import random


random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/l1KVaj5UcbHwrBMqI/giphy.gif?cid=82a1493b7htyope04ijf4j27ihb47dpytkxwgfiexs0pbeh6&ep=v1_gifs_trending&rid=giphy.gif&ct=g'/>"


@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_number:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3X5C68GcAnI7m/giphy.gif?cid=82a1493b7htyope04ijf4j27ihb47dpytkxwgfiexs0pbeh6&ep=v1_gifs_trending&rid=giphy.gif&ct=g'/>"

    elif guess < random_number:
        return "<h1 style='color: red'>Too low, try again!</h1>"\
               "<img src='https://media.giphy.com/media/jnQYWZ0T4mkhCmkzcn/giphy.gif?cid=82a1493btxycncspmn4fb90zdtald1fkxrmxxi4kivb27olt&ep=v1_gifs_trending&rid=giphy.gif&ct=g'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/xTiN0CNHgoRf1Ha7CM/giphy.gif?cid=82a1493btxycncspmn4fb90zdtald1fkxrmxxi4kivb27olt&ep=v1_gifs_trending&rid=giphy.gif&ct=g'/>"


if __name__ == '__main__':
    app.run()