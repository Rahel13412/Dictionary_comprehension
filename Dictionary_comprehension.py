""" Dictionary comprehension : new_dict = {new_key:new_value for item in list}
    Dictionary comprehension : {new_key: new_value for (key,value) in dict.items()}
    Dictionary comprehension : {new_key: new_value for (key,value) in dict.items() if test}                      :

"""
import random

student_names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_score = {student: random.randint(50, 100) for student in student_names}
print(student_score)  # {'Alex': 58, 'Beth': 59, 'Caroline': 89, 'Dave': 76, 'Eleanor': 52, 'Freddie': 78}

new_student_scores = {student: score + 5 for student, score in student_score.items()}
print(new_student_scores)  # {'Alex': 63, 'Beth': 64, 'Caroline': 94, 'Dave': 81, 'Eleanor': 57, 'Freddie': 83}

new_student_scores = {student: score + 5 for student, score in student_score.items() if score > 70}
print(new_student_scores)  # {'Caroline': 94, 'Dave': 81, 'Freddie': 83}

"""Dictionary Comprehension Exercise 1 """
sentence = "my name is rahel".split()
new_dict = {word: len(word) for word in sentence}
print(new_dict)  # {'my': 2, 'name': 4, 'is': 2, 'rahel': 5}

"""Dictionary Comprehension Exercise 2 """
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "saturday": 22,
    "sunday": 24

}
weather_f = {day: round((temp * (9 / 5) + 32),1) for day, temp in weather_c.items()}
print(weather_f) # {'Monday': 53.6, 'Tuesday': 57.2, 'Wednesday': 59.0, 'Thursday': 57.2, 'Friday': 69.8, 'saturday':
# 71.6, 'sunday': 75.2}

