from tkinter import *
from tkinter import messagebox


window = Tk()
window.title('Calculator')
window.geometry('250x360+300+100')
window.configure(bg='#001a1a')
window.resizable(FALSE,FALSE)


   
input_user = StringVar()

click = StringVar()

comma_write = StringVar()
comma_has_written = comma_write.get()
comma_write.set('0')

#------------------------------------------------------------------------------------------------------
#-------------------------------------Functions--------------------------------------------------------
#------------------------------------------------------------------------------------------------------
    
def del_bt():
    print("delete")
    x = input_user.get()
    input_user.set(x[:-1])
        
def clear_bt():
    print("clear")
    x = input_user.get()
    input_user.set('')
    comma_has_written = comma_write.get()
    comma_write.set('0')
   
def plus_bt():
    equal_clicked = click.get()
    x = input_user.get()
    if len(x)>=15:
        messagebox.showwarning("warning", "  مش مسموح لحضرتك تكتب أرقام أكتر من كده ، \n امسح أرقام وكمل حساباتك تاني \nYou can't write more number after this,\n This is the maximum length of numbers and operators" )
    else:
        print("plus")
        x = input_user.get()
        input_user.set(x+'+')
        click.set('no')
        comma_has_written = comma_write.get()
        comma_write.set('0')

def minus_bt():
    equal_clicked = click.get()
    x = input_user.get()
    if len(x)>=15:
        messagebox.showwarning("warning", "    مش مسموح لحضرتك تكتب أرقام أو عمليات أكتر من كده \n  امسح أرقام وبعدين كمل حساباتك تاني ، \nYou can't write more number after this,\n This is the maximum length of numbers and operators" )
    else:
        print("minus")
        x = input_user.get()
        input_user.set(x+'-')
        click.set('no')
        comma_has_written = comma_write.get()
        comma_write.set('0')
        
def multi_bt():
    x = input_user.get()
    equal_clicked = click.get()
    if len(x)>=15:
        messagebox.showwarning("warning", "  مش مسموح لحضرتك تكتب أرقام أكتر من كده ، \n امسح أرقام وكمل حساباتك تاني \nYou can't write more number after this,\n This is the maximum length of numbers and operators" )
    else:
        if equal_clicked == 'yes':
            print("multi")
            x = input_user.get()
            input_user.set(x+'*')
            click.set('no')
            comma_has_written = comma_write.get()
            comma_write.set('0')
        elif len(x)==0 or x[0]== '/' or x[0]== '*':
            input_user.set('')              
            
        else:
            if x[-1]=='/' or x[-1]=='*':
               messagebox.showwarning("warning", "You mustn't write // or **, you can write only one * or /" )
            elif x[-1]== '-' or x[0]== '+':
                print("can't write *")
            else:
                print("multi")
                x = input_user.get()
                input_user.set(x+'*')
                comma_has_written = comma_write.get()
                comma_write.set('0')

def divi_bt():
    equal_clicked = click.get()
    x = input_user.get()
   
    if len(x)>=15:
        messagebox.showwarning("warning", "  مش مسموح لحضرتك تكتب أرقام أكتر من كده ، \n امسح أرقام وكمل حساباتك تاني \nYou can't write more number after this,\n This is the maximum length of numbers and operators" )
    else:

        if equal_clicked == 'yes':
           print("divi")
           x = input_user.get()
           input_user.set(x+'/')
           click.set('no')
           comma_has_written = comma_write.get()
           comma_write.set('0')

        elif len(x)==0 or x[0]== '/' or x[0]== '*' :
            input_user.set('')              
            
            
        else:
            if x[-1]=='/' or x[-1]=='*':
                messagebox.showwarning("warning", "You mustn't write // or **, you can write only one * or /" )
            elif x[-1]== '-' or x[0]== '+':
                print("can't write /")
            else:
                print("divi")
                x = input_user.get()
                input_user.set(x+'/')
                comma_has_written = comma_write.get()
                comma_write.set('0')
        
