import tkinter as tk
from tkinter import ttk
import re
from matplotlib import pyplot as plt
import math

# Create main window
root = tk.Tk()
root.title("Disk Scheduling App")

def FCFS(sequence,start, CYLINDER_MAX):
    temp = sequence.copy()
    temp.insert(0,start)
    plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
    plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True
    size = len(temp)
    x = temp
    y = []
    headmovement = 0
    for i in range(0,size):
        y.append(-i)
        if i!=size-1:
            headmovement = headmovement + abs(temp[i]-temp[i+1])
    string = 'Headmovement = ' + str(headmovement) + ' cylinders'
    string2 = str(temp)
    plt.plot(x,y, color="green", markerfacecolor = 'blue', marker='o', markersize = 5, linewidth = 2, label="FCFS")
    plt.ylim = (0,size)
    plt.xlim = (0,CYLINDER_MAX)
    plt.yticks([])
    plt.title("First Come First Served Scheduling Algorithm")
    plt.text(172.5, -8.85, string, horizontalalignment='center',verticalalignment='center',fontsize=12)
    plt.text(172.5, -9.5, string2, horizontalalignment='center',verticalalignment='center',fontsize=12)
    plt.show()

def SSTF(sequence,start, CYLINDER_MAX):
    temp = sequence.copy()
    def next_in_sequence(seq,val):
        diff = 0
        mindiff = math.inf
        nextval = 0
        #print(seq)
        for i in range(0,len(seq)):
            if(seq[i]!=val):
                diff = abs(seq[i]-val)
                if(diff<mindiff):
                    mindiff=diff
                    nextval = seq[i]
        return nextval
    
    temp.insert(0,start)
    val = start
    x = []
    y = []
    size = 0
    x.append(start)
    headmovement = 0
    while(len(temp)):
        val = next_in_sequence(temp,val)
        #print(val)
        x.append(val)
        temp.remove(val)
    size = len(x)
    for i in range(0,size):
        y.append(-i)
        if i!=(size-1):
            headmovement = headmovement + abs(x[i]-x[i+1])
    string = 'Headmovement = ' + str(headmovement) + ' cylinders'
    string2 = str(x)
    
    plt.plot(x,y, color="green", markerfacecolor = 'blue', marker='o', markersize = 5, linewidth = 2, label="SSTF")
    plt.ylim = (0,size)
    plt.xlim = (0,CYLINDER_MAX)
    plt.yticks([])
    plt.title("Shortest Seek Time First Scheduling Algorithm")
    plt.text(182.5, -10.85, string, horizontalalignment='center',verticalalignment='center',fontsize=12)
    plt.text(182.5, -11.5, string2, horizontalalignment='center',verticalalignment='center',fontsize=12)
    plt.show()

def SCAN(sequence,start,direction, CYLINDER_MAX):
    temp = sequence.copy()
    left = []
    right = []
    x = []
    y = []
    x_approx = []
    y_approx = []
    headmovement = 0
    headmovement_approx = 0
    x.append(start)
    if(direction=="Left"):
        for i in temp:
            if i<start:
                left.append(i)
            else:
                right.append(i)
        left.sort(reverse = True)
        for i in left:
            x.append(i)
        x.append(0)
        right.sort()
        for i in right:
            x.append(i)

        x_approx.append(start)
        x_approx.append(min(x))
        x_approx.append(max(x))
        headmovement_approx = abs(start-0)
        headmovement_approx = headmovement_approx + abs(0-max(x))
    elif(direction=="Right"):
        for i in temp:
            if i>start:
                right.append(i)
            else:
                left.append(i)
        right.sort()
        for i in right:
            x.append(i)
        x.append(CYLINDER_MAX)
        left.sort(reverse = True)
        for i in left:
            x.append(i)
        x_approx.append(start)
        x_approx.append(max(x))
        x_approx.append(min(x))
        headmovement_approx = abs(start-199)
        headmovement_approx = headmovement_approx + abs(199-min(x))



    y_approx.append(0)
    size = len(x)
    for i in range(0,size):
        y.append(-i)
        if(x[i]==0 or x[i]==199):
            y_approx.append(-i)
        if i!=(size-1):
            headmovement = headmovement + abs(x[i]-x[i+1])
        else:
            y_approx.append(-i)
    string = 'Headmovement = ' + str(headmovement) + ' cylinders'
    string2 = str(x)

    plt.plot(x,y, color="green", markerfacecolor = 'blue', marker='o', markersize = 5, linewidth = 2, label="SCAN")
    plt.plot(x_approx,y_approx, dashes = [6,2] , color="red", markerfacecolor = 'red', marker='D', markersize = 5, linewidth = 0.5, label="Approx SCAN")
    plt.ylim = (0,size)
    plt.xlim = (0,CYLINDER_MAX)
    plt.yticks([])
    plt.title("SCAN Scheduling Algorithm")
    plt.text(182.5, -10.85, string, horizontalalignment='center',verticalalignment='center',fontsize=12)
    plt.text(182.5, -12.5, string2, horizontalalignment='center',verticalalignment='center',fontsize=12)
    plt.show()

