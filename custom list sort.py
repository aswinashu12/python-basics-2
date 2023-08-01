def my_class(n):
    return abs(n-12)

classes=[10,12,7,9,6]
classes.sort(key=my_class)
print(classes)
