#--------- modules--------
from math import cos,sin,tan,sqrt
from numpy import exp,log,arctan,arccos,pi
import matplotlib.pyplot as plt
import numpy as np
from colorama import Fore, Style
#------initialisations--------
Q=[]
time=[]
I=[]
Volt=[]
ukval=[]
kval=[]
Values=dict()
list1=['Inductance','Capacitance','Resistance','Peak Voltage','RMS Voltage','Peak Current','RMS Current','Angular Frequency of Source','Resonance Angular Frequency','Phase Difference','Impedance','Inductive Reactance','Capacitive Reactance','Average Power Delivered','Q-factor']


#---------functions-------------
#------time dependent-----------------

def graph(A,B,title,xl,yl):
    plt.title(title) 
    plt.xlabel(xl)
    plt.ylabel(yl)
    plt.scatter(A,B)
    plt.plot(A,B,'r-')
    plt.grid()
    plt.show()

def check(inp):
    r=2
    try:
        inp=str(inp)
        if inp=='y':
            r=1
        elif inp=='n':
            r=0
        else:
            print('Invalid input.')
    except:
            print('Invalid input.')
    return r
            
def RC(r,c,v,nu,n):
    
    T=1/nu
    menu=float(input(" Enter 1 for charging and 2 for discharging. "))
    
    if menu==1:
        
        t=0
        while t<=n*T :                                     # For charging.
            
            t+=(n/10000)
            q = v*c*(1-exp(-t/(r*c)))                        
            i = (v/r)*exp(-t/(r*c))
            emf = v*(1-exp(-t/(r*c)))

            I.append(i)
            Volt.append(emf)
            time.append(t)
            Q.append(abs(q))                                     


    else:
        
        qo = float(input(" Enter the value of charge when the capacitor is fully charged (in C) "))
        
        t=0
        while t<=n*T :                                   #For discharging.
            
            t+=n/10000
            q = qo*(exp(-t/(r*c)))
            i = (-qo/(r*c))*exp(-t/(r*c))
            emf = (qo/c)*(exp(-t/(r*c)))
            
            I.append(i)
            Volt.append(emf)
            time.append(t)
            Q.append(q)
            
    graph(time,Q,'q-t graph','t','q(t)')
    graph(time,I,'I-t graph','t','I(t)')
    graph(time,Volt,'V-t graph','t','V(t)')

    I.clear()
    Q.clear()
    Volt.clear()
    time.clear()
            

    return Q,I,Volt,time

def LR(r,l,v,nu,n):

    VL = []
    VR = []
    
    T=1/nu
    menu=float(input(" Enter 1 for charging and 2 for discharging. "))
    
    if menu==1:
        t=0
        while t<=n*T  :                                      # For charging.
            
            t+=(n/10000)
            i = (v/r)*(1-exp(-t*r/(l)))
            el = v*(exp(-t*r/l))
            er = v*(1-exp(-t*r/l))
            
            I.append(i)
            VL.append(el)
            VR.append(er)
            time.append(t)

    else:
        
        print(" The charge doesn't get stored in neither Resistor nor Inductor. ")
        t=0
        while t<=n*T :                                    # For discharging.

            t+=n/10000
            i = (v/r)*exp(-t*r/l)
            el = -v*(exp(-t*r/l))
            er = v*(exp(-t*r/l))
            
            I.append(i)
            VL.append(el)
            VR.append(er)            
            time.append(t)
            
            
            
    graph(time,I,'I-t graph','t','I(t)')
    graph(time,VL,'V across L-t graph','t','Vl(t)')
    graph(time,VR,'V across R-t graph','t','Vr(t)')

    I.clear()
    VL.clear()
    VR.clear()            
    time.clear()


def LC(l,c,nu,n):

    T = 1/nu
    w = 1/((l*c)**0.5)
    qo = float(input(" Enter the value of charge when capacitor is fully charged. "))
    
    t=0
    while t<=n*T :# LC OSCILLATIONS.

        t+=n/10000
        q = qo*(cos(w*t))
        i = -qo*w*(sin(w*t))
        e = qo/c * (cos(w*t))
        
        Q.append(q)
        I.append(i)
        Volt.append(e)
        time.append(t)
        
        
        
    graph(time,Q,'q-t graph','t','q(t)')
    graph(time,I,'I-t graph','t','I(t)')
    graph(time,Volt,'V-t graph','t','V(t)')

    Q.clear()
    I.clear()
    Volt.clear()
    time.clear()

        
