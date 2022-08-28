import math
import folium
import webbrowser

from SearchProblemUtilities import SearchProblem, Astar
from LocationUtilities import Location, loadLocations

# Per ottenere il path relativo della cartella di progetto:
import os

ROOT_DIR = os.path.dirname(os.path.dirname((os.path.abspath("amtab"))))
# File da cui caricare la mappa
MAP_FILE_PATH = ROOT_DIR + "\\utilities\\fermate.csv"

"""
Crea una mappa nella cartella corrente, dato un file .csv
E' possibile passare in input una lista di Location da contrassegnare diversamente sulla mappa
"""


def saveMap(strPath, specialLocs=[]):
    points = []
    streets = []

    points, streets = loadLocations(strPath)

    locationMap = folium.Map(location=[points[0].getValue().getY(), points[0].getValue().getX()], zoom_start=15)

    for n in points:
        if n.getValue() in specialLocs:  # Contrassegna la Location con un'icona diversa
            folium.Marker(location=[n.getValue().getY(), n.getValue().getX()], tooltip=n.getValue().getName(),
                          icon=folium.Icon(color='green', icon="fa-solid fa-train", prefix="fa")).add_to(locationMap)
        else:
            folium.Marker(location=[n.getValue().getY(), n.getValue().getX()], tooltip=n.getValue().getName()).add_to(
                locationMap)

    for a in streets:
        folium.PolyLine(locations=[(a.getFromNode().getValue().getY(), a.getFromNode().getValue().getX()),
                                   (a.getToNode().getValue().getY(), a.getToNode().getValue().getX())],
                        color='green').add_to(locationMap)

    folium.TileLayer('Stamen Terrain').add_to(locationMap)
    folium.TileLayer('Stamen Toner').add_to(locationMap)
    folium.TileLayer('Stamen Water Color').add_to(locationMap)
    folium.TileLayer('cartodbpositron').add_to(locationMap)
    folium.TileLayer('cartodbdark_matter').add_to(locationMap)
    folium.LayerControl().add_to(locationMap)

    locationMap.save("mymap.html")


"""
Mostra la mappa aprendola nel browser
"""


def showMap(strPath):
    webbrowser.open_new_tab(strPath)


"""
Dati un punto di inizio e di fine, sfrutta l'algoritmo A* per risolvere il problema di ricerca tra luoghi
nello spazio della mappa del file .csv passato in input
Restituisce il costo e salva il percorso sul file html della mappa
"""


def findLocationsPath(startLocation, goalLocation, strPath):
    # Strutture dati per il problema di ricerca
    nodes = []
    arcs = []
    start = []
    goal = None

    nodes, arcs = loadLocations(strPath)

    for n in nodes:
        # Se le coordinate coincidono con il luogo di partenza dato in input, lo salva nella struttura dati apposita
        # Controllo in più per assicurarsi che sia unico, se trovato
        if n.getValue().getX() == startLocation.getX() and n.getValue().getY() == startLocation.getY() and not start:
            start.append(n)
        # Se le coordinate coincidono con il luogo di arrivo dato in input, lo salva nella variabile
        # Controllo in più per assicurarsi che sia unico, se trovato
        if n.getValue().getX() == goalLocation.getX() and n.getValue().getY() == goalLocation.getY() and goal == None:
            goal = n

    print("Calcolo percorso da ", startLocation.getName(), " a ", goalLocation.getName())

    # Crea un problema di ricerca con i nostri dati
    sp = SearchProblem(nodes, arcs, start, goal)

    # Utilizza l'algoritmo A* per risolvere efficientemente il problema di ricerca
    result, cost = Astar(sp, heur)

    # Crea la mappa dove visualizzare il percorso, partendo dal nodo che identifica il luogo iniziale
    resultMap = folium.Map(location=[start[0].getValue().getY(), start[0].getValue().getX()], zoom_start=15)

    # Inserisce sulla mappa i vari Marker e Linee per indicare i luoghi e i percorsi
    rNodes = result.getNodes()

    # Inserisce icone specifiche per indicare il punto di partenza (in rosso) e di arrivo (in verde)
    folium.Marker(location=[rNodes[0].getValue().getY(), rNodes[0].getValue().getX()],
                  tooltip=rNodes[0].getValue().getName(),
                  icon=folium.Icon(color='red', icon="fas fa-map-pin", prefix="fa")).add_to(resultMap)
    folium.Marker(location=[rNodes[-1].getValue().getY(), rNodes[-1].getValue().getX()],
                  tooltip=rNodes[-1].getValue().getName(),
                  icon=folium.Icon(color='green', icon="fas fa-flag-checkered", prefix="fa")).add_to(resultMap)

    # Aggiunge i restanti luoghi e cammini del percorso
    for n in rNodes[1:-1]:
        folium.Marker(location=[n.getValue().getY(), n.getValue().getX()], tooltip=n.getValue().getName()).add_to(
            resultMap)

    for i in range(0, len(rNodes) - 1):
        folium.PolyLine(locations=[(rNodes[i].getValue().getY(), rNodes[i].getValue().getX()),
                                   (rNodes[i + 1].getValue().getY(), rNodes[i + 1].getValue().getX())],
                        color='red').add_to(resultMap)

    folium.TileLayer('Stamen Terrain').add_to(resultMap)
    folium.TileLayer('Stamen Toner').add_to(resultMap)
    folium.TileLayer('Stamen Water Color').add_to(resultMap)
    folium.TileLayer('cartodbpositron').add_to(resultMap)
    folium.TileLayer('cartodbdark_matter').add_to(resultMap)
    folium.LayerControl().add_to(resultMap)

    resultMap.save("resultMap.html")
    return cost


"""
Funzione euristica utilizzata per le ricerche euristiche
Nello specifico viene usata la distanza euclidea, ottimale per calcolare 
la distanza in linea d'aria in sistemi basati su coordinate
Funzione ammissibile, non sovrastima il costo effettivo della distanza
"""


def heur(a, b):
    return math.sqrt(
        (a.getValue().getX() - b.getValue().getX()) ** 2 + abs(a.getValue().getY() - b.getValue().getY()) ** 2)


station = [Location(16.872037, 41.117154, "Bari Centrale"),
           Location(16.854930850750335,41.109710989355946, "Bari Policlinico"),
           Location(16.8866559911761,41.11718821959866,"Bari Marconi"),
           Location(16.85246707708912,41.117230592349046,"Brigata Bari"),
           Location(16.879287217958307,41.117670657855406,"Bari Sud Est"),
           Location(16.897388394107338,41.11345211767091,"Bari Parco Sud"),
           Location(16.862451099949165,41.11782734770505,"Bari Quintino Sella")]
saveMap(MAP_FILE_PATH, station)



