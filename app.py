
import subprocess
from tkinter import *
import robin_stocks.robinhood as rh
import pyotp
import time



#https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
class RhApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.switch_frame(LoginAuth)
        self.geometry('700x700')
        self.configure(bg="black")

    def switch_frame(self, frame_class, args=None):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self, args) if args else frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class Session(Frame):

    def __init__(self, master, args=[]):
        Frame.__init__(self, master)

        # self.username = args[0]
        # orders = []
        # # populate orders from json
        # for el in orders:
        #     subprocess.run(self.monitor(el[0], el[1], el[2], el[3]))


        # # add new order 
        #     #ticker label
        #     #buy or sell
        #     #price to order at
        #     #amount to order
        


        self.buySPY = Button(self, text="buy $1 SPY", command=self.buy_spy).grid(row=5, column=0)

    def buy_spy(self):
        bought = rh.order_buy_fractional_by_price('SPY', 1)
        print(bought)
    
    def monitor(self, ticker, order_price, buy_sell, amount_usd):
        #TODO** Add label?? Current price?? 
        while True:
            price = rh.get_latest_price(ticker)
            if (buy_sell == True) and (price <= order_price):
                '''execute order'''
                rh.order_buy_fractional_by_price(ticker, amount_usd)
            elif (price <= order_price):
                '''execute order'''
                rh.order_sell_fractional_by_price(ticker, amount_usd)

            time.sleep(30)



class LoginAuth(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        self.userIn = StringVar()
        self.passIn = StringVar()
        self.mfaIn = StringVar()

        self.userLabel = Label(self ,text = "Username").grid(row = 1,column = 0)
        self.passLabel = Label(self ,text = "Password").grid(row = 2,column = 0)
        self.userForm = Entry(self, textvariable=self.userIn).grid(row = 1,column = 1)
        self.passForm = Entry(self, textvariable=self.passIn, show="*").grid(row = 2,column = 1)

        self.loginBtn = Button(self, text="login", command=lambda: self.rh_login(master)).grid(row=4, column=0)

    def rh_login(self, master):

        try:
            otp = ""
            with open('user.txt', 'r') as f:
                otp = f.read()
            print(otp)
            login = rh.login(self.userIn.get(), self.passIn.get(), mfa_code=str(otp))
            master.switch_frame(Session, self.userIn.get())

        except Exception as e:
            print(e)
            Label(self ,text = "Error logging in", width=100).grid(row = 5,column = 0)




if __name__ == "__main__":
    app = RhApp()
    app.mainloop()