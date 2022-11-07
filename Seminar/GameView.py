import tkinter as tk
import tkinter.font as tkFont


class GameView:
    def __init__(self, root, controller):
        self.controller = controller
        root.title("Monty Hall")
        # root.call('wm', 'attributes', '.', '-topmost', '1')

        # setting window size
        width = 1200
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.door_photo = tk.PhotoImage(file="door.png")

        self.btns = []

        self.btn1 = tk.Button(root)
        self.btn1["anchor"] = "center"
        self.btn1["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Arial', size=10)
        self.btn1["font"] = ft
        self.btn1["fg"] = "#000000"
        self.btn1["justify"] = "center"
        self.btn1["text"] = 0
        self.btn1.place(x=50, y=90, width=150, height=230)
        self.btn1["command"] = self.btn1_click

        self.lbl1 = tk.Label(root)
        ft = tkFont.Font(family='Arial', size=10)
        self.lbl1["font"] = ft
        self.lbl1["justify"] = "center"
        self.lbl1["text"] = ""
        self.lbl1.place(x=78, y=320, width=115, height=20)

        self.btn2 = tk.Button(root)
        self.btn2["anchor"] = "center"
        self.btn2["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Arial', size=10)
        self.btn2["font"] = ft
        self.btn2["fg"] = "#000000"
        self.btn2["justify"] = "center"
        self.btn2["text"] = 1
        self.btn2.place(x=225, y=90, width=150, height=230)
        self.btn2["command"] = self.btn2_click

        self.lbl2 = tk.Label(root)
        ft = tkFont.Font(family='Arial', size=10)
        self.lbl2["font"] = ft
        self.lbl2["justify"] = "center"
        self.lbl2["text"] = ""
        self.lbl2.place(x=78 + 175, y=320, width=115, height=20)

        self.btn3 = tk.Button(root)
        self.btn3["anchor"] = "center"
        self.btn3["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Arial', size=10)
        self.btn3["font"] = ft
        self.btn3["fg"] = "#000000"
        self.btn3["justify"] = "center"
        self.btn3["text"] = 2
        self.btn3.place(x=225 + 150 + 25, y=90, width=150, height=230)
        self.btn3["command"] = self.btn3_click

        self.lbl3 = tk.Label(root)
        ft = tkFont.Font(family='Arial', size=10)
        self.lbl3["font"] = ft
        self.lbl3["justify"] = "center"
        self.lbl3["text"] = ""
        self.lbl3.place(x=78 + 175*2, y=320, width=115, height=20)

        self.doorlbls = []
        self.doorlbls.append(self.lbl1)
        self.doorlbls.append(self.lbl2)
        self.doorlbls.append(self.lbl3)

        self.btns.append(self.btn1)
        self.btns.append(self.btn2)
        self.btns.append(self.btn3)

        self.btn_simulate = tk.Button(root)
        self.btn_simulate["anchor"] = "center"
        self.btn_simulate["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Arial', size=10)
        self.btn_simulate["font"] = ft
        self.btn_simulate["fg"] = "#000000"
        self.btn_simulate["justify"] = "center"
        self.btn_simulate["text"] = "simulate"
        self.btn_simulate.place(x=225 + 80, y=400+30, width=140, height=25)
        self.btn_simulate["command"] = self.btn_simulate_click

        self.btn_reset = tk.Button(root)
        self.btn_reset["anchor"] = "center"
        self.btn_reset["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Arial', size=10)
        self.btn_reset["font"] = ft
        self.btn_reset["fg"] = "#000000"
        self.btn_reset["justify"] = "center"
        self.btn_reset["text"] = "reset game"
        self.btn_reset.place(x=225 + 150 + 150, y=400 + 65, width=70, height=25)
        self.btn_reset["command"] = self.btn_reset_click

        self.toplbl = tk.Label(root)
        ft = tkFont.Font(family='Arial', size=10)
        self.toplbl["font"] = ft
        self.toplbl["justify"] = "center"
        self.toplbl["text"] = "Pick one of three doors"
        self.toplbl.place(x=100, y=15, width=400, height=40)

        self.statslbl = tk.Label(root)
        ft = tkFont.Font(family='Arial', size=10)
        self.statslbl["font"] = ft
        self.statslbl["justify"] = "center"
        self.statslbl["text"] = "statistics:"
        self.statslbl.place(x=50, y=350, width=100, height=20)
        self.winslbl = tk.Label(root)
        ft = tkFont.Font(family='Arial', size=10)
        self.winslbl["font"] = ft
        self.winslbl["justify"] = "left"
        self.winslbl["text"] = "Wins: 0"
        self.winslbl.place(x=50, y=380, width=100, height=20)
        self.losseslbl = tk.Label(root)
        ft = tkFont.Font(family='Arial', size=10)
        self.losseslbl["font"] = ft
        self.losseslbl["justify"] = "left"
        self.losseslbl["text"] = "Losses: 0"
        self.losseslbl.place(x=50, y=410, width=100, height=20)
        self.winratelbl = tk.Label(root)
        ft = tkFont.Font(family='Arial', size=10)
        self.winratelbl["font"] = ft
        self.winratelbl["justify"] = "left"
        self.winratelbl["text"] = "Win Rate: 0%"
        self.winratelbl.place(x=50, y=440, width=110, height=20)

        self.trigger_change = False
        self.change_checkbox = tk.Checkbutton(root)
        ft = tkFont.Font(family='Times', size=10)
        self.change_checkbox["font"] = ft
        self.change_checkbox["fg"] = "#333333"
        self.change_checkbox["justify"] = "center"
        self.change_checkbox["text"] = "With change door"
        self.change_checkbox.place(x=242, y=375, width=150, height=25)
        self.change_checkbox["offvalue"] = "0"
        self.change_checkbox["onvalue"] = "1"
        self.change_checkbox["command"] = self.checkbox_check

        self.trigger_random_simulate = False
        self.rand_checkbox = tk.Checkbutton(root)
        ft = tkFont.Font(family='Times', size=10)
        self.rand_checkbox["font"] = ft
        self.rand_checkbox["fg"] = "#333333"
        self.rand_checkbox["justify"] = "center"
        self.rand_checkbox["text"] = "With Random door opening/closing"
        self.rand_checkbox.place(x=252, y=400, width=225, height=25)
        self.rand_checkbox["offvalue"] = "0"
        self.rand_checkbox["onvalue"] = "1"
        self.rand_checkbox["command"] = self.checkbox_randomChoice

        self.amount_input = tk.Entry(root)
        self.amount_input["textvariable"] = 'amount'
        self.amount_input.place(x=345, y=350, width=100, height=25)

        self.amountlbl = tk.Label(root)
        ft = tkFont.Font(family='Arial', size=10)
        self.amountlbl["font"] = ft
        self.amountlbl["justify"] = "center"
        self.amountlbl["text"] = "Iterations:"
        self.amountlbl.place(x=440-200, y=380 - 30, width=100, height=15)

        self.exceptlbl = tk.Label(root)
        ft = tkFont.Font(family='Arial', size=10)
        self.exceptlbl["font"] = ft
        self.exceptlbl["justify"] = "left"
        self.exceptlbl["text"] = ""
        self.exceptlbl["fg"] = '#be4d25'
        self.exceptlbl.place(x=440-260, y=460, width=330, height=17)

    def btn1_click(self):
        self.controller.btn1_click()

    def btn2_click(self):
        self.controller.btn2_click()

    def btn3_click(self):
        self.controller.btn3_click()

    def btn_simulate_click(self):
        if not self.trigger_random_simulate:
            self.controller.simulate(self.trigger_change, self.amount_input.get())
        else:
            self.controller.simulate_random_choice(self.amount_input.get())

    def checkbox_check(self):
        self.trigger_change = not self.trigger_change

    def checkbox_randomChoice(self):
        self.trigger_random_simulate = not self.trigger_random_simulate
        self.change_checkbox['state'] = "disabled" if self.trigger_random_simulate else "active"

    def btn_reset_click(self):
        self.controller.btn_reset_game()

    def change_exceptionlbl(self, err_msg):
        self.exceptlbl["text"] = err_msg

    def random_choice(self):
        self.controller.random_choice_fromview()
    def create_btn_letChoiceToPC(self, root):
        self.btn_letPC_Choice = tk.Button(root)
        self.btn_letPC_Choice["anchor"] = "center"
        self.btn_letPC_Choice["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Arial', size=10)
        self.btn_letPC_Choice["font"] = ft
        self.btn_letPC_Choice["fg"] = "#000000"
        self.btn_letPC_Choice["justify"] = "center"
        self.btn_letPC_Choice["text"] = "Let the computer make the choice for you"
        self.btn_letPC_Choice.place(x=175, y=60, width=250, height=25)
        self.btn_letPC_Choice["command"] = self.random_choice
