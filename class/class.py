#!/usr/bin/python3

'''
file: class.py
name: Joshua Rodriguez
email: ewized@gmail.com
description: Design a class schedule for classes that I'm
    a student during a semester.
'''


class Schedule:
    class_id = ""
    name = ""
    times = ""

    def __init__(self, class_id, name, times):
        self.class_id = class_id
        self.name = name
        self.times = times

    def __str__(self):
        return "{0}, {1}, {2}".format(self.class_id, self.name, self.times)

classes = list()

classes.append(Schedule("CIS-101", "Intro to computer science", "T/TH 9:00am - 2:00pm"))
classes.append(Schedule("MATH-101", "Intro to mathematics", "M/W 9:00am - 2:00pm"))

print("ID, Name, Times")
for c in classes:
    print(c)