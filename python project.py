from os import truncate
from tkinter import  *
import pygetwindow as gw
import datetime
import winsound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second
#Initializing variables and paths
aloop = True
loop = False
main_loop = True
start_time = False
stop_time = False
starthourtime = 22
startminutetime = 45
stophourtime = 3
stopminutetime = 30
time_in_am = False
time_in_am1 = False
donotblock = ['Code', 'Edge', 'Chrome', "Mail", "Manager", "[Administrator]"]
host_file_location = r"C:\Windows\System32\drivers\etc\hosts"
host_local_ip = "127.0.0.1"
bot = 0
website_file = r"C:\Users\KimiwaSadat\Desktop\website document.txt"


#Items for Python GUI
win = Tk()
win.geometry('600x900')
win.configure(bg="#74ccff")
win.resizable(1,1)
win.title("Procrasination Bot 3000")
Label(win, text= "Procrasination Anihilator Bot 3000", font= "{Gill Sans MT} 20 bold", bg ="#74ccff").pack()
Label(win, text= "Made by: Kimiwa Sadat", font= " {Gill Sans mt} 10").pack(side=BOTTOM)
Label(win, text="Blocking the Following Websites:", font="{Gill Sans MT} 15 ", bg ="#74ccff" ).pack(side=TOP)
Sites = Text(win, font="{Times New Roman} 10", height=2, width=70,wrap=WORD, padx=5, pady= 60 )
pm_text =Label(win, text="PM", font="{Gill Sans MT} 12", bg="#74ccff")
pm_text1 =Label(win, text="PM", font="{Gill Sans MT} 12", bg="#74ccff")
am_text =Label(win, text="AM", font="{Gill Sans MT} 12", bg="#74ccff")
am_text1 =Label(win, text="AM", font="{Gill Sans MT} 12", bg="#74ccff")
Sites.place(x=80,y=100)


#Defines all the functions for the buttons

def Blocker():
    website_lists = Sites.get(1.0,END)
    website = list(website_lists.split(",",))
    with open(website_file, "r+") as users_file:
        hosts_content =users_file.read()
        for websites in website:

            if websites in hosts_content:
                p = websites
                print(f"Blocked the site name {p} already")
                Label(win, text=f"Added {p} already", font="{Gill Sans MT Condensed} 15", fg="red",bg="#74ccff",  height=2,width=30).place(x=190,y=250)
                pass
            else:
                p = websites
                users_file.write( websites)
                Label(win, text=f"Blocked {p} ", font= "{Gill Sans MT Condensed} 15", fg= "red", bg="#74ccff", height=1,width=30, pady=10).place(x=190, y=250 )

def pmoram1():
    global time_in_am1
    global starthourtime
    global startminutetime
    global stophourtime
    global stopminutetime
    timestartget = time_input_end.get(1.0,END)
    listtimepm = list(timestartget)
    hourtimepm = ""
    for x in listtimepm:
        if x == ":":
            break
        hourtimepm += x

    print(hourtimepm)

    print(listtimepm)
    print(listtimepm[-3:-1])
    timepmmin =""
    for x in listtimepm[-3:-1]:
        timepmmin += x
    print(timepmmin)
    hourmst= int(hourtimepm) + 12
    stophourtime = hourmst
    stopminutetime = int(timepmmin)
    if time_in_am1 == True:
        am_text1.config(text="")
        time_in_am1 = False
    else:
        pm_text1.config(text="PM")
        pm_text1.place(x=297, y=555)

    return hourmst

def pmoram():
    global time_in_am
    global starthourtime
    global startminutetime
    timestartget = time_input.get(1.0,END)
    listtimepm = list(timestartget)
    hourtimepm = ""
    for x in listtimepm:
        if x == ":":
            break
        hourtimepm += x

    print(hourtimepm)

    print(listtimepm)
    print(listtimepm[-3:-1])
    timepmmin =""
    for x in listtimepm[-3:-1]:
        timepmmin += x
    print(timepmmin)
    hourmst= int(hourtimepm) + 12
    starthourtime = hourmst
    startminutetime = int(timepmmin)
    if time_in_am == True:
        am_text.config(text="")
        time_in_am = False
    else:
        pm_text.config(text="PM")
        pm_text.place(x=300,y=412)

    return hourmst