def CSCAN(sequence, start, direction, CYLINDER_MAX):
    temp = sequence.copy()
    left = []
    right = []
    x = []
    y = []
    x_approx = []
    y_approx = []
    headmovement = 0
    headmovement_approx = 0
    x.append(start)
    if(direction=="Left"):
        for i in temp:
            if i<start:
                left.append(i)
            else:
                right.append(i)
        left.sort(reverse = True)
        for i in left:
            x.append(i)
        x.append(0)
        x.append(CYLINDER_MAX)
        right.sort(reverse = True)
        for i in right:
            x.append(i)
        x_approx.append(start)
        x_approx.append(min(x))
        x_approx.append(max(x))
        x_approx.append(x[-1])
        headmovement_approx = abs(start-0)
        headmovement_approx = headmovement_approx + abs(0-max(x))
        headmovement_approx = headmovement_approx + abs(0-x[-1])
    elif(direction=="Right"):
        for i in temp:
            if i>start:
                right.append(i)
            else:
                left.append(i)
        right.sort()
        for i in right:
            x.append(i)
        x.append(CYLINDER_MAX)
        x.append(0)
        left.sort()
        for i in left:
            x.append(i)
        x_approx.append(start)
        x_approx.append(CYLINDER_MAX)
        x_approx.append(0)
        x_approx.append(x[-1])
        headmovement_approx = abs(start-199)
        headmovement_approx = headmovement_approx + abs(199-0)
        headmovement_approx = headmovement_approx + abs(0-x[-1])



    y_approx.append(0)
    size = len(x)
    for i in range(0,size):
        y.append(-i)
        if(x[i]==0 or x[i]==199):
            y_approx.append(-i)
        if i!=(size-1):
            headmovement = headmovement + abs(x[i]-x[i+1])
        else:
            y_approx.append(-i)
    string = 'Headmovement = ' + str(headmovement) + ' cylinders'
    string2 = str(x)

    plt.plot(x,y, color="green", markerfacecolor = 'blue', marker='o', markersize = 5, linewidth = 2, label="CSCAN")
    plt.plot(x_approx,y_approx, dashes = [6,2] , color="red", markerfacecolor = 'red', marker='D', markersize = 5, linewidth = 0.5, label="Approx CSCAN")
    plt.ylim = (0,size)
    plt.xlim = (0,CYLINDER_MAX)
    plt.yticks([])
    plt.title("CSCAN Scheduling Algorithm")
    plt.text(182.5, -10.85, string, horizontalalignment='center',verticalalignment='center',fontsize=12)
    plt.text(182.5, -12.5, string2, horizontalalignment='center',verticalalignment='center',fontsize=12)
    plt.show()

