'''
#####################################
#                                   #
#  Dasturchi: AsAdbEk_Sotiboldiyev  #
#                                   #
#####################################

========== Tic Tac Toe ==============

'''

from tkinter import*
from tkinter.messagebox import*
from syntex import syntax
window=Tk()
window.title("project 01")
window.geometry("600x650")
window.config(bg="green")
window.title("Tic Tac Toe #AsAdbEk_Sotiboldiyev")
color="aqua"

root=Frame(window,bg="green")
root.pack(anchor=CENTER)

banner=Label(root,bg="green",text="<< Tic Tac Toe >>",fon=("mv boli",40))
banner.grid(row=0,column=0,columnspan=2) #columnspan=2

def game_function(button,mas,index,list_button):
	global count,list_0,list_1,list_2,restart,players,main_menu
	count+=1	
	
	if count%2==0:
		button.config(bg="red",text="X",state=DISABLED)
		mas[index]='x'
		main_menu.config(bg="blue",text=players[1])
	else:
		button.config(bg="blue",text="O",state=DISABLED)
		mas[index]='o'
		main_menu.config(bg="red",text=players[0])
	winner=syntax(list_0,list_1,list_2)
	if winner:
		if winner=="x":
			winner=players[0]
			color="red"
			showinfo("NATIJA",f"O'YINDA {winner} G'OLIB BO'LDI")
		elif winner=="o":
			winner=players[1]
			color="blue"
			showinfo("NATIJA",f"O'YINDA {winner} G'OLIB BO'LDI")
		else:
			color="cyan"
			showinfo("NATIJA","O'YINDA G'OLIB ANIQLANMADI.\n DURRANG!!!")

		for i in list_button:
			i.config(state=DISABLED,bg=color)
		restart.config(state=NORMAL)
		


def game_place_f():
	global list_0,list_1,list_2,count,restart,registration,main_menu
	registration.destroy()
	
	count=2

	list_0=['.','.','.']
	list_1=['.','.','.']
	list_2=['.','.','.']
	
	game_place=Frame(root,bg="black")
	game_place.grid(row=2,column=0,padx=20,pady=20,columnspan=2)
	
	b1=Button(game_place,font=("mv boli",55,"bold"),width=4,bg=color)
	b1.grid(row=0,column=0,padx=3,pady=3)
	b2=Button(game_place,font=("mv boli",55,"bold"),width=4,bg=color)
	b2.grid(row=0,column=1,padx=3,pady=3)
	b3=Button(game_place,font=("mv boli",55,"bold"),width=4,bg=color)
	b3.grid(row=0,column=2,padx=3,pady=3)
	b4=Button(game_place,font=("mv boli",55,"bold"),width=4,bg=color)
	b4.grid(row=1,column=0,padx=3,pady=3)
	b5=Button(game_place,font=("mv boli",55,"bold"),width=4,bg=color)
	b5.grid(row=1,column=1,padx=3,pady=3)
	b6=Button(game_place,font=("mv boli",55,"bold"),width=4,bg=color)
	b6.grid(row=1,column=2,padx=3,pady=3)
	b7=Button(game_place,font=("mv boli",55,"bold"),width=4,bg=color)
	b7.grid(row=2,column=0,padx=3,pady=3)
	b8=Button(game_place,font=("mv boli",55,"bold"),width=4,bg=color)
	b8.grid(row=2,column=1,padx=3,pady=3)
	b9=Button(game_place,font=("mv boli",55,"bold"),width=4,bg=color)
	b9.grid(row=2,column=2,padx=3,pady=3)
	
	list_button=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
	
	b1.config(command=lambda:game_function(b1,list_0,0,list_button))
	b2.config(command=lambda:game_function(b2,list_0,1,list_button))
	b3.config(command=lambda:game_function(b3,list_0,2,list_button))
	b4.config(command=lambda:game_function(b4,list_1,0,list_button))
	b5.config(command=lambda:game_function(b5,list_1,1,list_button))
	b6.config(command=lambda:game_function(b6,list_1,2,list_button))
	b7.config(command=lambda:game_function(b7,list_2,0,list_button))
	b8.config(command=lambda:game_function(b8,list_2,1,list_button))
	b9.config(command=lambda:game_function(b9,list_2,2,list_button))
	restart=Button(root,text="RESTART",width=10,font=("mv boli",20),state=DISABLED,command=game_place_f)
	restart.grid(row=1,column=0,pady=10)
	main_menu=Label(root,width=20,bg="blue",fg="white",text=players[1],font=("mv boli",25))
	main_menu.grid(row=1,column=1)

#=============================

players=[]

def start_function(btn,plyr,plyr_x='',plyr_o=''):
	global pl_count,start,players
	
	
	if plyr_o!='':
		players.append(plyr_o)
	if plyr_x!='':
		players.insert(0,plyr_x)
	


	pl_count+=1
	btn.config(state=DISABLED,bg="lightgreen")
	plyr.config(state=DISABLED)
	if pl_count==2:
		start.config(state=NORMAL,bg="lightgreen")
	
def start_place():
	global pl_count,start,registration
	pl_count=0
	registration=Frame(root,bg="green",relief=SOLID,bd=3,pady=30)
	registration.grid(row=1,column=0,pady=50)

	player_x_icon=Label(registration,bg="red",font=("sans-serif",20,"bold"),width=2,text="X")
	player_x_icon.grid(row=0,column=0,padx=10)
	player_x=Entry(registration,font=("sans-serif",22,"bold"))
	player_x.grid(row=0,column=1,pady=5)
	player_x_button=Button(registration,text="KIRITISH",font=("sans-serif",14,"bold"),command=lambda:start_function(player_x_button,player_x,plyr_x=player_x.get()))
	player_x_button.grid(row=0,column=2,padx=10)

	player_o_icon=Label(registration,bg="blue",font=("sans-serif",20,"bold"),width=2,text="O")
	player_o_icon.grid(row=1,column=0,padx=10)
	player_o=Entry(registration,font=("sans-serif",22,"bold"))
	player_o.grid(row=1,column=1,pady=5)
	player_o_button=Button(registration,text="KIRITISH",font=("sans-serif",14,"bold"),command=lambda:start_function(player_o_button,player_o,plyr_o=player_o.get()))
	player_o_button.grid(row=1,column=2,padx=10)
	
	start=Button(registration,text=" BOSHLASH ",bg="pink",state=DISABLED,font=("mv boli",20,"bold"),command=game_place_f)
	start.grid(row=2,column=0,columnspan=3,pady=20)
start_place()



window.mainloop()
