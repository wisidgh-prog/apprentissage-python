from tkinter import *
#creer une premiere fenetre
window = Tk()
# personnaliser la fenetre
window.title("Promanager")
window.geometry("240x200")
window.minsize(140, 100)
#pour l'icon de l'applcation
window.iconbitmap("favicon.ico")
window.configure(bg="black")
#creer frame
frame = Frame(window)
#afficher texte
label = Label(frame, text="Bienvenu sur promanager",bg="black",fg="white",font=("Arial",20))
label.pack()
#afficher second text
label_2 = Label(frame, text="que souhaitez vous",bg="black",fg="white",font=("Arial",15))
label_2.pack()
#afficher la frame
frame.pack(expand=YES)
#ajouter bouton
btn_retour= Button(window,text="quitter",bg="black",fg="yellow",font=("Arial",20))
#afficher bouton
btn_retour.pack(side=LEFT)
















# afficher
window.mainloop()