def LOOK(sequence, start, direction, CYLINDER_MAX):
    temp = sequence.copy()
    left = []
    right = []
    x = []
    y = []
    x_approx = []
    y_approx = []
    headmovement = 0
    headmovement_approx = 0
    x.append(start)
    if(direction=="Left"):
        for i in temp:
            if i<start:
                left.append(i)
            else:
                right.append(i)
        left.sort(reverse = True)
        for i in left:
            x.append(i)
        right.sort()
        for i in right:
            x.append(i)
        x_approx.append(start)
        x_approx.append(min(x))
        x_approx.append(max(x))
        headmovement_approx = abs(start-min(x))
        headmovement_approx = headmovement_approx + abs(min(x)-max(x))
    elif(direction=="Right"):
        for i in temp:
            if i>start:
                right.append(i)
            else:
                left.append(i)
        right.sort()
        for i in right:
            x.append(i)
        left.sort(reverse = True)
        for i in left:
            x.append(i)
        x_approx.append(start)
        x_approx.append(max(x))
        x_approx.append(min(x))
        headmovement_approx = abs(start-max(x))
        headmovement_approx = headmovement_approx + abs(max(x)-min(x))



    y_approx.append(0)
    size = len(x)
    for i in range(0,size):
        y.append(-i)
        if((x[i]==max(x) or x[i]==min(x)) and (i!=size)):
            y_approx.append(-i)
        if i!=(size-1):
            headmovement = headmovement + abs(x[i]-x[i+1])
    string = 'Headmovement = ' + str(headmovement) + ' cylinders'
    string2 = str(x)

    plt.plot(x,y, color="green", markerfacecolor = 'blue', marker='o', markersize = 5, linewidth = 2, label="LOOK")
    plt.plot(x_approx,y_approx, dashes = [6,2] , color="red", markerfacecolor = 'red', marker='D', markersize = 5, linewidth = 0.5, label="Approx LOOK")
    plt.ylim = (0,size)
    plt.xlim = (0,CYLINDER_MAX)
    plt.yticks([])
    plt.title("LOOK Scheduling Algorithm")
    plt.text(182.5, -10.85, string, horizontalalignment='center',verticalalignment='center',fontsize=12)
    plt.text(182.5, -12.5, string2, horizontalalignment='center',verticalalignment='center',fontsize=12)
    plt.show()

def CLOOK(sequence, start, direction, CYLINDER_MAX):
    temp = sequence.copy()
    left = []
    right = []
    x = []
    y = []
    x_approx = []
    y_approx = []
    headmovement = 0
    headmovement_approx = 0
    x.append(start)
    if(direction=="Left"):
        for i in temp:
            if i<start:
                left.append(i)
            else:
                right.append(i)
        left.sort(reverse = True)
        for i in left:
            x.append(i)
        right.sort(reverse = True)
        for i in right:
            x.append(i)
        x_approx.append(start)
        x_approx.append(min(x))
        x_approx.append(max(x))
        x_approx.append(x[-1])
        headmovement_approx = abs(start-min(x))
        headmovement_approx = headmovement_approx + abs(min(x)-max(x))
        headmovement_approx = headmovement_approx + abs(max(x)-x[-1])
    elif(direction=="Right"):
        for i in temp:
            if i>start:
                right.append(i)
            else:
                left.append(i)
        right.sort()
        for i in right:
            x.append(i)
        left.sort()
        for i in left:
            x.append(i)
        x_approx.append(start)
        x_approx.append(max(x))
        x_approx.append(min(x))
        x_approx.append(x[-1])
        headmovement_approx = abs(start-max(x))
        headmovement_approx = headmovement_approx + abs(max(x)-min(x))
        headmovement_approx = headmovement_approx + abs(min(x)-x[-1])



    y_approx.append(0)
    size = len(x)
    for i in range(0,size):
        y.append(-i)
        if((x[i]==min(x) or x[i]==max(x))and(i!=size)):
            y_approx.append(-i)
        if i!=(size-1):
            headmovement = headmovement + abs(x[i]-x[i+1])
        else:
            y_approx.append(-i)
    string = 'Headmovement = ' + str(headmovement) + ' cylinders'
    string2 = str(x)

    plt.plot(x,y, color="green", markerfacecolor = 'blue', marker='o', markersize = 5, linewidth = 2, label="CLOOK")
    plt.plot(x_approx,y_approx, dashes = [6,2] , color="red", markerfacecolor = 'red', marker='D', markersize = 5, linewidth = 0.5, label="Approx CLOOK")
    plt.ylim = (0,size)
    plt.xlim = (0,CYLINDER_MAX)
    plt.yticks([])
    plt.title("CLOOK Scheduling Algorithm")
    plt.text(182.5, -10.85, string, horizontalalignment='center',verticalalignment='center',fontsize=12)
    plt.text(182.5, -12.5, string2, horizontalalignment='center',verticalalignment='center',fontsize=12)
    plt.show()

