import random 
import rudolph, hallpass

# extension add a create madlib function

if __name__ == "__main__": 
    m = random.choice([rudolph, hallpass])
    print(m)
    print(m.madlib())

    

