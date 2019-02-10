room_length=float(input("Enter room length: "))
room_width=float(input("Enter room widht: "))
room_height=float(input("Enter room height: "))
room_volume=room_height*room_length*room_width
BTU_needed=room_volume*3.5
room_sunlight=input("Does the room get a lot of sunlight? [yes/no]:" )
if room_sunlight=="yes":
    increased_BTU_needed=BTU_needed*0.2
    final_BTU_needed=increased_BTU_needed+BTU_needed
    print("BTU needed for the air conditioner is: ", final_BTU_needed)
if room_sunlight=="no":
    print("BTU needed for the air conditioner is: ", BTU_needed)
