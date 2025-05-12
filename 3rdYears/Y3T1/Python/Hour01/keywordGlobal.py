x = "amazing~~~"

def callMeGlobal():
    global x
    x = "fantastic~~~"

callMeGlobal()
print("Python is " + x + '.')