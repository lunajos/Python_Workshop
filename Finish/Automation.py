import os
import shutil
count = 0

for root, dirs, files in os.walk("./Data/ovpn_src/", topdown=True):

    for name in files:

        namelist = name.split(".", 5)
        country = namelist[0][0:2]
        protocol = namelist[3][0:3]

        newname = namelist[0][3:] + "_config_" + namelist[3][3:]  +  ".ovpn"

        destination = os.path.join(os.getcwd(), "Data", "ovpn_dest"  )
        source = root + name

        if not os.path.isdir(os.path.join(destination,country)):
            os.mkdir(os.path.join(destination, country))

        if not os.path.isdir(os.path.join(destination, country, protocol)):
            os.mkdir(os.path.join(destination, country, protocol))

        count +=1
        shutil.copyfile(source, os.path.join( destination, country, protocol, name))

print("Successfully Oganized " + str(count) + " Files")