def LCR(l,c,r,nu,n):                                              # LCR Damping.
    
    VL = []
    VC = []
    VR = []
    
    
    T = 1/nu
    w = ((1/(l*c))-(r/(2*l)**2))**2
    qo = float(input(" Enter the value of charge when capacitor is fully charged. "))
    
    t=0
    while t<=n*T :                                        # LC OSCILLATIONS.
        
        t+=n/10000
        q = qo*(exp(-r*t/(2*l))*(cos(w*t)))
        i = (-qo*exp(-r*t/(2*l)))*((w*sin(w*t))-((r/(2*l))*cos(w*t)))
        el = (qo*exp(-r*t/(2*l)))*(((w*sin(w*t))*((r/(2*l))+1))-(cos(w*t)*(w**2 - (r/(2*l))**2)))
        ec = (qo/c)*exp(-r*t/(2*l))*(cos(w*t))
        er = i/r


        
        Q.append(q)
        I.append(i)
        VL.append(el)
        VC.append(ec)
        VR.append(er)
        time.append(t)

    graph(time,Q,'Q-t graph','t','Q(t)')
    graph(time,I,'I-t graph','t','I(t)')
    graph(time,VL,'V across L-t graph','t','Vl(t)')
    graph(time,VC,'V across C-t graph','t','Vc(t)') 
    graph(time,VR,'V across R-t graph','t','Vr(t)')

    Q.clear()
    I.clear()
    VL.clear()
    VC.clear()
    VR.clear()
    time.clear()

#------------------------non time dependent--------
def inp2():
    global ukval
    for i in range (0,len(list1)):
        print(i+1,'.',list1[i])
    print('Please enter the serial number of values known to you and then type its numerical value when further prompted')
    print("If you do not wish to enter any more values then type 'stop' ")
    while True:
        x=input('Serial Number:') 
        try:
            x=int(x)
            x=x
            if x in range(1,16):
                x=x
            else:
                print('Input out of range. Please type a number in the given range')
                continue
        except:
            if x=='stop':
                break
            else:
                print('Invalid input')
                continue
        if x==8 or x==9:
            print(Fore.CYAN +(list1[x-1]))
            print(Style.RESET_ALL) 
            val=input('Numerical value as a multiple of pi:')
            try:
                val=float(val)
                val=pi*val
            except:
                print('Invalid Input')
                continue
            Values[list1[x-1]]=val
            kval.append(list1[x-1])
        elif x!=8 or x!=9:
            print(Fore.CYAN +(list1[x-1]))
            print(Style.RESET_ALL) 

            val=input('Numerical value:')
            try:
                val=float(val)
                val=val
            except:
                print('Invalid Input')
                continue
            Values[list1[x-1]]=val
            kval.append(list1[x-1])

    print('')    
          
    for i in range (0,len(list1)):
        if list1[i] not in kval:
            print(i+1,'.',list1[i])

        
    print('Please enter the serial number of the values you want to find:')
    print("If you do not wish to enter any more values then type 'stop' ")
    print("If you wish to find all the values then type 'all ")

    while True:
        x=input('Serial Number:') 
        try:
            x=int(x)
        except:
            if x=='stop':
                break
            elif x=='all':
                ukval=list1
                break
            else:
                print('Invalid input')
                continue
        ukval.append(list1[x-1]) # Errrrrooorrrr

    for i in list1:    
        if i not in kval:
            Values[i]=''
    print('')
    return Values


