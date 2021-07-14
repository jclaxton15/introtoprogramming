print("Welcome to the area computational tool!\n")
print("****** Menu *******")
print("yeti   Compute probability of yeti")
print("dragon Compute probability of dragon")
print("????   This_Would_Be_Your_Choice_Don't_Output_This")
print("quit   Quit the tool")

inputValue = input("Please enter your choice: ")
if inputValue == "yeti":
    print("\nYou chose yeti")
elif inputValue == "dragon":
    print("\nYou chose dragon")
elif inputValue == "quit":
    exit();
elif inputValue != "yeti" or inputValue != dragon or inputValue != "quit":
    print(inputValue + " is not a valid choice! Please choose from the menu ")

