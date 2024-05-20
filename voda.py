

def maxim(x,y,z):
    def compara(p,q,r):
        return (p>q and p>r)
    if(compara(x,y,z)):
        return x
    if(compara(y,x,z)):
        return y
    if(compara(z,x,y)):
        return z

print(maxim(4,5,3))
