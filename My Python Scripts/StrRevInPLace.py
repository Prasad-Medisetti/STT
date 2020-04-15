s = input("Enter a String :\t")
print("Entered String is :\t", s)
words = s.split()
newwords = [word[::-1] for word in words]
rs = " ".join(newwords)
print("No.of Words :\t", len(newwords))
print("Reversed String :\t", rs)