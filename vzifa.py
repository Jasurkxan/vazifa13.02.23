try:
 month = {
    1:'Janauary',
    2:'February',
    3:'March',
    4:'April',
    5:'May',
    6:'June',
    7:'July',
    8:'August',
    9:'September',
    10:'October',
    11:'November',
    12:'December'}
 
 print("\nMalumotlarni: DD.MM.YYYY Hour:Minute korinishida kiriting !!!")
 a=input(">>> ").split()
 vaqt=a[1].split(':')
 m,s=int(vaqt[1]),int(vaqt[0])
 kun=a[0].split(".")
 
 for i in month:
    if i==int(kun[1]):
        if m==1 and s>1:
            print(f"{kun[0]} {month[i]} {kun[2]} year {s} hours {m} minute")
        elif m>1 and s==1:
            print(f"{kun[0]} {month[i]} {kun[2]} year {s} hour {m} minutes") 
        elif m==1 and s==1:
            print(f"{kun[0]} {month[i]} {kun[2]} year {s} hour {m} minute")
        else:
            print(f"{kun[0]} {month[i]} {kun[2]} year {s} hours{m} minutes")
    elif int(kun[1])>12:
       print(f"Eslatma !\n\t1 Yil 12 ta oydan iborat.Siz {kun[1]} kiritdingiz")  
       exit()
        
except:
   print("\nMalumot kiritishda xatolikga yol qoygan bolishingiz mumkin.Yana urinib koring !")    
            
