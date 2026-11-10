while True:
    x=input('Enter your name :')
    with open ('user.txt','a') as l:
        l.write ('\n'+x)
    print ('welcom',x)
    y=input ("Do you want coffee or smoke :")
    if y=='coffee':
        print ("12$ \n")
    elif y=='smoke':
        print ('5$ \n')
    else :
        print ("="*30)
        print ("   /Thanks for your trust\ ")
        print ("="*30)
        exit()
