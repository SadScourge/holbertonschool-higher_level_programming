#!/usr/bin/env python3

import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f'Name: {self.name},\nAge: {self.age},\
              \nIs Student: {self.is_student}')

    def serialize(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        with open(filename, 'rb') as file:
            obj = pickle.load(file)
            return obj
