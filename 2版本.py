import tkinter as tk
from tkinter import ttk 
import tkinter.font as tkFont
from PIL import ImageTk


i = 0
e = 0
lista = 'qweasdzxcrtyfghvbnuiojklmp'
dic = {}
place = '邦食堂'
class but(tk.Button):
    def __init__(self):
        tk.Button.__init__(self)
        self.num = 0

class Window(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.create_widgets()
    
    
    
    def create_widgets(self):
        # 字體
        font1 = tkFont.Font(size = 26, family = '宋體-繁')
        font2 = tkFont.Font(size = 15, family = '宋體-繁')

        #Build Object/建立物件
        self.entity_label = tk.Label(self, height=1,text="美食地圖", font = font1)
        self.can = tk.Canvas(self,width =500, height=300, bg= 'white')
        self.image1 = ImageTk.PhotoImage(file = 'food.png')
        self.can.create_image(50,155,image=self.image1,anchor=tk.W)

        # 地區選單
        self.myPlace = tk.StringVar()
        self.place_label = tk.Label(self, height=1, text="地區:",font=font2)
        self.place_combo = ttk.Combobox(self, state="readonly", textvariable=self.myPlace)
        self.place_combo['values'] = ("公館", "溫州街", "118", "六張犁", "學餐")
        
        # money選單
        self.myMoney = tk.StringVar()
        self.money_label = tk.Label(self, height=1, text="價錢:",font=font2)
        self.money_combo = ttk.Combobox(self, state="readonly", textvariable=self.myMoney)
        self.money_combo['values'] = ("$","$$","$$$")
        
        # money2選單
        self.myMoney2 = tk.StringVar()
        self.money_label2 = tk.Label(self, height=1, text="上限:",font=font2)
        self.money_combo2 = ttk.Combobox(self, state="readonly", textvariable=self.myMoney2)
        self.money_combo2['values'] = ("$","$$","$$$")

        # 按鍵
        self.submit_btn = tk.Button(self, height=1, width=5, text="確定", command = self.clickMe)


        
        #Assign Position/指定位置
        self.entity_label.grid(column = 1, columnspan=2, row=0, padx=3, sticky=tk.E)
        self.can.grid(row=0,rowspan=30, column=5,columnspan=5, sticky= tk.NE + tk.SW, padx=3, pady=2)

        self.place_label.grid(row=1, sticky=tk.E, padx=3)
        self.place_combo.grid(columnspan=3, row=1, column=1, padx=3, pady=2, sticky=tk.W)

        self.money_label.grid(row=2, sticky=tk.E, padx=3)
        self.money_combo.grid(columnspan=3, row=2, column=1, pady=2, padx=3, sticky=tk.W)
        self.money_label2.grid(row=3, sticky=tk.E, padx=3)
        self.money_combo2.grid(columnspan=3, row=3, column=1, pady=2, padx=3, sticky=tk.W)

        self.submit_btn.grid(column=1, columnspan=2, padx=3, pady=10,row=4)
        self.labels = []


    def clickMe(self):
        global i
        global e
        self.place_result = tk.Label(self, height=1)
        self.money_result = tk.Label(self, height=1)
        self.place_result.configure(text=self.myPlace.get())
        if self.myMoney2.get() == '':
            self.money_result.configure(text=self.myMoney.get())
        else:
            self.money_result.configure(text=self.myMoney.get()+'~'+self.myMoney2.get())
        self.place_result.grid(row=6+(i*2), column=1,sticky=tk.W)
        self.money_result.grid(row=6+(i*2), column=3,sticky=tk.W)
        self.rest_result = place
        dic[self.rest_result] = e



        self.place_result_la = tk.Label(self, height=1,text='地區:')
        self.money_result_la = tk.Label(self, height=1,text='價錢:')
        self.rest_result_la = tk.Label(self, height=1,text='餐廳:')
        self.place_result_la.grid(row=6+(i*2))
        self.rest_result_la.grid(row=7+(i*2))

        self.money_result_la.grid(row=6+(i*2), column=2)

        self.delete = tk.Button(self, height=1, width=5, text='刪除', command = lambda: self.dest(self.rest_result))
        self.delete.grid(column=3, row=7+(i*2))
        self.labels.append([self.place_result_la,self.money_result_la,self.rest_result_la,self.place_result,self.money_result, self.delete])


        i += 1
        e += 1

    def dest(self,var):
        num = dic[var]
        for label in self.labels[num]:
            label.destroy()




        

        

outer = tk.Tk()
outer.title('food app')
mywindow = Window()
mywindow.mainloop()

