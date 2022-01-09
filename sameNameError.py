def spam():
    print(eggs)  # ERROR! local variable is referenced before it is assigned a value
    eggs = 'spam local'  # needs to be placed above the print order

eggs = 'global'
spam()
