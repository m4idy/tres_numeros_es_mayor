print("...................................................................")
print("......................Numero mayor.................................")
print("...................................................................")


# imput 

n=int(input("digite un numero"))
o=int(input("digite otro nuemero"))
p=int(input("digite otro nuemero"))



 
# output


if n>o>p :
    rta = "Este es el mayor de los tres: " + str(n)

else :
    if n>o<p :
        rta ="Este es el mayor de los tres: " + str(p)
    
    else :
        if n<o>p :
           rta = "Este es el mayor de los tres: " + str(o)

print (rta) 