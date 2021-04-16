# This code demonstrates the solve_enigma() method of my Engima class. This
# method takes an encoded message, a crib, and any known settings of the Enigma
# machine and then works through the remaining Enigma Machine settings to find
# possible solutions to the message. These examples are not intended to be an
# exhaustive demonstration of the solve_enigma() method, but rather to showcase
# how it works in practice.

from enigma import *

# Message to encode and crib
message = 'THESEAREEXAMPLESOFUSINGTHEENIGMASOLVEMETHOD'
crib = 'ENIGMA'

# Create a new Enigma object and encode the message
plugboard = ['AZ', 'BY', 'CX']
rotors = ['I', 'III', 'IV']
positions = ['A', 'B', 'C']
settings = [3, 2, 1]
reflector = 'B'

my_enigma = Enigma()
my_enigma.add_plugboard(plugboard)
my_enigma.add_rotors(rotors, positions, settings)
my_enigma.add_reflector(reflector)
encoded_message = my_enigma.encode_message(message)

# Check encoded message
print('original message:', message)
print('encoded message to solve:', encoded_message)
print('crib:', crib, '\n')

# Check machine configuration
print('Enigma settings:', '\n', my_enigma.show_config(), '\n')

# Example 1: Solve where we know everything except the reflector
print('Ex 1. Solving for reflector:')
ex1 = solve_enigma(encoded_message, crib, plugboard, rotors, positions,
                   settings)
print(ex1, '\n')

# Example 2: Solve where we know everything except the rotors
print('Ex 2. Solving for rotors:')
ex2 = solve_enigma(encoded_message, crib, plugboard, pos_in=positions,
                   set_in=settings)
print(ex2, '\n')

# Example 3: Solve where we know everything except the positions
print('Ex 3. Solving for positions:')
ex3 = solve_enigma(encoded_message, crib, plugboard, rot_in=rotors,
                   set_in=settings, ref_in=reflector)
print(ex3, '\n')

# Example 4: Solve where we know everything except the rotors and reflector
print('Ex 4. Solving for rotors and reflector:')
ex4 = solve_enigma(encoded_message, crib, plugboard, set_in=settings,
                   pos_in=positions)
print(ex4, '\n')

# Example 5: Solve where we know everything except the rotors, positions and reflector
# Takes about a minute to run
print('Ex 5. Solving for rotors, positions and reflector:')
ex5 = solve_enigma(encoded_message, crib, plugboard, set_in=settings,
                   max_iterations=-1)
print(ex5, '\n')
