from characters import Monster, Warrior, Sorcerer, Sage
import special_abilities as spc_abs
import time
import sympy
from sympy.abc import pi
from sympy import pi, pretty
import math
import random


# How to print the pi symbol using standard function chr:
print(f"The {chr(1087)} symbol represents {math.pi:.8f}")

# The "prettier" output comes from the sympy library
sympy.pprint(pi)


pi_str = pretty(pi, use_unicode=True)
print(f"The {pi_str} symbol is the best way to represent {math.pi:.8f}")
print(f"One of the most famous math equations is: {pi_str}r{chr(0x00B2)}")

r = 18
print(f"If the radius of Circle A is {r}, {pi_str}r{chr(0x00B2)} = {pi_str}{r}{chr(0x00B2)} = {math.pi*(r**2):.2f}")
#
# if __name__ == '__main__':
#     malda = Sorcerer("Malda")
#     for title, trait in malda.traits.items():
#         if trait:
#             print(f"{title}:  {trait}")
#
#     move_1 = input("\n\tWould you like to move? (Y or N) ")
#     if move_1.lower() == "y":
#         print(f"\n\t{malda.move()}")
#
#     field = ['A', 'B', 'C', 'M', 'X', 'Y', 'Z']

symbols = { 164:'currency',
            167: 'Section',
            931: 'Sigma',
            934: 'Phi',
            936: 'Psi',
            937: 'Omega',
            916: 'Delta',
            948: 'lower-delta',
            951: 'Theta',
            1046: 'Zhe',
            1087: 'Pi',
            8470: 'Numero',
            8383: 'Bitcoin',
            8373: 'Cedi',
            8380: 'Manat',
            8731: 'Cube Root',
            8853: 'Circled Plus',
            8854: 'Circled Minus',
            8855: 'Circled Times',
            8858: 'Circled Ring',
            8927: 'Equal to or Succeeds',
            8954: 'Contains with long horizonal stroke',
            8982: 'Position Indicator',
            9827: 'Black Club Suit',
            8606: 'Leftwards Two Headed Arrow',
            8607: 'Upwards Two Headed Arrow',
            8608: 'Rightwards Arrow',
            8609: 'Downwards Arrow',
            9600: 'Upper Half Block',
            9604: 'Lower Half Block',
            9608: 'Full Block',

}

for symbol, name in symbols.items():
    print(f"\033[1:5m{chr(symbol)}: {name}")

def big_A_with_chr():
    block = chr(9608)  # █ Full block
    lower_half = chr(9604)  # ▄ Lower half block
    upper_half = chr(9600)  # ▀ Upper half block
    space = " "

    return f"""
   {lower_half * 3}   
  {block}{space * 3}{block}  
 {block}{space * 5}{block} 
 {block}{upper_half * 5}{block} 
 {block}{space * 5}{block} 
    """

print(big_A_with_chr())

def big_cedi_curved():
    block = chr(9608)         # █ Full block
    lower_half = chr(9604)    # ▄ Lower half block
    upper_half = chr(9600)    # ▀ Upper half block
    med_shade = chr(9618)        # ▒ Medium Shade
    space = " "

    return f"""
    {lower_half*6}      
  {block}{space*8}{block}   
 {block}{space*4}{med_shade}{space*5}   
 {block}{space*4}{med_shade}{space*5}   
 {block}{space*4}{med_shade}{space*5}   
  {block}{space*8}{block}   
    {upper_half*6}      
"""

print(big_cedi_curved())


def big_cedi_detailed():
    block = chr(9608)         # █ Full block
    h_line = chr(9552)        # ═ Double horizontal line
    med_shade = chr(9618)        # ▒ Medium Shade
    space = " "

    return f"""
   {block*7}     
  {block}{space*9}{block}  
 {block}{space*4}{med_shade}{space*6}  
 {block}{space*4}{h_line*6}  
 {block}{space*4}{med_shade}{space*6}  
  {block}{space*9}{block}  
   {block*7}     
"""

print(big_cedi_detailed())


def big_cedi_with_line():
    block = chr(9608)         # █ Full block
    med_shade = chr(9618)        # ▒ Medium Shade
    space = " "

    return f"""
    {block*8}    
  {block}{space*10}{block}  
 {block}{space*5}{med_shade}{space*6} 
 {block}{space*5}{med_shade}{space*6} 
 {block}{space*5}{med_shade}{space*6} 
  {block}{space*10}{block}  
    {block*8}    
"""

print(big_cedi_with_line())

for i in range(3):
    print(f"\033[31m{chr(8608)}\033[39m", end=" ")
    time.sleep(0.3)
print()
for _ in range(5):
    for s in [chr(164), chr(167), chr(931), chr(1046), chr(8982)]:
        print(f"\033[34mMagic: {s}\033[39m", end='\r')
        time.sleep(0.1)


p = ['A', 'B', 'C', 'M', 'X', 'Y', 'Z']
A = p[0]
B = p[1]
C = p[2]
M = p[3]
X = p[4]
Y = p[5]
Z = p[6]
print("C is next to M:", p.index(C) == p.index(M) - 1)
print("C is next to X:", p.index(C) == p.index(X) - 1)
print("C is next to B:", p.index(C) == p.index(B) - 1 or p.index(C) == p.index(B) + 1)
t = random.choice(p)
u = random.choice(p)
print(f"{t} is next to {u}: {p.index(t) == p.index(u) - 1 or p.index(t) == p.index(u) + 1}")

