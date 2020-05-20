def oudansliste(list,caractere): 
      for i in range(len(list)):
               if liste[i]==caractere:
                       return i
      return -1
         


def ajouterchiffre(nombreinit,chiffre2):
            nombre=10*nombreinit
            nombreinit=nombre+chiffre2
      

def letter_to_number(text):
      n=len(text)
      nombre
      list = [ ,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,.,!,?,-,@,"]
      for i in range(n):
           if text[i]==',':
                  ajouterchiffre(nombre,0)  #we put a 0 as a separator of LETTERS
                  ajouterchiffre(nombre,36) # we represent ',' by 36
            elif (oudansliste(list,text[i])=-1):  #we check if its a letter or a character of pronounciation
                        s=2+oudansliste(list,text[i]) # we add 2 because 1 and 0 are taken as separators
                         ajouterchiffre(nombre,0) #we put a 0 as a separator of LETTERS
                        if s>9:
                                 ajouterchiffre(nombre,s//10)
                                   ajouterchiffre(nombre,s%10)
                        else:
                                   ajouterchiffre(nombre,s)
            else: # so we know we are dealing with a number here
                     s=2+oudansliste(list,text[i]) # we add 2 because 1 and 0 are taken as separators
                         ajouterchiffre(nombre,1) #we put a 1 as a separator of NUMBERS
                        if s>9:
                                 ajouterchiffre(nombre,s//10)
                                   ajouterchiffre(nombre,s%10)
                        else:
                                   ajouterchiffre(nombre,s)
           
              
       return nombre
       
       
def number_to_letter(numbers):
      n=len(numbers)
      text=[]
      list = [ ,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,.,!,?,-,@,"]
      for i in range(n):
            numero=0
            if numbers[i]!='-1':
                 numero=numbers[i]
            text.append(list[numero])
      return text
