# Author PT 10/19/20
# Integer division is //

print("Think of a date in the past...")
x = int(input("Enter the year of the date: "))
m = int(input("Enter the month of the date: "))
q = int(input("Enter the day of the month: "))

j = (x // 100)
k = (x % 100)

if m == 1:
    int(m + 12)
if m == 2:
    int(m + 12)

h = int((q + ((26 * (m + 1)) // 10) + k + (k // 4) + (j // 4) + (5 * j)) % 7)

if h == 0:
    print(m, "/", q, "/", x, "was a Saturday")
if h == 1:
    print(m, "/", q, "/", x, "was a Sunday")
if h == 2:
    print(m, "/", q, "/", x, "was a Monday")
if h == 3:
    print(m, "/", q, "/", x, "was a Tuesday")
if h == 4:
    print(m, "/", q, "/", x, "was a Wednesday")
if h == 5:
    print(m, "/", q, "/", x, "was a Thursday")
if h == 6:
    print(m, "/", q, "/", x, "was a Friday")