def am():
    global time_in_am
    global starthourtime
    global startminutetime
    timestartget = time_input.get(1.0,END)
    list_time_am = list(timestartget)
    hour_time_am = ""
    for x in list_time_am:
        if x == ":":
            break
        hour_time_am += x

    print(hour_time_am)

    print(list_time_am)
    print(list_time_am[-3:-1])
    time_am_min =""
    for x in list_time_am[-3:-1]:
        time_am_min += x
    print(time_am_min)
    starthourtime = hour_time_am
    startminutetime = time_am_min
    if time_in_am == False:
        pm_text.config(text="")
        time_in_am = True
    else:
        am_text.config(text="AM")
        am_text.place(x=300, y=390)


def am1():
    global time_in_am1
    global stophourtime
    global stopminutetime
    timestartget = time_input_end.get(1.0,END)
    list_time_am = list(timestartget)
    hour_time_am = ""
    for x in list_time_am:
        if x == ":":
            break
        hour_time_am += x

    print(hour_time_am)

    print(list_time_am)
    print(list_time_am[-3:-1])
    time_am_min =""
    for x in list_time_am[-3:-1]:
        time_am_min += x
    print(time_am_min)
    stophourtime = hour_time_am
    stopminutetime = time_am_min
    if time_in_am1 == False:
        pm_text1.config(text="")
        time_in_am1 = True
    else:
        am_text1.config(text="AM")
        am_text1.place(x=295, y=535)


def submitstarttime():
    global start_time
    global starthourtime
    global startminutetime
    start_time = True
    print(start_time)


def submitstoptime():
    global stop_time

    global starthourtime
    global startminutetime
    global stophourtime
    global stopminutetime
    stop_time = True
    print(stop_time)

def addprogramtolist():
    block_list = application_block.get(1.0,"end-1c")
    split_application_into_list = block_list.split()
    print(split_application_into_list[-1])
    donotblock.append(split_application_into_list[-1])

#Python GUI text input and labels
time_input = Text(win, font="{Times New Roman} 15", height=1, width=5,wrap=WORD, padx=5, pady= 10 )
time_input.place(x=230, y=400)
Label(win, text="What time do you want this to start", font="{Gill Sans MT} 15", bg ="#74ccff" ).place(x=140, y=350)
Button(win, text="Submit Start Time", font= "Galano 12", pady=2, command= submitstarttime ,width = 15, bg = '#b3ff99', activebackground = '#2db2ff').place(x=390, y=400)
input_am_button = Button(win, text="AM", font= "Galano 15", pady=2, command= am ,width = 4, bg = '#94ff67', activebackground = '#74ccff').place(x=230, y=450)
input_startbutton =Button(win, text="PM", font= "Galano 15", pady=2, command= pmoram ,width = 4, bg = '#94ff67', activebackground = '#74ccff').place(x=290, y=450)


Label(win, text="What time do you want this to end", font="{Gill Sans MT} 15", bg ="#74ccff" ).place(x=140, y=500)
time_input_end = Text(win, font="{Times New Roman} 15", height=1, width=5,wrap=WORD, padx=5, pady= 10 )
Button(win, text="Submit Stop Time", font= "Galano 12", pady=2, command= submitstoptime ,width = 15, bg = '#b3ff99', activebackground = '#74ccff').place(x=390, y=540)
time_input_end.place(x=230, y=540)
input_end_text = Button(win, text="PM", font= "Galano 15", pady=2, command= pmoram1 ,width = 4, bg = '#94ff67', activebackground = '#2db2ff').place(x=290, y=590)
input_am_button2 = Button(win, text="AM", font= "Galano 15", pady=2, command= am1 ,width = 4, bg = '#94ff67', activebackground = '#2db2ff').place(x=230, y=590)

