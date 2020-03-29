print("Welcome to the Golf Club Helper!")
print("Tell me your situation, and I'll recommend a club")

green = str(input("Did you hit it on the green? "))


howFar = int(input("How far is the ball from the hole? "))

if(green=="y" and green != "y"):
    print("I recommend using your putter")
if(howFar > 200 and green != "y"):
    print("I recommend using your Driver")
if(howFar >= 140 and howFar <= 200 and green != "y"):
    print("I recommend using your 5-Iron")
if(howFar >= 100 and howFar < 140 and green != "y"):
    print("I recommend using your 9-Iron")
else:
    print("I recommend using your Pitching Wedge")
    





