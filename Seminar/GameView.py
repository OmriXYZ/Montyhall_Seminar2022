import tkinter as tk
import tkinter.font as tkFont


class GameView:
    def __init__(self, root, controller):
        """
        Initialize the game UI, GameView object handles the UI interation with the user.

        :param root: Tkinter root window
        :param controller: MVC controller that "holds" the entire program objects
        """
        self.controller = controller
        root.title("Monty Hall")
        root.call('wm', 'attributes', '.', '-topmost', '1')
        # setting window size
        self.controller.change_scale(700, 500)
        root.resizable(width=False, height=False)

        # Make the top instruction label
        self.toplbl = tk.Label(root, text="Pick one of three doors")
        self.toplbl.grid(row=0, column=1, padx=1, pady=5, columnspan=2, sticky='W')

        door_start_row = 1
        door_start_col = 0

        self.door_photo = tk.PhotoImage(file="images/door.png")

        # Making the first door
        self.btn1 = tk.Button(root, command=self.btn1_click)
        self.btn1.place(width=150, height=230)
        self.btn1.grid(row=door_start_row, column=door_start_col, padx=5, pady=5)
        self.lbl1 = tk.Label(root, text="")
        self.lbl1.grid(row=door_start_row + 1, column=door_start_col, sticky='w', padx=5, pady=2)
        # Making the second door
        self.btn2 = tk.Button(root, command=self.btn2_click)
        self.btn2.place(width=150, height=230)
        self.btn2.grid(row=door_start_row, column=door_start_col + 1, sticky='w', padx=5, pady=5)
        self.lbl2 = tk.Label(root, text="")
        self.lbl2.grid(row=door_start_row + 1, column=door_start_col + 1, sticky='w', padx=5, pady=2)
        # Making the third door
        self.btn3 = tk.Button(root, command=self.btn3_click)
        self.btn3.place(width=150, height=230)
        self.btn3.grid(row=door_start_row, column=door_start_col + 2, padx=5, pady=5)
        self.lbl3 = tk.Label(root, text="")
        self.lbl3.grid(row=door_start_row + 1, column=door_start_col + 2, sticky='w', padx=5, pady=2)

        # Appends all subtext to a list
        self.doorlbls = []
        self.doorlbls.append(self.lbl1)
        self.doorlbls.append(self.lbl2)
        self.doorlbls.append(self.lbl3)

        # Appends all doors to a list
        self.btns = []
        self.btns.append(self.btn1)
        self.btns.append(self.btn2)
        self.btns.append(self.btn3)

        # Make the simulate button
        self.btn_simulate = tk.Button(root, command=self.btn_simulate_click, text='simulate')
        self.btn_simulate.place(x=250, y=400 + 30)

        # Make the reset game button
        self.btn_reset = tk.Button(root, command=self.btn_reset_click, text='reset game')
        self.btn_reset.place(x=225 + 150 + 150, y=400 + 65)

        # Make the stats labels
        self.statslbl = tk.Label(root, text="Statistics:")
        self.statslbl.place(x=35, y=330)

        self.winslbl = tk.Label(root, text="Wins: 0")
        self.winslbl.place(x=35, y=350)

        self.changedoorlbl = tk.Label(root, text="The door changed randomly: 0 times")
        self.changedoorlbl.place(x=225 + 30, y=400 + 70)

        self.losseslbl = tk.Label(root, text="Losses: 0")
        self.losseslbl.place(x=35, y=370)

        self.winratelbl = tk.Label(root, text="Win Rate: 0%")
        self.winratelbl.place(x=35, y=390)

        self.totalgames = tk.Label(root, text="Total games played: 0")
        self.totalgames.place(x=35, y=410)

        # Make the Radio Button for changing the door
        self.simulate_option = 0
        self.selected = tk.StringVar()
        self.r1 = tk.Radiobutton(root, text='For each iteration change the initial selection',
                                 value='Value 1', variable=self.selected, command=self.radio1)
        self.r1.place(x=245, y=355)
        self.r2 = tk.Radiobutton(root, text='For each iteration keep the initial selection',
                                 value='Value 2', variable=self.selected, command=self.radio2, tristatevalue=0)
        self.r2.place(x=245, y=380)
        self.r3 = tk.Radiobutton(root, text='For each iteration randomly decide whether to change the door or not',
                                 value='Value 3', variable=self.selected, command=self.radio3, tristatevalue=0)
        self.r3.place(x=245, y=405)

        # Make the input text for simulations
        self.amount_input = tk.Entry(root, textvariable='amount')
        self.amount_input.place(x=315, y=332)

        self.amountlbl = tk.Label(root, text="Iterations:")
        self.amountlbl.place(x=440 - 200, y=330)

        self.exceptlbl = tk.Label(root, text="", fg='#be4d25')
        self.exceptlbl.place(x=325, y=433)

    def btn1_click(self):
        """
        handles what happens after first door is pressed
        :return: None
        """
        self.controller.btn1_click()

    def btn2_click(self):
        """
        handles what happens after first door is pressed
        :return: None
        """
        self.controller.btn2_click()

    def btn3_click(self):
        """
        handles what happens after first door is pressed
        :return: None
        """
        self.controller.btn3_click()

    def btn_simulate_click(self):
        """
        handles what happens after simulation button is presses
        :return: None
        """
        self.controller.simulate(self.simulate_option, self.amount_input.get())

    def btn_reset_click(self):
        """
        handles what happens after reset button is presses.
        :return: None
        """
        self.controller.change_scale(700, 500)
        self.controller.btn_reset_game()
        self.amount_input.setvar('amount', '')

    def change_exceptionlbl(self, err_msg):
        self.exceptlbl["text"] = err_msg

    """
    handles the radio buttons.
    """
    def radio1(self):
        self.simulate_option = 0

    def radio2(self):
        self.simulate_option = 1

    def radio3(self):
        self.simulate_option = 2
