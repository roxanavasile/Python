roomLength = float(input('Enter room length: '))
while roomLength <=0:
    print('Room length cannot be negative.')
    roomLength = float(input('Enter room length: '))

roomWidth = float(input('Enter room width: '))
while roomWidth <=0:
    print('Room width cannot be negative.')
    roomWidth = float(input('Enter room width: '))

roomHeight = float(input('Enter room height: '))
while roomHeight<=0:
    print('Room height cannot be negative.')
    roomHeight = float(input('Enter room height: '))

roomVolume = roomLength * roomWidth * roomHeight
while roomVolume<=0:
    print('Room volume cannot be negative.')
    roomVolume = roomLength * roomWidth * roomHeight

btuNeeded = roomVolume * 3.5
print('BTU needed for this room:', btuNeeded)