def calc2(Values):
    count=0
    while count<=5:          
        count=count+1
        if Values['Inductance']=='':
            if Values['Inductive Reactance']!='' and Values['Angular Frequency of Source']!='':
                Values['Inductance']=(Values['Inductive Reactance'])/(Values['Angular Frequency of Source'])
            elif Values['Q-factor']!='' and Values['Resistance']!='' and Values['Capacitance']!='':
                Values['Inductance']=((Values['Q-factor'])**2)*((Values['Resistance'])**2)*(Values['Capacitance'])
            elif Values['Resonance Angular Frequency']!='' and Values['Capacitance']!='':
                Values['Inductance']=1/((Values['Resonance Angular Frequency'])**2)*(Values['Capacitance'])
            
                
        if Values['Capacitance']=='':
            
            if Values['Capacitive Reactance']!='' and Values['Angular Frequency of Source']!='':
                Values['Capacitance']=1/((Values['Capacitive Reactance'])*(Values['Angular Frequency of Source']))
            elif Values['Q-factor']!='' and Values['Resistance']!='' and Values['Inductance']!='':
                Values['Capacitance']=(Values['Inductance'])/((Values['Q-factor'])**2)*((Values['Resistance'])**2)
            elif Values['Resonance Angular Frequency']!='' and Values['Inductance']!='':
                Values['Capacitance']=1/((Values['Resonance Angular Frequency'])**2)*(Values['Inductance'])
            
                
        if Values['Resistance']=='':

            if Values['Impedance']!='' and Values['Capacitive Reactance']!='' and Values['Inductive Reactance']!='':
                Values['Resistance']=sqrt((Values['Impedance'])**2 - ((Values['Capacitive Reactance']) - (Values['Inductive Reactance']))**2)
            elif Values['Inductive Reactance']!='' and Values['Capacitive Reactance']!='' and Values['Phase Difference']!='':
                Values['Resistance']= ((Values['Capacitive Reactance'])-(Values['Inductive Reactance']))/tan(Values['Phase Difference'])
            elif Values['Q-factor']!='' and Values['Inductance']!='' and Values['Capacitance']!='':
                Values['Resistance']=sqrt(Values['Inductance'])/((Values['Q-factor'])*sqrt(Values['Capacitance']))
            
                
        if Values['Peak Voltage']=='':
            if Values['Peak Current']!='' and Values['Impedance']!='':
                Values['Peak Voltage']=(Values['Peak Current'])*(Values['Impedance'])
        if Values['RMS Voltage']=='':
            if Values['Peak Voltage']!='':
                Values['RMS Voltage']=(Values['Peak Voltage'])/(sqrt(2))
           
        
        if Values['Angular Frequency of Source']=='':
            
            if Values['Inductive Reactance']!='' and Values['Inductance']!='':
                Values['Angular Frequency of Source']=(Values['Inductive Reactance'])/(Values['Inductance'])
            elif Values['Capacitive Reactance']!='' and Values['Capacitance']!='':
                Values['Angular Frequency of Source']=1/((Values['Capacitive Reactance'])*(Values['Capacitance']))
            
            
        if Values['Peak Current']=='':
            if Values['Peak Voltage']!='' and Values['Impedance']!='':
                Values['Peak Current']=(Values['Peak Voltage'])/(Values['Impedance'])
        if Values['RMS Current']=='':
            if Values['Peak Current']!='':
                Values['RMS Current']=(Values['Peak Current'])/(sqrt(2))    
        
        if Values['Resonance Angular Frequency']=='':
            if Values['Inductance']!='' and Values['Capacitance']!='':
                Values['Resonance Angular Frequency']=1/sqrt((Values['Inductance'])*(Values['Capacitance']))
            
                    
        if Values['Phase Difference'] =='':
            if Values['Inductive Reactance']!='' and Values['Capacitive Reactance']!='' and Values['Resistance']!='':
                Values['Phase Difference']=arctan(((Values['Capacitive Reactance'])-(Values['Inductive Reactance']))/(Values['Resistance']))
            elif Values['Average Power Delivered']!='' and Values['Peak Voltage']!='' and Values['Peak Current']!='':
                Values['Phase Difference']=arccos((2*(Values['Average Power Delivered']))/(Values['Peak Voltage']*(Values['Peak Current'])))
            
            
        if Values['Impedance']=='':
            if Values['Resistance']!='' and Values['Inductive Reactance']!='' and Values['Capacitive Reactance']!='':
                Values['Impedance']=sqrt((Values['Resistance'])**2 + ((Values['Capacitive Reactance'])-(Values['Inductive Reactance']))**2)
            elif  Values['Peak Voltage']!='' and Values['Peak Current']!='':
                Values['Impedance']=Values['Peak Voltage']/(Values['Peak Current'])
            
        
        if Values['Inductive Reactance']=='':
            if Values['Inductance']!='' and Values['Angular Frequency of Source']!='':
                Values['Inductive Reactance']=(Values['Inductance'])*(Values['Angular Frequency of Source'])
            elif Values['Capacitive Reactance']!='' and Values['Impedance']!='' and Values['Resistance']!='':
                Values['Inductive Reactance']= (Values['Capacitive Reactance']) - sqrt((Values['Impedance'])**2 - (Values['Resistance'])**2)
            elif Values['Capacitive Reactance']!='' and Values['Resistance']!='' and Values['Phase Difference']!='':
                Values['Inductive Reactance']= (Values['Resistance'])*(tan(Values['Phase Difference'])) + (Values['Capacitive Reactance'])
            
                
        if Values['Capacitive Reactance']=='':
            if Values['Capacitance']!='' and Values['Angular Frequency of Source']!='':
                Values['Capacitive Reactance']=1/((Values['Capacitance'])*(Values['Angular Frequency of Source']))
            elif Values['Impedance']!='' and Values['Resistance']!='' and Values['Inductive Reactance']!='':
                Values['Capacitive Reactance']=Values['Inductive Reactance'] + sqrt((Values['Impedance'])**2 - (Values['Resistance'])**2)
            elif Values['Inductive Reactance']!='' and Values['Phase Difference']!='' and Values['Resistance']!='':
                Values['Capacitive Reactance']=Values['Inductive Reactance'] - (Values['Resistance'])*(tan(Values['Phase Difference']))
            
                
        if Values['Average Power Delivered']=='':
            if Values['Peak Voltage']!='' and Values['Peak Current']!='' and Values['Phase Difference']!='':
                Values['Average Power Delivered']= ((Values['Peak Voltage'])*(Values['Peak Current'])*cos(Values['Phase Difference']))/2
            
                
        if Values['Q-factor']=='':
            if Values['Inductance']!='' and Values['Capacitance']!='' and Values['Resistance']!='':
                Values['Q-factor']=(1/(Values['Resistance']))*(sqrt((Values['Inductance'])/(Values['Capacitance'])))

    return Values

