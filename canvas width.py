from tkinter import * 
root = Tk()

def harry(event):
    print(f"You clicked on {event.x}, {event.y}")

    
canvas_width = 855
canvas_height = 432
root.geometry("855x432")
#The above 3 lines code is the another way of writing root.geometry("855x432") 

can_widget = Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()


#The following code goes from point x1, y1 to x2, y2
can_widget.create_line(100, 200, 800, 0, fill="green")
can_widget.create_line(100, 0, 800, 200, fill="red")

#To create a rectangle, specify coordinates in this format:- cordinates of top left, coordinates of bottom right
can_widget.create_rectangle(100, 200, 800, 0 , fill="grey")


can_widget.create_text(200, 200, text="Python!")

can_widget.create_oval(344, 233, 244, 355)

can_widget.create_polygon(100, 400, 455, 545, 154, 341, fill="red")


root.title("canvas width practice")




 #Events: Jo bhi cheez hum karte h chhe vo mouse se click karna ho, mouse ko kahi hover karna ho, keyboard ki keys press karni ho, etc sab kuch events kehlate h
button = Button(root, text="Click me")
button.pack()

button.bind("<Button-1>", harry)        #ye <Button-1> darasal preassigned cheez h, baki ke ase hi dekhne ke liye "button official documentation in tkinter" par jae
button.bind("<Double-1>", quit)



root.mainloop()