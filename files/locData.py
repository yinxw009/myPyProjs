#!/usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np

locVeriance = open("locVeriance.txt","r+")
dataGGAconvert = open("dataGGAconverted.txt","w+")
dataGGAorigin = open("dataGGAoriginal.txt","w+")
line_count = 0
locData = []

abDataLat = str(3103.3087151//100 + (3103.3087151%100)/60)
abDataLong = str(11925.0796437//100 + (11925.0796437%100)/60)

for line in locVeriance.readlines():
  if line_count > 35:
    ggaTime = float(line[7:16])
    if "," not in line[17:29]:
      latNgga = float(line[17:29])
      longEgga = float(line[32:45])
      dataGGAconvert.write(line[7:16] + "," + str(latNgga//100 + (latNgga%100)/60) + "," +str(longEgga//100 + (longEgga%100)/60) + "\n")
      dataGGAorigin.write(line[7:16] + "," + line[17:29] + "," + line[32:45] + "\n")
    else:
      dataGGAconvert.write(line[7:16] + "," + abDataLat + "," + abDataLong + "\n")
      dataGGAorigin.write(line[7:16] + "," + str(3103.3087151) + "," +str(11925.0796437) + "\n")
    
    locData.append([ggaTime, latNgga, longEgga])
    
    print(ggaTime, latNgga, longEgga)
  line_count += 1

data = np.array(locData)
plt.figure(1, dpi=100)
plt.plot(data[:,1], data[:,2], 'ro')
plt.show()

locVeriance.close
dataGGAconvert.close
dataGGAorigin.close