# 1 cup = 240 ml

def convert(cups):
    ml = round((float(cups) * 240), 2)
    return ml

print("This program will help you convert cups to milliliters.")
cups = raw_input("Enter the number of cups you'd like to convert to ml:  ")
mil = convert(cups)
print(cups + " cups is equal to " + str(mil) + " milliliters!")