Label(win, text="What applications do you need active", font="{Gill Sans MT} 15", bg ="#74ccff" ).place(x=140, y=640)
application_block = Text(win, font="{Times New Roman} 15",height=3, width=40,wrap=WORD, padx=5, pady= 12)
application_block.place(x=93,y=670)
Button(win, text="Add Programs", font= "Galano 12", pady=2, command=addprogramtolist  ,width = 15, bg = '#b3ff99', activebackground = '#74ccff').place(x=190, y= 800)
time_input_end.place(x=230, y=540)

def qut():
    global aloop
    global main_loop
    main_loop = False
    aloop = False
    print("Quit button pressed, exit application to start the blocking process")
    

blockbutton = Button(win, text="Eradicate", font= "Galano 18", pady=3, command= Blocker ,width = 10, bg = '#42ff00', activebackground = 'red').place(x=210, y=300)
quitbutton = Button(win,text="Quit",font="Galano 15", pady=5, width = 10, bg = 'red', command= qut).place(x=5 , y=850)


#main Functions for blocking and unblocking websites and programs
def application_killer():
    global bot
    bot = 0
    while bot != 3:
        for things in gw.getAllTitles():
            if things != "":
                listofapplication = things.split()

                if listofapplication[-1] in donotblock or listofapplication[-1] == "Code":
                    print(f"I will not close {things[0]}")
                else:
                    print(f"Closing: {things}")
                    try:
                        print(gw.getWindowsWithTitle(f"{things}")[0])
                        windowname = gw.getWindowsWithTitle(f"{things}")[0]
                    except IndexError:
                        pass
                    try:
                        windowname.close()
                    except gw.PyGetWindowException:
                        pass
        bot += 1
global check_if_time_is_up
check_if_time_is_up = False
def block_function():
    
    list_of_websites_blocked = []
    add_websites_to_hosts = True
    
    importantLoop = True
    while importantLoop == True:
        global check_if_time_is_up
        if add_websites_to_hosts == True:
            winsound.Beep(frequency, duration)
            if stop_time == True and start_time == True:
                current_time = datetime.datetime.now()
                print(current_time)
                print(starthourtime)
                print(startminutetime)
                print(stophourtime)
                print(stopminutetime)
                if current_time.hour == starthourtime and current_time.minute == startminutetime or  current_time.minute <= startminutetime:
                    print("worktime")
                    with open(website_file, 'r+') as docfile:
                            
                        print("in website list file")
                        global website_list 
                        website_list= docfile.readlines()
                    with open(host_file_location, 'r+') as file:
                        print("in the host file")
                        content = file.readlines()
                        for website in website_list:
                            print("in loop of website in website list")
                            if website == content:
                                print(f"Program did not {website}")
                                pass
                            else:
                                print(f"Program did add {website}")
                                #adding host local ip to the website domain
                                file.write(host_local_ip+ " "+ website + "\n")
                        add_websites_to_hosts = False
                        check_if_time_is_up = True
        
        
        while check_if_time_is_up == True:
            if check_if_time_is_up == True:
                
                current_time = datetime.datetime.now()
                
                application_killer()
                if current_time.hour == stophourtime and current_time.minute == stopminutetime:
                    print("hour and minute conditions are met")
                    with open(website_file,"r+") as web:
                        listelement = web.readlines()
                        for element in listelement:
                            list_of_websites_blocked.append(host_local_ip+ " "+ element.strip('\n'))
                            
                            print(list_of_websites_blocked)
                        with open(host_file_location, 'r+') as file:
                            print("In the host file")
                            content =file.readlines()
                            file.seek(0)
                            for line in content:
                                print("Checking line in host file and the website file")
                                for thing in list_of_websites_blocked:
                                    print("Checking if the host and the website conditions meet")
                                    print(line.strip(), thing.strip())
                                    if line.strip() == thing.strip():
                                        
                                        file.truncate()
                                        print("Remove this item from the host file")
                        
                    print("done")
                    #two beeps indicating that the process is complete
                    winsound.Beep(frequency, duration)
                    winsound.Beep(frequency, duration)
                    quit()

#Main loop for the tkinter window
while aloop is True:
    if main_loop == True:
        win.mainloop()
    print("Application is closed")
    block_function()
    break