def equal_bt():
    x = input_user.get()
    print('sentence is :',x)
    print('sentence length equal',len(x))
    comma_has_written = comma_write.get()
    if len(x)==0:
         input_user.set('0')
         equal_clicked = click.get()
         click.set('yes')
         print(equal_clicked)
         comma_has_written = comma_write.get()
         comma_write.set('0')

    elif x[0]=='+' and len(x)>1:
        x = input_user.get()
        print(x)
        z = eval(x)
        input_user.set(z)
        print(z)
        equal_clicked = click.get()
        click.set('yes')
        print(equal_clicked)
        comma_has_written = comma_write.get()
        comma_write.set('0')
 
            
    elif (x[0]=='.' or x[0]=='+' or x[0]=='-' )and len(x)==1:
        if x[0]=='.':
            
            print('HaHaHa')
            print("equal")
            x = input_user.get()
            input_user.set('0.0')
            equal_clicked = click.get()
            click.set('yes')
            print(equal_clicked)
            comma_has_written = comma_write.get()
            comma_write.set('0')
#--------------------------------
            if equal_clicked == 'yes':
                x = input_user.get()
                input_user.set('')
                click.set('no')
                print(equal_clicked)
                equal_bt()

#--------------------------------
            
        elif x[0]=='+' or x[0]=='-':
            input_user.set('')
        else:
             equal_clicked = click.get()
             print("LAaaaaaaaaaaaaaaaaaa")
             x = input_user.get()
             print(x)
             z = eval(x)
             input_user.set(z)
             print(z)
           
             click.set('yes')
             print(equal_clicked)
             comma_write.set('0')
              
 #------------------------------------------------        
    elif x[0]=='.' and len(x)>1:
        x = input_user.get()
        equal_clicked = click.get()
        print(x)
        z = eval(x)
        input_user.set(z)
        print(z)
        click.set('yes')
        print(equal_clicked)
        comma_write.set('0')
 #------------------------------------------------        

              
        
    
    else:     

                       
        if x[-1]=='/' or x[-1]=='*' or x[-1]=='+' or x[-1]=='-':
            #messagebox.showwarning("warning", "You mustn't write / or * or + or - at the end of calculation without number !" )
            input_user.set(x[:-1])
            x = input_user.get()
            print(x)
            z = eval(x)
            input_user.set(z)
            print(z)
            equal_clicked = click.get()
            click.set('yes')
            print(equal_clicked)
            #print("length is :",len(x))
            comma_has_written = comma_write.get()
            comma_write.set('0')
       
        elif x[:]=='.':
            #messagebox.showwarning("warning", "You mustn't write ' , ' (comma) without number !" )
            input_user.set(x[:-1])
            x = input_user.get()
            print(x)
            z = eval(x)
            input_user.set(z)
            print(z)
            equal_clicked = click.get()
            click.set('yes')
            print(equal_clicked)
            
        else :
            print("equal")
            x = input_user.get()
            print(x)
            z = eval(x)
            input_user.set(z)
            print(z)
            equal_clicked = click.get()
            click.set('yes')
            print(equal_clicked)
            comma_write.set('0')

            


def comma_bt():
    comma_has_written = comma_write.get()
    print(comma_has_written)
    print(comma_write)
    
    x = input_user.get()    
    equal_clicked = click.get()
    
    if len(x)>=15:
        messagebox.showwarning("warning", "  مش مسموح لحضرتك تكتب أرقام أكتر من كده ، \n امسح أرقام وكمل حساباتك تاني \nYou can't write more number after this,\n This is the maximum length of numbers and operators" )
    else:
      
        if equal_clicked == 'yes':
            x = input_user.get()
            input_user.set('')
            click.set('no')
            print(equal_clicked)
            comma_bt()
        elif comma_has_written == '0':
            print("comma")
            x = input_user.get()
            input_user.set(x+'.')
            comma_write.set('1')
            
        
        else:
            print('can" write comma, LoL')
        
               
#----------------------------------------------

def num0_bt():
    equal_clicked = click.get()
    x = input_user.get()
    if len(x)>=15:
        messagebox.showwarning("warning", "  مش مسموح لحضرتك تكتب أرقام أكتر من كده ، \n امسح أرقام وكمل حساباتك تاني \nYou can't write more number after this,\n This is the maximum length of numbers and operators" )
    else:
        
        if equal_clicked == 'yes':
            x = input_user.get()
            input_user.set('')
            click.set('no')
            print(equal_clicked)
            num0_bt()
        else:
            print('0')
            x = input_user.get()
            input_user.set(x+'0')
            comma_has_written = comma_write.get()
            comma_write.set('0')
          
 