def output2(Values):
    print('')
    print('Characteristics of the Circuit:')
    print('')

    if Values['Peak Voltage']!='' and Values['Peak Current']!='' and  Values['Angular Frequency of Source']!='' and 'Peak Voltage' in ukval:
        print('The variation of Voltage and Current is as follows:')
        print('')
        print('V = ',Values['Peak Voltage'],'sin(',Values['Angular Frequency of Source'],'t)')
        print('I = ',Values['Peak Current'],'sin(',Values['Angular Frequency of Source'],'t + ',Values['Phase Difference'],')')
        print('')
    elif Values['Peak Voltage']!='' and Values['Angular Frequency of Source']!='' and 'Peak Voltage' in ukval:
        print('V = ',Values['Peak Voltage'],'sin(',Values['Angular Frequency of Source'],'t)')
        print('Peak Voltage=',Values['Peak Voltage'],'Volts')
        print('')
    elif Values['Peak Voltage']!='' and 'Peak Voltage' in ukval:
        print('Peak Voltage=',Values['Peak Voltage'],'Volts')
        print('')
    elif Values['Peak Current']!='' and Values['Angular Frequency of Source']!='' and 'Peak Current' in ukval:
        print('I = ',Values['Peak Current'],'sin(',Values['Angular Frequency of Source'],'t + ',Values['Phase Difference'],')')
        print('Peak Current=',Values['Peak Current'],'Amperes')
        print('')
    elif Values['Peak Current']!='' and 'Peak Current' in ukval:
        print('Peak Current=',Values['Peak Current'],'Amperes')
        print('')

    if Values['RMS Voltage']!='' and 'RMS Voltage' in ukval:
        print('RMS Voltage=',Values['RMS Voltage'],'Volts')
        print("")
    if Values['RMS Current']!='' and 'RMS Current' in ukval:
        print('RMS Current=',Values['RMS Current'],'Amperes')
        print('')
        
    if Values['Inductance']!='' and 'Inductance' in ukval:  
        print('Inductance= ',Values['Inductance'],'Henry')
        print('')

    if Values['Capacitance']!='' and 'Capacitance' in ukval:
        print('Capacitance= ',Values['Capacitance'],'Farad')
        print('')

    if Values['Resistance']!=''and 'Resistance' in ukval:
        print('Resistance= ',Values['Resistance'],'Ohms')
        print('')

    if Values['Angular Frequency of Source']!=''and 'Angular Frequency of Source' in ukval:
        print('Angular Frequency of Source= ',Values['Angular Frequency of Source'],'Radians per second')
        print('Frequency of Source= ',(Values['Angular Frequency of Source'])/(2*pi),'Hertz')
        print('')

    if Values['Resonance Angular Frequency']!='' and 'Resonance Angular Frequency' in ukval:
        print('Resonance Angular Frequency=',Values['Resonance Angular Frequency'],'Radians per second')
        print('Resonance Frequency=',(Values['Resonance Angular Frequency'])/(2*pi),'Hertz')
        print('')

    if Values['Phase Difference']!='' and 'Phase Difference' in ukval:
        print('Phase difference between Volatage and Current Phasor= ',Values['Phase Difference'],'Radians')
        if Values['Phase Difference']>0:
            print('Current Leads the Voltage ')
        elif Values['Phase Difference']<0:
            print('Voltage Leads the Current')
        elif Values['Phase Difference']==0:
            print('Current and Voltage are in phase')
        print('')
        print('Power factor= ',cos(Values['Phase Difference']))
        print('')

    if Values['Impedance']!='' and 'Impedance' in ukval:
        print('Impedance= ',Values['Impedance'],'Ohms')
        print('')

    if Values['Inductive Reactance']!='' and 'Inductive Reactance' in ukval:
        print('Inductive Reactance= ',Values['Inductive Reactance'],'Ohms')
        print('')

    if Values['Capacitive Reactance']!='' and 'Capacitive Reactance' in ukval:
        print('Capacitive Reactance= ',Values['Capacitive Reactance'],'Ohms')
        print('')

    if Values['Average Power Delivered']!='' and 'Average Power Delivered' in ukval:
        print('Average Power Delivered=',Values['Average Power Delivered'],'Watts')
        print('')

    if Values['Q-factor']!='' and 'Q-factor' in ukval:
        print('Q-factor=',Values['Q-factor'])
        
    print('')
            
    if Values['Inductance']=='' or Values['Capacitance']=='' or Values['Resistance']=='' or Values['Peak Voltage']=='' or Values['Angular Frequency of Source']=='' or Values['Peak Current']=='' or Values['Resonance Angular Frequency']=='' or Values['Phase Difference']=='' or Values['Impedance']=='' or Values['Inductive Reactance']=='' or Values['Capacitive Reactance']=='' or Values['Average Power Delivered']=='' or Values['Q-factor']=='':
        print('Data Inadequate to find:')
    if Values['Inductance']==''and 'Inductance' in ukval:
        print('Inductance')
    if Values['Capacitance']==''and 'Capacitance' in ukval:
         print('Capacitance')
    if Values['Resistance']==''and 'Resistance' in ukval:
        print('Resistance')
    if Values['Peak Voltage']==''and 'Peak Voltage' in ukval:
         print('Peak Volatge of the Circuit')
         print('RMS Voltage of the Circuit')
    if Values['Angular Frequency of Source']==''and 'Angular Frequency of Source' in ukval:
        print('Angular Frequency of Source')
    if Values['Peak Current']=='' and 'Peak Current' in ukval:
        print('Peak Current of the Circuit')
        print('RMS Current of the Circuit')
    if Values['Resonance Angular Frequency']==''and 'Resonance Angular Frequency' in ukval:
        print('Resonance Angular Frequency')
        print('Resonance Frequency')
    if Values['Phase Difference']==''and 'Phase Difference' in ukval:
        print('Phase Difference between Voltage and Current Phasor')
        print('Power Factor of the circuit')
    if Values['Impedance']==''and 'Impedance' in ukval:
        print('Impedance of the Circuit')
    if Values['Inductive Reactance']=='' and 'Inductive Reactance' in ukval:
        print('Inductive Reactance')
    if Values['Capacitive Reactance']==''and 'Capacitive Reactance' in ukval:
        print('Capacitice Reactance')
    if Values['Average Power Delivered']==''and 'Average Power Delivered' in ukval:
        print('Average Power Delivered')
    if Values['Q-factor']==''and 'Q-factor' in ukval:
        print('Q-factor')

