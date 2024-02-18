class Length:
    def __init__(self,feet=0,inches=0):
        self.feet = feet
        self.inches= inches
    def SetLength(self,feet,inches):
        self.feet = feet
        self.inches = inches
    def getLength(self):
        return (self.feet, self.inches)
    def __str__(self):
        return f"({self.feet}, {self.inches})"
    def __add__(self, other):
        total_inches = self.inches + other.inches
        total_feet = self.feet + other.feet + total_inches // 12
        remaining_inches = total_inches % 12
        return Length(total_feet, remaining_inches)

#Example usage:
length1 = Length(5, 8)
length2 = Length(3, 2)

print("Length 1:", length1)
print("Length 2:", length2)

sum_length = length1 + length2
print("Sum of Length 1 and Length 2:", sum_length)
        
        