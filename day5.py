heights = input("Input students Heights: ").split(',')
print(round((sum(map(int,heights))*1.0/len(heights)),2))