import tkinter as tk


def scan_usb():        #Function for button1
      import subprocess
      subprocess.call('/home/pi/Desktop/Pie/shell script/shell.sh', shell=True)

#Function for button2
def copy_usb():
      import subprocess
      subprocess.call('/home/pi/Desktop/Pie/shell script/copy.sh', shell=True)

#Function for button3
def wifi_connect():
      import subprocess
      subprocess.call('/home/silico/Desktop/copy.sh', shell=True)

#Function for button4
def update_AV():
      import subprocess
      subprocess.call('/home/silico/Desktop/copy.sh', shell=True)

#Function for button5
#def cloud_send():
 #     import subprocess
  #    subprocess.call('/home/silico/Desktop/copy.sh', shell=True) 

 #Function for button6        
def copy_sd():
      import subprocess
      subprocess.call('/home/silico/Desktop/copy.sh', shell=True)  

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
frame.place()
root.attributes("-fullscreen", True)
root.configure(background='black')

button = tk.Button(frame,
                   text="QUIT",
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
button.config( height = 10, width = 10 )



button1= tk.Button(frame,
                   text="SCAN USB",
                   fg="green",
                  command=scan_usb)

button1.pack(side=tk.TOP)
button1.config( height = 5, width = 10 )

button2= tk.Button(frame,
                   text="Copy USB",
                   command=copy_usb)


button2.pack(side=tk.BOTTOM)
button2.config( height = 5, width = 10 )


button3= tk.Button(frame,
                   text="WIFI Connect")
                   # command=write_button)

button3.pack(side=tk.TOP)
button3.config(height=5, width=10)


button4= tk.Button(frame,
                   text="Update AV")
                   #command=write_button)

button4.pack(side=tk.TOP)
button4.config( height =5, width = 10 )

button5= tk.Button(frame,
                   text="Cloud Send")
                   #command=write_button)
button5.pack(side=tk.BOTTOM)
button5.config( height =5, width = 10 )

button6 = tk.Button(frame,
                   text="COPY To SD")
                   #command=write_button)
button6.pack(side=tk.TOP)
button6.config( height =5, width = 10 )



root.mainloop()
root.geometry('1250*1250')
