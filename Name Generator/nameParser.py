import csv
import random
from hyphen import Hyphenator
from hyphen.dictools import *

def syllabizeNames(nameList):
  tempList = []
  for lang in ['en_US']:
    if not is_installed(lang): install(lang)
  en_US = Hyphenator('en_US')
  for item in nameList:
    tempList.append(en_US.syllables(item))
  return tempList

def parseNames(nameFile):
  tempList = []
  csv_f = open(nameFile)
  try:
    reader = csv.reader(csv_f)
    for row in reader:
      tempList.append(row[0])
  finally:
    csv_f.close()
  return syllabizeNames(tempList)

def sample(items):
    randomIndex = random.randrange(len(items))
    return items[randomIndex]


def chooseItem(list, place):
  #just a local variable
  thirdIndex = sample(list)

  if place == 1:
    return sample(list)[0]
  elif place == 3:
    while len(thirdIndex) != 3:
      thirdIndex = sample(list)
    return thirdIndex[2]


def genName(list):
  firstPart = chooseItem(list, 1)
  secondPart = chooseItem(list, 3)
  return firstPart + secondPart

#parse the names, syllabalizing them
names = parseNames('nameDB.csv')

#longestItem = 0
#or item in names:
#  if len(item) > longestItem:
#    longestItem = len(item)
#    print(item)
#print (longestItem)

print("Welcome to the Random Name Generator by Liquid Think!")
print("Heres Your Name!:")
print(genName(names))





