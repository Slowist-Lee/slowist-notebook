from sage.all import *
cnt=0
for a11 in range(252):
    for a12 in range(252):
        a13 = (252 - a11 - a12) 
        for a21 in range(242):
            for a22 in range(242):
                a23 = (242 - a21 - a22) 
                for a31 in  range(29):
                    for a32 in  range(29):
                        a33 = (29 - a31 - a32) 
                        # Create the matrix
                        MT = Matrix(Zmod(256), [[a11, a12, a13], [a21, a22, a23], [a31, a32, a33]])
                        cnt+=1

