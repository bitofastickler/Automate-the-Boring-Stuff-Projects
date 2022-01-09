def spam():
    global eggs
    eggs = 'spam'  # this is the global variable (acts like a global value modifier)

def bacon():
    eggs = 'bacon'  # this is a local variable

def ham():
    print(eggs)  # this is the global variable (it's not defined under the local function)

eggs = 42 # this is the global
spam()
print(eggs)
