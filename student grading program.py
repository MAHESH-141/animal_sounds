# description:
'''
you are tasked with creating a simple student grading program using python.
the program should take i/p from the user from the marks,obtained by a student in a subject and then calculate 
and display the grade based on the following grading scale:
90 or above:A+
80 to 89 : A
70 to 79: B
60 to 69: C
50 to 59: D
below 50: fail

'''


mark=int(input("ENTER YOUR PERCENTAGE MARK : "))

if mark>=90:
      print('congratulations!!!')
      print('you are achieving "A+" grade')
      
elif (mark>=80 and mark<=89) :
      print('congratulations!!!')
      print('you are achieving "A" grade')  
      
elif (mark>=70 and mark<=79) :
      print('congratulations!!!')
      print('you are achieving "B" grade')
      
elif (mark>=60 and mark<=69) :
      print('congratulations!!!')
      print('you are achieving "C" grade')
      
elif (mark>=50 and mark<=59) :
      print('congratulations!!!')
      print('you are achieving "D" grade')      

else:
      print('SORRY YOU ARE FAIL!!!')                     