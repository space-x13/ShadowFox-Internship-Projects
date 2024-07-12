# 1. Write a function that takes two arguments, 145 and 'o'
# , and
# uses the `format` function to return a formatted string. Print the
# result. Try to identify the representation used.

def format_numbers(digit, character):
    formatted = format(digit, character)
    print(formatted)
format_numbers(145, 'o')
print()
# 2. In a village, there is a circular pond with a radius of 84 meters.
# Calculate the area of the pond using the formula: Circle Area = π
# r^2. (Use the value 3.14 for π) Bonus Question: If there is exactly
# 1.4 liters of water in a square meter, what is the total amount of
# water in the pond? Print the answer without any decimal point in
# it. Hint: Circle Area = π r^2 Water in the pond = Pond Area
# Water per Square Meter

def calcPondArea(radius):
    PI = 3.14 # pi value

    # pond area calculation
    circular_pond_area = PI * radius ** 2
    return circular_pond_area

# function for water pond
def waterPond(circular_pond_area, waterPerSquareMeter):

    # total water calculation
    totalWater = circular_pond_area * waterPerSquareMeter

    totalWater = int(totalWater)

    return totalWater

def main():
    radius = 84
    waterPerSquareMeter = 1.4

    # area of the circular pond
    pond_area = calcPondArea(radius)

    # total water in pond
    totalWater = waterPond(pond_area, waterPerSquareMeter)

    print(f"Total Water in the pond: {format(totalWater, '.2f')} square meter")

main() # calling main function
print()

# 3. If you cross a 490meterlong street in 7 minutes, calculate your
# speed in meters per second. Print the answer without any decimal
# point in it. Hint: Speed = Distance / Time

def calc_speed(distance, time):
    Speed = distance / time
    return Speed

print(f'Speed in meters per second: {round(calc_speed(490, 420))}')