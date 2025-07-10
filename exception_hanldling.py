
'''
try:
    print(x)
except: 
    print(" Something went wrong")
finally:
    print(" The 'try except' is finished")
'''
    
try:
    print(x)
except: 
    print(" Variable x is not defined")
else:
    print(" The 'try except' is finished")    
    
    
x = -1
if x < 0:
        raise Exception(" Sorry, no numbers below zero")