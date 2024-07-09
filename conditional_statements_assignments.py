# Assignment-1: if condition
# Check if a person is eligible to vote based on their age
# Input: Age of the person
# Check if the person is eligible to vote
age=int(input("eneter the age of the person: "))
if age>=18:
    print(f"age of the person is {age} and he is aligble for vote")
# Assignment-2: if else condition
# WAP that checks whether a number is positive or negative
number=int(input("enter the number:"))
if number>=0:
    print("number is positive")
else :
    print("number is negative")

# Assignment-3: if else condition
# WAP that Checks if a given number is even or odd
number=int(input("enter the number:"))
if number%2==0:
    print("number is even")
else :
    print("number is odd")
# Assignment-4: nested if condition
# WAP to find the greatest of 3 numbers

# Assignment-5: nested if else condition
"""

Movie Ticket Pricing
Imagine a movie theater that offers different ticket prices based on the age of the customer and the time of the day. The rules might be as follows:

Regular price: $10
Children under 12 and seniors over 65 get a 50% discount.
Matinee show (before 5 PM) offers a 25% discount to all.
"""
movie_ticket_price=10
show_time=float(input("show time"))
age=int(input("enter the age:"))
if (age<12 and age>65):
    if show_time<17:
      movie_ticket_price=movie_ticket_price*0.25
    else :
        movie_ticket_price = movie_ticket_price * 0.5
else :
    if show_time<17:
        movie_ticket_price = movie_ticket_price * 0.75

print(f"the price at showtime {show_time} of the ticket of age {age} and is {movie_ticket_price} ")


# Assignment-6: nested if else condition
# WAP to find the biggest country among 3 based on the population
country1=input("enetr name of the country")
population1=int(input("enter the number of population"))
country2=input("enetr name of the country")
population2=int(input("enter the number of population"))
country3=input("enetr name of the country")
population3=int(input("enter the number of population"))
if population1 >= population2:
        if population1 >= population3:
            biggest_country = country1
        else:
            biggest_country = country3
else:
        if population2 >= population3:
            biggest_country = country2
        else:
            biggest_country = country3

print(f"the biggest country is {biggest_country} ")