# Function to handle button click
def on_click():
    sequence = [int(i) for i in re.findall(r'\d+', entry_sequence.get())] # transform input to list on ints
    head_position = int(entry_head_position.get()) # transform input to int
    direction = direction_var.get() 
    CYLINDER_MAX = int(entry_max_cylinder.get())
    algorithm = algorithm_var.get() # get selected algorithm as a string 

    # Process the input data here
    print("Sequence:", sequence)
    print("Direction:", direction)
    print("Max Cylinder:", CYLINDER_MAX)
    print("Algorithm:", algorithm)
    print("Head Position:", head_position)

    if algorithm == "FCFS":
        FCFS(sequence, head_position, CYLINDER_MAX)
    elif algorithm == "SSTF":
        SSTF(sequence, head_position, CYLINDER_MAX)
    elif algorithm == "SCAN":
        if direction == "Not Important":
            print("Please Enter the direction!")
        else:
            SCAN(sequence, head_position, direction, CYLINDER_MAX)
    elif algorithm == "C-SCAN":
        if direction == "Not Important":
            print("Please Enter the direction!")
        else:
            CSCAN(sequence, head_position, direction, CYLINDER_MAX)
    elif algorithm == "LOOK":
        if direction == "Not Important":
            print("Please Enter the direction!")
        else:
            LOOK(sequence, head_position, direction, CYLINDER_MAX)
    elif algorithm == "C-LOOK":
        if direction == "Not Important":
            print("Please Enter the direction!")
        else:
            CLOOK(sequence, head_position, direction, CYLINDER_MAX)
# Create labels
label_sequence = tk.Label(root, text="Sequence of Requests:")
label_sequence.pack()

# Create entry for sequence of requests
entry_sequence = tk.Entry(root, width=50)
entry_sequence.pack()

# Create entry for current head position
label_head_position = tk.Label(root, text="Current Head Position:")
label_head_position.pack()
entry_head_position = tk.Entry(root)
entry_head_position.pack()

# Create radio buttons for direction
direction_var = tk.StringVar()
label_direction = tk.Label(root, text="Direction:")
label_direction.pack()
radio_right = tk.Radiobutton(root, text="Right", variable=direction_var, value="Right")
radio_right.pack()
radio_left = tk.Radiobutton(root, text="Left", variable=direction_var, value="Left")
radio_left.pack()
radio_not_important = tk.Radiobutton(root, text="Not Important", variable=direction_var, value="Not Important")
radio_not_important.pack()

# Create entry for max cylinder number
label_max_cylinder = tk.Label(root, text="Max Cylinder Number:")
label_max_cylinder.pack()
entry_max_cylinder = tk.Entry(root)
entry_max_cylinder.pack()

# Create listbox for algorithm selection
label_algorithm = tk.Label(root, text="Select Algorithm:")
label_algorithm.pack()
algorithm_var = tk.StringVar()
algorithm_list = ttk.Combobox(root, textvariable=algorithm_var)
algorithm_list['values'] = ("FCFS", "SSTF", "SCAN", "C-SCAN", "LOOK", "C-LOOK")
algorithm_list.pack()

# Create submit button
button_submit = tk.Button(root, text="Submit", command=on_click)
button_submit.pack()

# Start the GUI
root.mainloop()

