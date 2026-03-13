a, b, c = map(int, input("Enter three side lengths: ").split()) #input all 3 at once, variables for each side length

print("Equilateral triangle" if len({a, b, c}) == 1 else "Not an equilateral triangle") #created a set to remove duplicates, meaning if there's only 1 
                                                                                        #element in the set, the initial values were the same in this case


