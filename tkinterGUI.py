import tkinter as tk


def scan_usb():        #Function for button1
      import subprocess
      subprocess.call('/home/pi/Desktop/Pie/shell/shell.sh', shell=True)

#Function for button2
def copy_usb():
      import subprocess
      subprocess.call('/home/pi/Desktop/Pie/shell/copy.sh', shell=True)

#Function for button3
def wifi_connect():
      import subprocess
      subprocess.call('/home/pi/Desktop/Pie/shell/wifi.sh', shell=True)

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
button.config( height = 10, width = 5 )



button1= tk.Button(frame,
                   text="Scan USB",
                   fg="green",
				   bg="white",
                  command=scan_usb)

button1.pack(padx=5, pady=20, side=tk.LEFT)
button1.config( height = 10, width = 10 )

button2= tk.Button(frame,
                   text="Copy USB",
				   bg="white",
                   command=copy_usb)


button2.pack(padx=5, pady=20, side=tk.RIGHT)
button2.config( height = 10, width = 10 )


button3= tk.Button(frame,
                   text="WIFI Connect",
				   bg="white",
                   command=wifi_connect)

button3.pack(padx=5, pady=20, side=tk.LEFT)
button3.config(height=5, width=10)


button4= tk.Button(frame,
                   text="Update AV",
				   bg="white")
                   #command=write_button)

button4.pack(padx=5, pady=20, side=tk.RIGHT)
button4.config( height =5, width = 10 )

button5= tk.Button(frame,
                   text="Cloud Send",bg="white")
                   #command=write_button)
button5.pack(padx=5, pady=20, side=tk.LEFT)
button5.config( height =5, width = 10 )

button6 = tk.Button(frame,
                   text="COPY To SD",
				   bg="white")
                   #command=write_button)
button6.pack(padx=5, pady=20, side=tk.RIGHT)
button6.config( height =5, width = 10 )



root.mainloop()

