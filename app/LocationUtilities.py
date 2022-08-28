
import pandas as pd
from GraphUtilities import Node, Edge

"""
Classe che identifica un luogo sulla mappa
Contiene le coordinate (latitudine = Y e longitudine = X)
e il nome del luogo
"""


class Location(object):

    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getName(self):
        return self.name

    def __repr__(self):
        return str(self.name)

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return (self.x == other.x) and (self.y == other.y)

    def __lt__(self, other):
        if type(self) != type(other):
            return False
        return self.x < other.getX() and self.y < other.getY()

    def __le__(self, other):
        if type(self) != type(other):
            return False
        return self.x <= other.getX() and self.y <= other.getY()

    def __hash__(self):
        return hash(str(self))


'''
Funzione per caricare i luoghi e vie da file .csv
Il file dovrà contenere per ogni riga due punti identificati da coordinate,
I punti verranno mappati in nodi, e le coppie di punti saranno unite in archi.
'''


def loadLocations(strPath):
    nodes = []
    arcs = []
    locs_csv = pd.read_csv(strPath)

    for i, l in locs_csv.iterrows():
        l1 = Node(Location(l["long1"], l["lat1"], l["Name"]))
        l2 = Node(Location(l["long2"], l["lat2"], l["Name"]))
        # Se i nodi non sono già presenti tra quelli mappati
        if l1 not in nodes:
            nodes.append(l1)
        if l2 not in nodes:
            nodes.append(l2)
        arcs.append(Edge(l1, l2, l["Length"]))

    return nodes, arcs
