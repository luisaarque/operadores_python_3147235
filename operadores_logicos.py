'''
Los operadores logicos son
an, or not,
obedecen las tablas de verdad:

'''
op1= False
op2= True
op3= op1 or op2
print(op3)
#operador not
op4=not op2
print(op4)
'''
jerarquia definitiva de operadores
1         ()
2         **
3       *,/,%
4         +,-
5     >,<,!=,==,<=,=>
6         not
7         and
8         or
9         =
NOTA:Si hay operaciones en el mismo nivel de jerarquia
se resuelven de izquiera a derecha
'''
op1=False
op2= True
op3=False
op4=True
resultado =not op1 and (op2 or op3 and not op1) and not op4
print(resultado)