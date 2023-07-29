#----------------------------------------------------------------------------------------------------------------------------------------#
# THIS WAS THE REAL CODE I USED TO CREATE THE GITHUB REPO:                                                                               #            
# https://github.com/1darshanpatil/foundMyOldPomodoroProject/blob/main/main.py                                                           #          
# ^ HOWEVER, THIS CODE LOOKS TOO UGLY TO BE READABLE. SO IN MY SPARE TIME, I DECIDED                                                     #
# TO USE CLASS OBJECTS AND ADD `ALERT SOUNDS`. PLEASE NOTE THAT I HAVE USED WINSOUND, SO IT WILL ONLY WORK ON WINDOWS (NOT LINUX).       #
#                                                                                                                                        #
#                                                                                                                    EDITED: 29-07-2023  #
#----------------------------------------------------------------------------------------------------------------------------------------#


#5Min of work
    #1min of break
    #1-tick mark
#5Min of work
    #1min of break
    #2-tick mark
#5Min of work
    #1min of break
    #3-tick mark
#5Min of work
    #2min of break
    #Success 
                                 #--------------------------------------------------#
                                 # Make changes only to the below three variables.  #
                                 #--------------------------------------------------#
work_time =  15     
break_time = 3
final_break_time = 5






#----------------------------------------------------------------------------------------------------------------------------------#
#__________________________________________________________________________________________________________________________________#
#------------------------------------------------------------------------------------------------------------------------#
#                                       Do not make changes for below lines                                              #
#------------------------------------------------------------------------------------------------------------------------#
#----------------------------------------#
#Work time = wrkt                        #
wrkt = work_time                         #
#break timee = brkt                      #
brkt = break_time                        #
#final break time = frkt                 #
frkt = final_break_time                  #
#----------------------------------------#



#----------------------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------------------#


wrks = wrkt*60
brks = brkt*60
frks = frkt*60
set_of_counts = []
#    {0}----work----{wrks}----break----{wrks + brks}-----work-----{wrks + brks + wrks}------break------{2*wrks + 2*brks}


#Work = [0, wkrs)
    #break = [wrks, wrks+brks)
#Work = [wrks + brks, 2*W+b)
    #break = [2*W+b, 2W+2b)
#Work = [2W+2b, 3W+2b]



u = range(0, wrks)
v = range(wrks + brks, 2*wrks + brks)
w = range(2*wrks + 2*brks, 3*wrks + 2*brks)
x = range(3*wrks+3*brks, 4*wrks + 3*brks)
end_of_pomodoro = 3*(wrks + brks) + wrks + frks
set_of_counts.extend(u)
set_of_counts.extend(v)
set_of_counts.extend(w)
set_of_counts.extend(x)
#print(set_of_counts[:50])
import tkinter as tk
import datetime as _dt
CLOCK_FONT_TYPE = "Cambria Math"
#FONT_TYPE = "Segoe Print"
LABEL_FONT = "Segoe Print"
W = None
tiik = "✔"
raund = 1
dlt = None
#Create a window
window = tk.Tk()
window.title("Pomodoro")
window.config(padx = 10, pady = 10, bg = 'white')
#Label
lbl = tk.Label(text = 'Timer', fg = "#1E212D", bg  = "white", font = (LABEL_FONT, 35))
lbl.grid(row = 0, column = 1)
#Creating a canvas
    #Importing image
img = tk.PhotoImage(file = "clock_.png")
    #;
kyanvas = tk.Canvas(width = 290, height = 290, bg = 'white', highlightthickness = 0)
kyanvas.create_image(144.5, 144.5, image = img)
text_kyanvas = kyanvas.create_text(148, 148, text = "00:00", fill = '#4d91c9', font = (CLOCK_FONT_TYPE, 45, 'bold'))
#The fill in the above line is found using paint app as the rbg value then converting rbg value to #hex a
#  The below line of code shows how it's done
# '#%02x%02x%02x' % (r, b, g)
kyanvas.grid(row = 1, column = 1)
#;
def count_down(count):
    global dlt, tiik, W, set_of_counts
    if count == end_of_pomodoro:
        print('Pomodoro Ended!')
        
    if count in set_of_counts:
        lbl.config(text = "Work", fg = 'green')
        if count in [u[0], v[0], w[0], x[0]]:
            dlt = wrks
    elif count in [u[-1] + 1, v[-1] + 1, w[-1] + 1, x[-1] + 1]:
        lbl.config(text = "Break", fg = 'red')
        dlt = brks
        if count == x[-1] + 1:
            dlt = frks
            lbl.config(text = 'Enjoy!', fg = 'pink')
        tick_mark.config(text = tiik)
        tiik += "✔"
    if count < end_of_pomodoro+1:
        tm_txt = f'{_dt.timedelta(seconds = dlt)}'
        kyanvas.itemconfig(text_kyanvas, text = tm_txt[2:])
        W = window.after(1000, count_down, count + 1)
        dlt += -1    
#start
def start_f():
    count_down(0)
    #Each cycle of (wrkt + brkt)*3 + (wrkt + frkt)
    #count_down()    
str_btn = tk.Button(text = "start", highlightthickness = 0, command = start_f, bg = '#2d5289', fg = 'white')
str_btn.grid(row = 2, column = 0)
#;
#reset
def rst_f():
    try:
       window.after_cancel(W) #This only stops the window
       lbl.config(text = 'Timer', fg = 'green')
       kyanvas.itemconfig(text_kyanvas, text = f"00:00")
       tick_mark.config(text = "")
       tiik = "✔"
    except ValueError:
        #Why this{ValueError}:
        #Because the value to W is assign in count_down() function. so, if someone
        #hits 'reset' btn for the first then as 'start' had not been pressed
        #the value to W remains None which then raises a ValueError
        return print("You should not press reset before starting the timer.")
rst_btn = tk.Button(text = "reset", highlightthickness = 0, command = rst_f, bg = '#2d5289', fg = 'white')
rst_btn.grid(row = 2, column = 2)
tick_mark = tk.Label(text = '', fg = "green", bg = "white", font = (35))
tick_mark.grid(row = 3, column = 1)
window.mainloop()