def num1_bt():
    equal_clicked = click.get()
    x = input_user.get()
    if len(x)>=15:
        messagebox.showwarning("warning", "  مش مسموح لحضرتك تكتب أرقام أكتر من كده ، \n امسح أرقام وكمل حساباتك تاني \nYou can't write more number after this,\n This is the maximum length of numbers and operators" )
    else:
        if equal_clicked == 'yes':
            x = input_user.get()
            input_user.set('')
            click.set('no')
            print(equal_clicked)
            num1_bt()
        else:
            print("1")
            x = input_user.get()
            input_user.set(x+'1')
            comma_has_written = comma_write.get()
            comma_write.set('0')
        
def num2_bt():
    equal_clicked = click.get()
    x = input_user.get()
    if len(x)>=15:
        messagebox.showwarning("warning", "  مش مسموح لحضرتك تكتب أرقام أكتر من كده ، \n امسح أرقام وكمل حساباتك تاني \nYou can't write more number after this,\n This is the maximum length of numbers and operators" )
    else:
        if equal_clicked == 'yes':
            x = input_user.get()
            input_user.set('')
            click.set('no')
            print(equal_clicked)
            num2_bt()
        else:
            print("2")
            x = input_user.get()
            input_user.set(x+'2')
            comma_has_written = comma_write.get()
            comma_write.set('0')

def num3_bt():
    equal_clicked = click.get()
    x = input_user.get()
    if len(x)>=15:
        messagebox.showwarning("warning", "  مش مسموح لحضرتك تكتب أرقام أكتر من كده ، \n امسح أرقام وكمل حساباتك تاني \nYou can't write more number after this,\n This is the maximum length of numbers and operators" )
    else:
        if equal_clicked == 'yes':
            x = input_user.get()
            input_user.set('')
            click.set('no')
            print(equal_clicked)
            num3_bt()
        else:
            print("3")
            x = input_user.get()
            input_user.set(x+'3')
            comma_has_written = comma_write.get()
            comma_write.set('0')

def num4_bt():
    equal_clicked = click.get()
    x = input_user.get()
    if len(x)>=15:
        messagebox.showwarning("warning", "  مش مسموح لحضرتك تكتب أرقام أكتر من كده ، \n امسح أرقام وكمل حساباتك تاني \nYou can't write more number after this,\n This is the maximum length of numbers and operators" )
    else:
        if equal_clicked == 'yes':
            x = input_user.get()
            input_user.set('')
            click.set('no')
            print(equal_clicked)
            num4_bt()
        else:
            print("4")
            x = input_user.get()
            input_user.set(x+'4')
            comma_has_written = comma_write.get()
            comma_write.set('0')

def num5_bt():
    equal_clicked = click.get()
    x = input_user.get()
    if len(x)>=15:
        messagebox.showwarning("warning", "  مش مسموح لحضرتك تكتب أرقام أكتر من كده ، \n امسح أرقام وكمل حساباتك تاني \nYou can't write more number after this,\n This is the maximum length of numbers and operators" )
    else:
        if equal_clicked == 'yes':
            x = input_user.get()
            input_user.set('')
            click.set('no')
            print(equal_clicked)
            num5_bt()
        else:
            print("5")
            x = input_user.get()
            input_user.set(x+'5')
            comma_has_written = comma_write.get()
            comma_write.set('0')

def num6_bt():
    equal_clicked = click.get()
    x = input_user.get()
    if len(x)>=15:
        messagebox.showwarning("warning", "  مش مسموح لحضرتك تكتب أرقام أكتر من كده ، \n امسح أرقام وكمل حساباتك تاني \nYou can't write more number after this,\n This is the maximum length of numbers and operators" )
    else:
        if equal_clicked == 'yes':
            x = input_user.get()
            input_user.set('')
            click.set('no')
            print(equal_clicked)
            num6_bt()
        else:
            print("6")
            x = input_user.get()
            input_user.set(x+'6')
            comma_has_written = comma_write.get()
            comma_write.set('0')

