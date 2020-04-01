print("Welcome to the Golf Club Helper!")
print("Tell me your situation, and I'll recommend a club\n")

green = str(input("Did you hit it on the green? "))


howFar = int(input("How far is the ball from the hole? "))

if(green =="y"):
    print("\nI recommend using your putter")
elif(howFar > 200 and green != "y"):
    print("\nI recommend using your Driver")
elif(howFar >= 140 and howFar <= 200 and green != "y"):
    print("\nI recommend using your 5-Iron")
elif(howFar >= 100 and howFar < 140 and green != "y"):
    print("\nI recommend using your 9-Iron")
else:
    print("\nI recommend using your Pitching Wedge")
    

    





