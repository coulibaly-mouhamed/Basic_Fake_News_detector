def oudansliste(list,caractere): 
      for i in range(len(list)):
               if liste[i]==caractere:
                       return i
      retrun -1
         



def letter_to_number(text):
      n=len(text)
      new_text=[]
      list = [ ,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,.,!,?,-,@,"]
      for i in range(n):
           if text[i]==,:
                  new_text.append(,)
            else :
                  s=oudansliste(list,text[i])
                 new_text.append(s)
       return new_text
       
       
def number_to_letter(numbers):
      n=len(numbers)
      text=[]
      list = [ ,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,.,!,?,-,@,"]
      for i in range(n):
            numero=0
            if numbers[i]!=-1:
                 numero=numbers[i]
            text.append(list[numero])
      return text
