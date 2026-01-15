# Δημήτρης Σαουρίδης Εργασία Άσκηση 1 7/4/2025

nikes1=0 #Plithos nikwn gia ton prwto paikth
nikes2=0 #Plithos nikwn gia deutero paikth
name1=str(input("Dwse to onoma tou prwtou paikth :")) #Eisagwgh onomatos tou prwtou paikth
name2=str(input("Dwse to onoma to deuterou paikth :"))#Eisagwgh onomatos tou deuterou paikth 
print("Dwse mia epilogh :\n1. PETRA\n2. PSALIDI\n3. XARTI\n4. TELOS") #Menou Epiloghs
while True:
    epilogh1=int(input("Dwse mia apo tis parapanw epiloges apo 1 mexri 4 :")) #Eisagwgh epiloghs tou 1ou paikth
    epilogh2=int(input("Dwse mia apo tis parapanw epiloges apo 1 mexri 4 :")) #Eisagwgh epilloghw tou 2ou paikth
    while epilogh1<=0 or epilogh>=5 or epilogh2<=0 or epilogh>=5 :  #Elegxos Egkurotitas
        if epilogh1<=0 or epilogh>=5 :
            epilogh1=int(input("Dwse mia apo tis parapanw epiloges apo 1 mexri 4 :"))
        else    
        epilogh2=int(input("Dwse mia apo tis parapanw epiloges apo 1 mexri 4 :"))
    if epilogh1==4 or  epilogh2==4:
        break #An dothei h epilogh 4 bgainei apo thn epanalhpsh
    if epilogh1==epilogh2 : 
        print("Nikhse o paikths me to onoma",name1)
    elif (epilogh1 == 1 and epilogh2 == 2) or (epilogh1 == 2 and epilogh2 == 3) or (epilogh1 == 3 and epilogh2 == 1) or (epilogh1 == 3 and epilogh2 == 1):
        nikes1 += 1
    else:
        nikes2=nikes2+1
        print("Nikhse o paikths me to onoma",name2)
    print("Dwse mia epilogh :\n1. PETRA\n2. PSALIDI\n3. XARTI\n4. TELOS")      
if nikes1>nikes2: #Metrhsh Nikwn kai poios o Nikiths
    print("O nikiths einai o",name1)
elif nikes2>nikes1:
    print("O nikiths einai o ",name2)
else:
    print("To paixnidi eleikse isopalo")
    

    
