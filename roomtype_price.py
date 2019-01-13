#Autor: Lukas Ludwig - s0564263

import pandas
import os
import math
import statistics
import matplotlib.pyplot as plt

print("Auswertung der Daten fuer den Datensatz von Oktober 2018")

path = os.path.dirname(__file__)
file2018 = os.path.join(path, 'listings_2018.csv')
data2018 = pandas.read_csv(file2018, sep=',')

#List mit allen Preisen
prices2018 = (data2018['price'].values)

#List mit allen Unterkunftstypen
types2018 = (data2018['room_type'].values)

#Lists im Stil: [0 - 19, 20 - 39, 40 - 59, ... , 480 - 499, >= 500]
listStrings = ['0-19€', '20-39€', '40-59€', '60-79€', '80-99€',
            '100-119€', '120-139€', '140-159€', '160-179€', '180-199€',
            '200-219€', '220-239€', '240-259€', '260-279€', '280-299€',
            '300-319€', '320-339€', '340-359€', '360-379€', '380-399€',
            '400-419€', '420-439€', '440-459€', '460-479€', '480-499€', '>=500€']

#List mit Anzahl des Auftretens der Preisintervalle (siehe oben)
#fuer den Unterkunftstyp "Entire home/apt"
listHome2018 = [0]*26
pricesHome2018 = []
#bereinigte Liste, nur Werte fuer Preis von <= 1000€
pricesHomeClean2018 = []

#List mit Anzahl des Auftretens der Preisintervalle (siehe oben)
#fuer den Unterkunftstyp "Private room"
listPriv2018 = [0]*26
pricesPriv2018 = []
#bereinigte Liste, nur Werte fuer Preis von <= 1000€
pricesPrivClean2018 = []

#List mit Anzahl des Auftretens der Preisintervalle (siehe oben)
#fuer den Unterkunftstyp "Shared room"
listShare2018 = [0]*26
pricesShare2018 = []
#bereinigte Liste, nur Werte fuer Preis von <= 1000€
pricesShareClean2018 = []

#durch alle Datensaetze iterieren
for index, price in enumerate(prices2018):
    badValue = False
    indexPrice = math.floor(price / 20)
    #>= 500
    if indexPrice > 25:
        #>= 1000
        if indexPrice > 50:
            badValue = True
        indexPrice = 25
    #alle Datensaetze mit "Entire home/apt"
    if types2018[index] == 'Entire home/apt':
        listHome2018[indexPrice] += 1
        pricesHome2018.append(price)
        if badValue == False:
            pricesHomeClean2018.append(price)
    #alle Datensaetze mit "Private room"
    elif types2018[index] == 'Private room':
        listPriv2018[indexPrice] += 1
        pricesPriv2018.append(price)
        if badValue == False:
            pricesPrivClean2018.append(price)
    #alle Datensaetze mit "Shared room"
    elif types2018[index] == 'Shared room':
        listShare2018[indexPrice] += 1
        pricesShare2018.append(price)
        if badValue == False:
            pricesShareClean2018.append(price)

print("Intervall-List fuer Entire home:", listHome2018)
print("Intervall-List fuer Private room:", listPriv2018)
print("Intervall-List fuer Shared room:", listShare2018)

print("Statistische Daten zu den Preisverteilungen nach Unterkunftstyp")
dataframeHome2018 = pandas.Series(pricesHome2018)
print("Entire home:")
print(dataframeHome2018.describe())
print(dataframeHome2018.mode()[0])

dataframePriv2018 = pandas.Series(pricesPriv2018)
print("Private room:")
print(dataframePriv2018.describe())
print(dataframePriv2018.mode()[0])

dataframeShare2018 = pandas.Series(pricesShare2018)
print("Shared room:")
print(dataframeShare2018.describe())
print(dataframeShare2018.mode()[0])


print("Bereinigte statistische Daten zu den Preisverteilungen nach Unterkunftstyp")
print("Datensaetze mit Preis >= 1000 wurden entfernt")
dataframeHomeClean2018 = pandas.Series(pricesHomeClean2018)
print("Entire home:")
print(dataframeHomeClean2018.describe())
print(dataframeHomeClean2018.mode()[0])

dataframePrivClean2018 = pandas.Series(pricesPrivClean2018)
print("Private room:")
print(dataframePrivClean2018.describe())
print(dataframePrivClean2018.mode()[0])

dataframeShareClean2018 = pandas.Series(pricesShareClean2018)
print("Shared room:")
print(dataframeShareClean2018.describe())
print(dataframeShareClean2018.mode()[0])

#   Plot für Verteilung Entire home, fuer anzeigen des plots einfach die "#" in den folgenden 4 Zeilen entfernen
#homePlot = pandas.Series(listHome2018, listStrings)
#barplot = homePlot.plot.bar()
#barplot.set_ylabel('Anzahl der Einträge')
#plt.show()

#   Plot für Verteilung Private room, fuer anzeigen des plots einfach die "#" in den folgenden 4 Zeilen entfernen
#privPlot = pandas.Series(listPriv2018, listStrings)
#barplot = privPlot.plot.bar()
#barplot.set_ylabel('Anzahl der Einträge')
#plt.show()

#   Plot für Verteilung Shared room, fuer anzeigen des plots einfach die "#" in den folgenden 4 Zeilen entfernen
#sharePlot = pandas.Series(listShare2018, listStrings)
#barplot = sharePlot.plot.bar()
#barplot.set_ylabel('Anzahl der Einträge')
#plt.show()

print("Auswertung der Daten fuer den Datensatz von Oktober 2015")

file2015 = os.path.join(path, 'listings_2015.csv')
data2015 = pandas.read_csv(file2015, sep=',')

#List mit allen Preisen
prices2015 = (data2015['price'].values)