def num7_bt():
    equal_clicked = click.get()
    x = input_user.get()
    if len(x)>=15:
        messagebox.showwarning("warning", "  مش مسموح لحضرتك تكتب أرقام أكتر من كده ، \n امسح أرقام وكمل حساباتك تاني \nYou can't write more number after this,\n This is the maximum length of numbers and operators" )
    else:
        if equal_clicked == 'yes':
            x = input_user.get()
            input_user.set('')
            click.set('no')
            print(equal_clicked)
            num7_bt()
        else:
            print("7")
            x = input_user.get()
            input_user.set(x+'7')
            comma_has_written = comma_write.get()
            comma_write.set('0')

def num8_bt():
    equal_clicked = click.get()
    x = input_user.get()
    if len(x)>=15:
        messagebox.showwarning("warning", "  مش مسموح لحضرتك تكتب أرقام أكتر من كده ، \n امسح أرقام وكمل حساباتك تاني \nYou can't write more number after this,\n This is the maximum length of numbers and operators" )
    else:
        if equal_clicked == 'yes':
            x = input_user.get()
            input_user.set('')
            click.set('no')
            print(equal_clicked)
            num8_bt()
        else:
            print("8")
            x = input_user.get()
            input_user.set(x+'8')
            comma_has_written = comma_write.get()
            comma_write.set('0')

def num9_bt():
    equal_clicked = click.get()
    x = input_user.get()
    if len(x)>=15:
        messagebox.showwarning("warning", "  مش مسموح لحضرتك تكتب أرقام أكتر من كده ، \n امسح أرقام وكمل حساباتك تاني \nYou can't write more number after this,\n This is the maximum length of numbers and operators" )
    else:
        if equal_clicked == 'yes':
            x = input_user.get()
            input_user.set('')
            click.set('no')
            print(equal_clicked)
            num9_bt()
        else:
            print("9")
            x = input_user.get()
            input_user.set(x+'9')
            comma_has_written = comma_write.get()
            comma_write.set('0')



#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------





#--------------------------------------------------------------------------------------------------------
#-------------------------------------------------Buttons------------------------------------------------
#--------------------------------------------------------------------------------------------------------


#------------------------------clear_button--------------------------------------------------
clear_button = Button(text='clear',
                   bg='#0066cc',
                   fg='#00ff00',
                   activebackground='#003366',
                   activeforeground='yellow',
                   height=2,
                   width=6,
                   command=clear_bt)
clear_button.place(x=10,y=130)

#--------------------------------plus_button--------------------------------------------------
plus_button = Button(text='+',
                   bg='#0066cc',
                   fg='white',
                   activebackground='#003366',
                   activeforeground='yellow',
                   height=2,
                   width=6,
                   command=plus_bt)
plus_button.place(x=190,y=220)
#------------------------------minus_button-------------------------------------------------
minus_button = Button(text='-',
                   bg='#0066cc',
                   fg='white',
                   activebackground='#003366',
                   activeforeground='yellow',
                   height=2,
                   width=6,
                   command=minus_bt)
minus_button.place(x=190,y=175)
#--------------------------------multiplication_button--------------------------------------------------
multiplication_button = Button(text='x',
                   bg='#0066cc',
                   fg='white',
                   activebackground='#003366',
                   activeforeground='yellow',
                   height=2,
                   width=6,
                   command=multi_bt)
multiplication_button.place(x=190,y=130)
#------------------------------division_button--------------------------------------------------
division_button = Button(text='÷',
                   bg='#0066cc',
                   fg='white',
                   activebackground='#003366',
                   activeforeground='yellow',
                   height=2,
                   width=6,
                   command=divi_bt)
division_button.place(x=130,y=130)

#--------------------------------delete_button--------------------------------------------------
delete_button = Button(text='delete',
                       bg='#0066cc',
                       fg='#00ff00',
                       activebackground='#003366',
                       activeforeground='yellow',
                       height=2,
                       width=6,
                       command=del_bt)
delete_button.place(x=70,y=130)
#--------------------------------equal_button--------------------------------------------------
equal_button = Button(text='=',
                       bg='#99004d',
                       fg='white',
                       activebackground='#4d0026',
                       activeforeground='yellow',
                       height=5,
                       width=6,
                       command=equal_bt)
