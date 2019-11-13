# Import Modules
import os
import shutil
count = 0

# Look through each source folder
# Decide how to group files
for root, dirs, files in os.walk("./Data/ovpn_src/", topdown=True):

    for name in files:

        # Read each line, Decide how to split
        namelist = name.split(".", 5)

        # Extract country
        country = namelist[0][0:2]
        # Extract protocol
        protocol = namelist[3][0:3]

        # Define Destination and Source Locations
        destination = os.path.join(os.getcwd(), "Data", "ovpn_dest"  )
        source = root + name

        # Create Country Directory if not exists
        if not os.path.isdir(os.path.join(destination,country)):
            os.mkdir(os.path.join(destination, country))

        # Create Protocol Directory if not exists
        if not os.path.isdir(os.path.join(destination, country, protocol)):
            os.mkdir(os.path.join(destination, country, protocol))

        count += 1
        # Move or Copy file into new location
        shutil.copyfile(source, os.path.join( destination, country, protocol, name))

# Print How many records
print("Successfully Oganized " + str(count) + " Files")
