"""
['/users/great_books/joyce.ulysses.txt', '/users/great_books/fitzgerald.the.great.gatsby.txt',
'/users/great_books/hesse.sidhartha.txt', '/users/great_books/baum.the.wizard.of.oz.txt',
 '/users/great_books/tolstoy.war.and.peace.txt', '/users/great_books/dostoyevsky.the.brothers.karamazov.txt',
 '/users/great_books/austen.pride.and.prejudice.txt', '/users/great_books/gibbon.the.decline.and.fall.of.the.roman.empire.txt',
 '/users/great_books/einstein.relativity.txt', '/users/great_books/darwin.on.the.origin.of.species.txt',
'/users/great_books/shelley.frankenstein.txt']
"""


import glob
import os

for file in glob.glob('/users/great_books/*.txt'):
    file = os.path.split(file)[1]
    file = os.path.splitext(file)[0].split('.')
    print('auth:', file[0])
    print('title:', ' '.join(file[1:]))
    print()



