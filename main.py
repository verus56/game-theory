import numpy as np


M2 = np.array([[(4, 3), (5, 1), (6, 2)],
               [(2, 1), (8, 4), (3, 6)],
               [(3, 0), (9, 6), (2, 8)]])


def StrategieDominéeLigne(M):
    M2=M
    ind = -1
    indtemp = -1
    l=0
    l2=1
    br=False
    c=0
    i=0
    while (l <len(M2)-1):    
        l2=l+1
        while (l2 <len(M2)):
            ind=-1
            indtemp=-1
            br=False
            c=0
            while (c < len(M2[0])):
                if (M2[l,c,0]> M2[l2,c,0]):
                    indtemp=l2
                elif(M2[l,c,0]< M2[l2,c,0]):
                    indtemp=l
                c+=1
                if(ind == -1):
                        ind = indtemp
                elif (ind != indtemp):
                        br=True
                        break
            if indtemp==-1:
                br=True
            if br == False:
                M2=np.delete(M2, ind,axis=0)
                
            l2+=1
        if br==True:
            l+=1
            
    return M2
            

def StrategieDominéeCol(M):
    M2=M
    ind = -1
    indtemp = -1
    c=0
    c2=1
    br=False
    l=0
    i=0
    while (c <len(M2[0])-1):    
        c2=c+1
        while (c2 <len(M2[0])):
            ind=-1
            indtemp=-1
            br=False
            l=0
            while (l < len(M2)):
                if (M2[l,c,1]> M2[l,c2,1]):
                    indtemp=c2
                elif(M2[l,c,1]< M2[l,c2,1]):
                    indtemp=c
                l+=1
                if(ind == -1):
                        ind = indtemp
                elif (ind != indtemp):
                        br=True
                        break
            if indtemp==-1:
                br=True
            if br == False:
                M2=np.delete(M2, ind,axis=1)
                
            c2+=1
        if br==True:
            c+=1
            
    return M2


def StrategieDominée(M):
    con=True
    M2=M
    restemp=M2
    while con:
        
        res1= StrategieDominéeLigne(restemp)
        res2=StrategieDominéeCol(res1)
        if (np.shape(res2)==np.shape(restemp)):
            con=False
        else:
            restemp=res2            
    return res2



res= StrategieDominée(M2)
print(res)