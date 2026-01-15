# Δημήτρης Σαουρίδης Εργασία Άσκηση 2 7/4/2025
def Epidothsh(timh): #Συνάρτηση για υπολογισμό της επιδότησης
    if timh>=0 and timh<=10000:
        epidothsh=0.025*timh
    elif timh>=10001 and timh<=13000:
        epidothsh=0.025*10000+(timh-10000)*0.05
    elif timh>13001 and timh<=20000:
        epidothsh=0.025*10000+3000*0.05+(timh-13000)*0.15
    else:
        epidothsh=0.025*10000+3000*0.05+7000*0.15+(timh-20000)*0.25
    return epidothsh    
eisprakseis=float(input("Dwse thn miniaia eispraksh :")) # Διάβασμα της μηνιαίας είσπραξης
epid=Epidothsh(eisprakseis) # Κάλεσμα της συνάρτησης  
print(f"H epidothsh einai :{epid:.2f}") # Εμφάνιση της επιδότηση
