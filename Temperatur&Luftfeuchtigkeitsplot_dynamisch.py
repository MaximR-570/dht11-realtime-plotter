

import matplotlib.pyplot as plt
# import matplotlib.animation as animation

# import numpy as np

import serial

import time


ser = serial.Serial('COM6', 9600, timeout=1)


Temperaturliste = []
Luftfeuchtigkeitliste = []
Zeitstempel = []

startZeit = time.time()

max_len = 999


plt.ion()
fig, ax = plt.subplots()
ax2 = ax.twinx()

line_temp, = ax.plot([], [], color='tab:red', label = 'Temperatur')
line_feucht, = ax2.plot([], [], color='tab:blue', label = 'Feuchtigkeit')

ax.set_title("Live-Temperatur-und Luftfeuchtigkeitdaten")
ax.set_xlabel("Zeit [s]")
ax2.set_ylabel("Luftfeuchtigkeit [%]")
ax.set_ylabel("Temperatur [°C]")
ax.legend()




try: 
    while True:
        if ser.in_waiting > 0:
            Werte = ser.readline().decode('utf-8').rstrip()
            Werte = Werte.split(",")
            
            if len(Werte) == 2:
                aktuellerTempWert = float(Werte[0])
                aktuellerFeuchtWert = float(Werte[1])
                aktuelleZeit = time.time() - startZeit
            
            
                print(aktuellerTempWert)
                print(aktuellerFeuchtWert)
                
                aktuellerWert = float(aktuellerTempWert)
                
                
                Temperaturliste.append(aktuellerTempWert)
                Luftfeuchtigkeitliste.append(aktuellerFeuchtWert)
                Zeitstempel.append(aktuelleZeit)
                
                Tmin = float(min(Temperaturliste))
                Tmax = float(max(Temperaturliste))
                
                Fmin = float(min(Luftfeuchtigkeitliste))
                Fmax = float(max(Luftfeuchtigkeitliste))
                
                DurchschnittswertTemp = sum(Temperaturliste) / len(Temperaturliste)
                DurchschnittswertFeucht = sum(Luftfeuchtigkeitliste) / len(Luftfeuchtigkeitliste
                                                                           )
                labelTemp = f"Temp | Min: {Tmin:.1f} °C | Max: {Tmax:.1f} °C | Durchschnitt: {DurchschnittswertTemp:.1f} °C"
                labelFeucht = f"Feuchte | Min {Fmin:.1f} % | Max: {Fmax:.1f} % | Durchschnitt: {DurchschnittswertFeucht:.1f} %"
                
                
                line_temp.set_label(labelTemp)
                line_feucht.set_label(labelFeucht)
                
                if len(Temperaturliste) > max_len:
                    Temperaturliste.pop(0)
                    Zeitstempel.pop(0)
                    
                    
                line_temp.set_data(Zeitstempel, Temperaturliste)
                line_feucht.set_data(Zeitstempel, Luftfeuchtigkeitliste)
                
                
                ax.set_xlim(max(0, aktuelleZeit - 600), aktuelleZeit + 10)
                ax.set_ylim(Tmin - 3, Tmax + 3)
                ax2.set_ylim(Fmin-5, Fmax + 5)
                ax.legend(loc="upper left")
                ax2.legend(loc="lower left")
                
                
                
            plt.draw()
                
                
        plt.pause(0.5) # Die Pause muss so gewählt werden, dass sie zum delay im Arduinoskript passt
                    
            
except KeyboardInterrupt:
    print("Programm manuell gestoppt.")
    
finally:
    ser.close()
    print("Serieller Port eschlossen.")
            

