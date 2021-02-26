import os
from models import Street, Input, Car
from score import calculateFinalScore
from program import solve
from collections import defaultdict

IN_FOLDER = './input/'
OUT_FOLDER = './output/'
FILE_NAMES = 'abcdef'


def fileToObject(filename):
    with open(IN_FOLDER + filename, 'r') as fin:
        lines = fin.read().splitlines()

        graph = defaultdict(list)
        streets = dict()

        D, I, S, V, F = list(map(int, lines[0].split(' ')))

        for i in range(1, S+1):
            B, E, name, L = lines[i].split(' ')
            B, E, L = int(B), int(E), int(L)
            street = Street(B, E, name, L)
            graph[E].append(street)
            streets[name] = street


        cars = []

        for i in range(S+1, S+V+1):
            street_names = lines[i].split(' ')
            street_objects = list(map(lambda name: streets[name], street_names[1:]))
            cars.append(Car(street_objects))

        return Input(D, I, S, V, F, graph, cars)


def readFiles():
    return [fileToObject(IN_FOLDER + filename) for filename in os.listdir(IN_FOLDER)]


def printScore(filename, score):
    print(f'{filename.ljust(5, " ")}: {score:,}')


def readAndTestOne(filename):
    inputObj = fileToObject(filename)
    submitToFile(inputObj, filename)


def printScores(inputs, solutions):
    scores = [calculateFinalScore(inputObj, solution)
              for inputObj, solution in zip(inputs, solutions)]
    for score, filename in zip(scores, FILE_NAMES):
        printScore(filename, score)
    print('Total:', f'{sum(scores):,}')


def submitToFile(inputObj, filepath):
    with open(OUT_FOLDER + filepath, 'w') as fout:
        fout.write(inputObj.printResult())

def submitAll(answers):
    for libs, fileName in zip(answers, FILE_NAMES):
        submitToFile(libs, OUT_FOLDER + fileName + '.txt')