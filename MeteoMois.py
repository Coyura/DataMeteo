import numpy as np
import matplotlib.pyplot as plt

# charger un tableau de données :
data = np.loadtxt(open("dataMeteo.csv", "r"), delimiter=";", skiprows=2)

# récupérer les 3 premières colonnes du tableau de données:

jours=data[:,0]
tempMax=data[:,1]
tempMin=data[:,2]

# convertir les fahrenheit en celsius:
tMinCels=(tempMin-32)*5/9
tMaxCels=(tempMax-32)*5/9
print (tMinCels)
print(tMaxCels)

# découpe des 15 jours en 2 semaines
joursSem1=jours[:7]
joursSem2=jours[7:]

# conversion du jour réel en jour de la semaine:
sem1=joursSem1-8
print(sem1)
sem2=joursSem2-15
print(sem2)

# découpe des temp des 15 jours en 2 semaines:
tMaxCelsSem1=tMaxCels[:7]
tMinCelsSem1=tMinCels[:7]
tMaxCelsSem2=tMaxCels[7:]
tMinCelsSem2=tMinCels[7:]

# # autre possibilité pour découper:
# tMaxCelsSem12=np.array(np.array_split(tMaxCels,2)
# tMaxs1C = tMaxCelsSem12[0]
# print(tMaxs1C)

moyTempJr=(tMinCels+tMaxCels)/2
tMinMois=tMinCels.min()
tMaxMois=tMaxCels.max()
tempMoy=moyTempJr.mean()
print(moyTempJr)
print(tMinMois)
print(tMaxMois)
print(tempMoy)

# xS1=joursSem1
# xS2=joursSem2

plt.subplot(221)
plt.plot(sem1, tMaxCelsSem1,'b^-', label="Max")
plt.plot(sem1, tMinCelsSem1, 'g^-',  label="Min")
plt.ylabel("Température °C")
plt.xlabel("Jour")
plt.gca().set_ylim([10,40])
plt.title("Semaine1")
plt.legend()

plt.subplot(222)
plt.plot(sem2, tMaxCelsSem2, 'bo-',  label="Max")
plt.plot(sem2, tMinCelsSem2, 'go-', label="Min")
plt.ylabel("Température °C")
plt.xlabel("Jour")
plt.gca().set_ylim([10,40])
plt.title("Semaine2")
plt.legend()

plt.subplot(212)
plt.plot(jours, moyTempJr, 'rs-',  label="Moy")
plt.gca().set_ylim([10,40])
plt.ylabel("Température °C")
plt.xlabel("Jour")
plt.title("Mois")
# plt.legend()
plt.annotate('T° Moy :'+str("%.2f"%tempMoy)+"°C"+'\nT°Min :'+str("%.2f" %tMinMois)+"°C"+'\nT°Max :'+str("%.2f" %tMaxMois)+"°C",xy=(20, 32))

plt.show()