def graphs2(Values):
    #PHASOR DIAGRAM PLOT
    # VOLTAGE PHASOR
    x = np.linspace(-0.5,0.5,100)

    y = Values['Peak Voltage']*( np.sin((Values['Angular Frequency of Source'])*x))


    # setting the axes at the centre
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    # plot the function 
    plt.plot(x,y, 'b', label='Voltage Phasor')

    plt.title('Phasor Diagram')
    plt.legend(loc='upper left')
    plt.xlabel('t')
    plt.ylabel('V')
    # show the plot
    plt.show()

    #CURRENT PHASOR
    x = np.linspace(-0.5,0.5,100)

    y = Values['Peak Voltage']*( np.sin((Values['Angular Frequency of Source'])*x + Values['Phase Difference']))


    # setting the axes at the centre
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    # plot the function
    plt.plot(x,y, 'r', label='Current Phasor')

    plt.title('Phasor Diagram')
    plt.legend(loc='upper left')
    plt.xlabel('t')
    plt.ylabel('I')
    # show the plot
    plt.show()




#------------------------menu driven part-------------
    


while True:

    print(" \n\t\t\t *********** AC CIRCUITS ********** \t\t\t\n ")
    print(" \n\t\t ******************* MENU ********************** \t\n ")
    print(" 1. When charge (q) is time dependent. ",'\n',"2. When charge (q) is not time dependent. ",'\n',"3. Quit\n")
    execu = int(input(" Enter the Case Number you want to execute. "))

    if execu == 1:
        print(" \n\t\t\t TIME DEPENDENCE \t\t\t\t\t\n ")
        print(" \t Time Dependence Cases for Various Circuits. \t\t\t\t\t\n ")
        print(" 1. Time dependence on 'q' for R-C circuit. ",'\n',"2. Time dependence on 'q' for L-R Circuit ",'\n',"3. Time dependence on 'q' for L-C Circuit. ",'\n',"4. Time dependence on 'q' for L-C-R Circuit. ",'\n')
        doingthis = int(input(" Enter the case number you would like to execute. "))
    
        if doingthis == 1:
            r=1
            while r!=0:
                print(" \n\t\t\t *********** R-C CIRCUIT ********** \t\t\t\n ")
                r = float(input(" Enter the value of Resistance of wire in Ohms. "))
                c = float(input(" Enter the value of Capacitance of Capacitor in F. "))
                v = float(input(" Enter the value of Voltage of Battery attached in the circuit in Volts. "))
                nu = float(input(" Enter the value of frequency of the source in Hz "))
                n = float(input(" Enter the number of cycles. "))
                RC(r,c,v,nu,n)
                inp=input(' Do you wish to continue with the RC ciruit (y/n)? ')
                r=check(inp)
        
        elif doingthis == 2:
            r=1
            while r!=0:
                print(" \n\t\t\t *********** L-R CIRCUIT ********** \t\t\t\n ")
                r = float(input(" Enter the value of Resistance of wire in Ohms. "))
                l = float(input(" Enter the value of Inductance of Inductor in Henry. "))
                v = float(input(" Enter the value of Voltage of Battery attached in the circuit in Volts. "))
                nu = float(input(" Enter the value of frequency of the source in Hz "))
                n = float(input(" Enter the number of cycles. "))
                LR(r,l,v,nu,n)
                inp=input(' Do you wish to continue with the LR ciruit (y/n)? ')
                r=check(inp)
        
        elif doingthis == 3:
            r=1
            while r!=0:
                print(" \n\t\t\t *********** L-C CIRCUIT ********** \t\t\t\n ")
                print(' This is for an LC circuit without damping. There is no source voltage.')
                print(' The graph will show LC osccilations.')
                l = float(input(" Enter the value of Inductance of Inductor in Henry. "))
                c = float(input(" Enter the value of Capacitance of Capacitor in F. "))
                nu = float(input(" Enter the value of frequency of the source in Hz "))
                n = float(input(" Enter the number of cycles. "))
                LC(l,c,nu,n)
                inp=input(' Do you wish to continue with the LC ciruit (y/n)? ')
                r=check(inp)
        
        elif doingthis == 4:
            r=1
            while r!=0:
                print(" \n\t\t\t *********** L-C-R CIRCUIT ********** \t\t\t\n ")
                print(' This is for an LCR circuit which has damping. There is no source voltage.')
                print(' The graph will show LCR osccilations with damping.')
                l = float(input(" Enter the value of Inductance of Inductor in Henry. "))
                c = float(input(" Enter the value of Capacitance of Capacitor in F. "))
                r = float(input(" Enter the value of Resistance of wire in Ohms. "))
                nu = float(input(" Enter the value of frequency of the source in Hz "))
                n = float(input(" Enter the number of cycles. "))
                LCR(l,c,r,nu,n)
                inp=input(' Do you wish to continue with the LCR ciruit (y/n)? ')
                r=check(inp)


    if execu == 2:
        print(" \n\t\t\t *********** Series LCR Circuit ********** \t\t\t\n ")
        print('')
        print('We will be finding different characteristic quantities of a series LCR circuit using the data provided.') 
        print('When prompted by the program, enter the quantities known to you and the ones you want to find.')
        print('')
        dictval=inp2()
        dictval2=calc2(dictval)
        output2(dictval2)
        graphs2(dictval)
        

    if execu == 3:
        break
    
