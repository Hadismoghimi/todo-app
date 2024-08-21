# from modules.functions import:
#
# nr_of_periods = count("Trees are good. Grass is green.")
# print(nr_of_periods)
#
#
# functions.py:
#
# def count(phrase):
#     return phrase.count('.')



# from modules.functions import:
#   nr_of_periods = functions.count("Trees are good. Grass is green.")
# print(nr_of_periods)
#
#
# functions.py:
#
# def count(phrase):
#     return phrase.count('.')




# import functions.py:
#
# nr_of_periods = functions.count("Trees are good. Grass is green.")
# print(nr_of_periods)
#
#
# functions.py:
#
# def count(phrase):
#     return phrase.count('.')

def calculate_time(h, g=9.80665):
    t = (2 * h / g)** 0.5
    return t

time = calculate_time(100,10)
print(time)