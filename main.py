# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
def greet(name,tmp='Hello, <name>!'):
    vervang = '<name>'   #<<<dit de is string dat hij moet vervangen
    greet = tmp.replace(vervang,name)

    return greet

def force(mass,body='earth'):
    #let op in kleine letters voor planeten
    #Maak dictionary planet aan"""
    planet = {'sun':274,
            'jupiter':24.92,
            'neptune':11.15,
            'saturn':10.44,
            'earth':9.798,
            'uranus':8.87,
            'venus':8.87,
            'mars':3.71,
            'mercury':3.7,
            'moon':1.62,
            'pluto':0.58
        }
    force = mass * round(planet[body],1) #afronden 1 decimaal
    return force

def pull(m1,m2,d):
    g=6.674 * 10**-11 # gegeven constante voor gravity
    pull = g*((m1*m2)/d**2) #eerst m1*m2, dan delen door d^2 en dan maar g
    return pull

print(greet('BOB','Testing, <name>! Testing, <name>!'))
print(greet('BOB','Testing, <name>!'))