equal_button.place(x=190,y=265)
#--------------------------------number_7_button--------------------------------------------------
number7_button = Button(text='7',
                        bg='#99004d',
                        fg='white',
                        activebackground='#4d0026',
                        activeforeground='green',
                        height=2,
                        width=6,
                        command=num7_bt)

number7_button.place(x=10,y=175)
#---------------------------------number_8_button-------------------------------------------------
number8_button = Button(text='8',
                        bg='#99004d',
                        fg='white',
                        activebackground='#4d0026',
                        activeforeground='green',
                        height=2,
                        width=6,
                        command=num8_bt)
number8_button.place(x=70,y=175)
#---------------------------------number_9_button---------------------------------------------------------
number9_button = Button(text='9',
                        bg='#99004d',
                        fg='white',
                        activebackground='#4d0026',
                        activeforeground='green',
                        height=2,
                        width=6,
                        command=num9_bt)

number9_button.place(x=130,y=175)
#-----------------------------------number_4_button-----------------------------------------------------------------
number4_button = Button(text='4',
                        bg='#99004d',
                        fg='white',
                        activebackground='#4d0026',
                        activeforeground='green',
                        height=2,
                        width=6,
                        command=num4_bt)
number4_button.place(x=10,y=220)
#----------------------------------number_5_button--------------------------------------------------------------------
number5_button = Button(text='5',
                        bg='#99004d',
                        fg='white',
                        activebackground='#4d0026',
                        activeforeground='green',
                        height=2,
                        width=6,
                        command=num5_bt)

number5_button.place(x=70,y=220)
#---------------------------------number_6_button---------------------------------------------
number6_button = Button(text='6',
                        bg='#99004d',
                        fg='white',
                        activebackground='#4d0026',
                        activeforeground='green',
                        height=2,
                        width=6,
                        command=num6_bt)
number6_button.place(x=130,y=220)
#-----------------------------------number_1_button-----------------------------------------------------------------
number1_button = Button(text='1',
                        bg='#99004d',
                        fg='white',
                        activebackground='#4d0026',
                        activeforeground='green',
                        height=2,
                        width=6,
                        command=num1_bt)

number1_button.place(x=10,y=265)
#----------------------------------number_2_button---------------------------------------------------------------------------------
number2_button = Button(text='2',
                        bg='#99004d',
                        fg='white',
                        activebackground='#4d0026',
                        activeforeground='green',
                        height=2,
                        width=6,
                        command=num2_bt)
number2_button.place(x=70,y=265)
#---------------------------------number_3_button---------------------------------------------
number3_button = Button(text='3',
                        bg='#99004d',
                        fg='white',
                        activebackground='#4d0026',
                        activeforeground='green',
                        height=2,
                        width=6,
                        command=num3_bt)
number3_button.place(x=130,y=265)
#---------------------------------number_0_button---------------------------------------------
number0_button = Button(text='0',
                        bg='#99004d',
                        fg='white',
                        activebackground='#4d0026',
                        activeforeground='green',
                        height=2,
                        width=15,
                        command=num0_bt)
number0_button.place(x=9,y=310)
#---------------------------------comma_button---------------------------------------------
comma_button = Button(text=',',
                        bg='#99004d',
                        fg='white',
                        activebackground='#4d0026',
                        activeforeground='green',
                        height=2,
                        width=6,
                        command=comma_bt)
comma_button.place(x=130,y=310)


#--------------------------------------------------------------------------------------------------------
#-------------------------------------------------Lables-------------------------------------------------
#--------------------------------------------------------------------------------------------------------

screen = Label(window,textvariable= input_user,
               bg='#d9d9d9',
               fg='black',
               height=3,
               width=17,
               anchor=SE,
               padx=5,
               pady=5)
screen.config(font=("Courier", 16))
screen.place(x=8,y=34)

title_programmer = Label(window,text='By Mohamed Emad, Member at IEEE. April 2020', bg='green',fg='white',height=1,width=17)
title_programmer.config(font=("Comic Sans MS", 8))
title_programmer.pack(fill='x')

#------------------------------------------------------------------------------------------------------
#----------------------------------------------programming---------------------------------------------
#------------------------------------------------------------------------------------------------------











window.iconbitmap(r'C:\Users\comp\Desktop\Tkinter\calc.ico')




window.mainloop()