#List mit allen Unterkunftstypen
types2015 = (data2015['room_type'].values)

#List mit Anzahl des Auftretens der Preisintervalle (siehe oben)
#fuer den Unterkunftstyp "Entire home/apt"
listHome2015 = [0]*26
pricesHome2015 = []
#bereinigte Liste, nur Werte fuer Preis von <= 1000€
pricesHomeClean2015 = []

#List mit Anzahl des Auftretens der Preisintervalle (siehe oben)
#fuer den Unterkunftstyp "Private room"
listPriv2015 = [0]*26
pricesPriv2015 = []
#bereinigte Liste, nur Werte fuer Preis von <= 1000€
pricesPrivClean2015 = []

#List mit Anzahl des Auftretens der Preisintervalle (siehe oben)
#fuer den Unterkunftstyp "Shared room"
listShare2015 = [0]*26
pricesShare2015 = []
#bereinigte Liste, nur Werte fuer Preis von <= 1000€
pricesShareClean2015 = []

#durch alle Datensaetze iterieren
for index, price in enumerate(prices2015):
    badValue = False
    indexPrice = math.floor(price / 20)
    #>= 500
    if indexPrice > 25:
        #>= 1000
        if indexPrice > 50:
            badValue = True
        indexPrice = 25
    #alle Datensaetze mit "Entire home/apt"
    if types2015[index] == 'Entire home/apt':
        listHome2015[indexPrice] += 1
        pricesHome2015.append(price)
        if badValue == False:
            pricesHomeClean2015.append(price)
    #alle Datensaetze mit "Private room"
    elif types2015[index] == 'Private room':
        listPriv2015[indexPrice] += 1
        pricesPriv2015.append(price)
        if badValue == False:
            pricesPrivClean2015.append(price)
    #alle Datensaetze mit "Shared room"
    elif types2015[index] == 'Shared room':
        listShare2015[indexPrice] += 1
        pricesShare2015.append(price)
        if badValue == False:
            pricesShareClean2015.append(price)

print("Intervall-List fuer Entire home:", listHome2015)
print("Intervall-List fuer Private room:", listPriv2015)
print("Intervall-List fuer Shared room:", listShare2015)

print("Statistische Daten zu den Preisverteilungen nach Unterkunftstyp")
dataframeHome2015 = pandas.Series(pricesHome2015)
print("Entire home:")
print(dataframeHome2015.describe())
print(dataframeHome2015.mode()[0])

dataframePriv2015 = pandas.Series(pricesPriv2015)
print("Private room:")
print(dataframePriv2015.describe())
print(dataframePriv2015.mode()[0])

dataframeShare2015 = pandas.Series(pricesShare2015)
print("Shared room:")
print(dataframeShare2015.describe())
print(dataframeShare2015.mode()[0])

#   Plot für Verteilung Entire home, fuer anzeigen des plots einfach die "#" in den folgenden 4 Zeilen entfernen
#homePlot = pandas.Series(listHome2015, listStrings)
#barplot = homePlot.plot.bar()
#barplot.set_ylabel('Anzahl der Einträge')
#plt.show()

#   Plot für Verteilung Private room, fuer anzeigen des plots einfach die "#" in den folgenden 4 Zeilen entfernen
#privPlot = pandas.Series(listPriv2015, listStrings)
#barplot = privPlot.plot.bar()
#barplot.set_ylabel('Anzahl der Einträge')
#plt.show()

#   Plot für Verteilung Shared room, fuer anzeigen des plots einfach die "#" in den folgenden 4 Zeilen entfernen
#sharePlot = pandas.Series(listShare2015, listStrings)
#barplot = sharePlot.plot.bar()
#barplot.set_ylabel('Anzahl der Einträge')
#plt.show()

'''
#Listen zu Preis pro Nacht nach Unterkunftstyp, wobei index der Preis ist und Wert an diesem
#Index die Anzahl des Auftretens dieses Preises (für den Datensatz von 2018)
listHome2018All = [0]*1001
listPriv2018All = [0]*1001
listShare2018All = [0]*1001
for index, price in enumerate(prices2018):
    if price <= 1000:
        if types2018[index] == 'Entire home/apt':
            listHome2018All[price] += 1
        elif types2018[index] == 'Private room':
            listPriv2018All[price] += 1
        elif types2018[index] == 'Shared room':
            listShare2018All[price] += 1

listSumsPrices = [0]*1001

for index in range(0, 1001):
    listSumsPrices[index] = listHome2018All[index] + listPriv2018All[index] + listShare2018All[index]

#index 0: Entire home, index 1: Private room, index 2: Shared room
listSumsTypes = [0]*3
for index in range(0, 1001):
    listSumsTypes[0] += listHome2018All[index]
    listSumsTypes[1] += listPriv2018All[index]
    listSumsTypes[2] += listShare2018All[index]

sum = listSumsTypes[0] + listSumsTypes[1] + listSumsTypes[2]
print(listSumsTypes)

chiquadrat = 0
for index in range(0, 1001):
    sumPrice = listSumsPrices[index]
    chiquadrat += ((listHome2018All[index] - (listSumsTypes[0] * listSumsPrices[index] / sum)) ** 2) / (listSumsTypes[0] * sumPrice / sum)
    print(chiquadrat)
    chiquadrat += ((listPriv2018All[index] - (listSumsTypes[1] * listSumsPrices[index] / sum)) ** 2) / (listSumsTypes[1] * sumPrice / sum)
    print(chiquadrat)
    chiquadrat += ((listShare2018All[index] - (listSumsTypes[2] * listSumsPrices[index] / sum)) ** 2) / (listSumsTypes[2] * sumPrice / sum)
    print(chiquadrat)

print(chiquadrat)
'''
