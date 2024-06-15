# Chapter 09 - While Loop
########################################################
# initialization of the control variable
# i = 1;

# # test on the control variable
# while(i <= 3):
#     print("Welcome to Python");
#     i = i + 1; # update on the control variable

# print("End of program");

########################## EXERCISE 1 ##############################

# i = 1; # starts the loop from the set variable

# while(i <= 5): # i passes as true until it's false
#     print(i) #print i because it's true
#     i = i + 1; # i is incremented until it's false

# print("End of program"); #ends the loop

########################### EXERCUSE 2 #############################

# i = 5;

# while(i <= 25):
#     print(i);
#     i = i + 5;

# print("End of program");

########################### EXERCUSE 3 #############################

# i = 10;
# while(i >= 0):
#     print(i);
#     i = i - 1;

# print("End print program");

########################### EXERCUSE 4 ##############################

# numberOfTimes = int(input("Enter a number: ")); # the user sets the limit of the loop

# i = 1; # initialization

# while(i <= numberOfTimes): # the limit of the loop is checked
#     print("Python is fun"); # output to console

#     i = i + 1; # incremented valu. (Make sure the proper code structure exists)

########################### EXERCUSE 5 ##############################

# name = ""; # initialized with a blank variable

# while(name != "Daniel"): # while loop expecting the name in condition
#     name = input("Enter a name: ").capitalize(); # presents the name when the condition is met, correcting capitalization error form user.

# print("Welcome"); # executed after loop condition is met

########################### EXERCUSE 6 ##############################

# while(True):
#     state = input("Columbus is the capital city of which US state?: ").capitalize(); # user input 

#     if(state == "Ohio"): #checks the condition of the user input
#         print("Congratulations, you won the trivia!") # output to the user when condition is true
#         break; # console will keep running the program until it's told to stop.
# print("End of program");

########################### EXERCUSE 6 ##############################
# “Write a program that asks the user to enter a number via keyboard input. Then, create a loop that repeats as many times as the entered number (for example, if the user enters 3, the loop should run three times). And then, within the body of loop, print four asterisks "****".”

# i = 1;

# userInput = int(input("Enter a number: "));

# while(i <= 3):
#     print("***");
#     i = i + 1;

# print("End of program");

########################### EXERCUSE 7 ##############################
name =""; 

while(True):
    name = input("Enter the keyword: ");
    
    if(name != "Robert"):
        print("Incorrect Keyword");
    else:
        print("Correct Keyword");
        break;
