#permutacije naj bodo od 0 do n-1
class Permutacija:
    def __init__(self,seznam,n=None):
        self.seznam=seznam
        if n==None:
            self.n=len(self.seznam)
        else:
            self.n=n
    def permutiraj(self,sez):
        if len(sez)==self.n:
            j=[0 for x in range(self.n)]
            for i in range(self.n):
                j[i]=sez[self.seznam[i]]
            return j
        else:
            return "sranje"
    def __repr__(self):
        return str(self.seznam)
    def __len__(self):
        return self.n

    def __mul__(self,druga):
            k=self.permutiraj(druga.seznam)
            return Permutacija(k,self.n)
                
    

p=Permutacija([0,2,1],3)
print(p.permutiraj(["a","b","c"]))
