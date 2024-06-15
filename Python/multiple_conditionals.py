# multiple conditionals chapter 8

# Figure 8.2 ------------------------------------------------------------------------------------

# temp = float(input("Enter temperature: "));

# if(temp > 27):
#     print("Buy Ice Cream");
# else:
#     print("Buy Orange Juice");

# print("End of Program");

# Example Area of a Square -----------------------------------------------------------------------

# side = float(input("Enter the length of the square's side: "));

# if(side > 0):
#     area = side * side;
#     print("The area of the square is: " + str(area));
# else:
#     print("Square's side must be greater than zero.");

# Example 8.2 ------------------------------------------------------------------------------------
#  elif section evaluated only if all previous conditions were false.

# temp = float(input("Enter temperature: "));

# if(temp > 27):
#     print("Buy ice cream");
# elif(temp < 15):
#     print("Buy chocolate");
# else:
#     print("Buy orange juice");

# print("End of program");

# Example 8.3 ------------------------------------------------------------------------------------

# attractionType = int(input("Enter type 1) roller coster 2) train: "));
# height = float(input("Enter height: "));

# if(attractionType == 1):
#     if (height >= 121.92):
#         print("Enjoy the roller coaster");
#     else:
#         print("Height not allowed.");
# elif(attractionType == 2):
#     print("Enjoy the train ride");

# second example --------------------------------------------------------------------------------

# if(attractionType == 2):
#     print("Enjoy the train ride");
# elif(attractionType == 1 and height >= 121.92):
#     print("Enjoy the roller coaster")
# elif(attractionType == 1 and height < 121.92):
#     print("Height not allowed");

# print("End of program");

# Example Practice ------------------------------------------------------------------------------------

# genre = input("Enter your favorite musical genre: ");

# if(genre == "hip hop" or genre == "hip-hop" or genre == "rap"):
#     print("You have good taste");
# else:
#     print("Disgusting");

# Example 8.4 ------------------------------------------------------------------------------------

student1 = input("Enter the student name 'Michelle': ");
vote1 = int(input("Enter the vote count: "));
student2 = input("Enter the student name 'Ronald': ");
vote2 = int(input("Enter the vote count: "));


if(student1 == "Michelle", "michelle" and vote1 == True):
    if(vote1 > vote2):
        print(student1.capitalize());

if(student2 == "Ronald","ronald" and vote2 == True):
    if(vote2 > vote1):
        print(student2.capitalize());