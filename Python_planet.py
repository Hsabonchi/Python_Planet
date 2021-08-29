import matplotlib.pyplot as plt
import numpy as np
name = []
mass=[]
raduis=[]
period= []

#Reading File
f=open("planets_data.txt", "r")
fwrite=open("mass.txt", "w+")
#loop through each line in the file
for line in f:
        Type=line.split(",")
        x= Type[0]
        name.append(x)
        y=float(Type[1].strip('""'))
        mass.append(y)
        z=float(Type[2].strip('""'))
        raduis.append(z)
        h= Type[3]
        period.append(h)

for item in mass:
   fwrite.write("%s\n" % item)

median=np.median(np.array(mass))

plt.plot(mass, raduis,'.')
plt.show()
f.close()
fwrite.close()


