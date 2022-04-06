import wx


class MyApp(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyApp, self).__init__(*args, **kw)
        self.check_list_item2 = None
        self.check1 = None
        self.radio_btn1 = None
        self.radio_btn2 = None
        self.radio_btn3 = None
        self.radio_btn4 = None
        self.OnInitUI()

    def OnClose(self, e):
        self.Close(True)

    def OnInitUI(self):
        self.SetTitle('Order food ')
        self.Centre()
        self.Show(True)


        pnl = wx.Panel(self)
        # panel
        self.SetSize(420, 300)

        heading_font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        heading = wx.StaticText(pnl, label='Menu', pos=(105, 10))
        heading.SetFont(heading_font)

        self.radio_btn1 = wx.RadioButton(pnl, label="Beef burger", pos=(20, 42), style=wx.RB_GROUP)
        self.radio_btn2 = wx.RadioButton(pnl, label="Veggie burger", pos=(20, 62))
        self.radio_btn3 = wx.RadioButton(pnl, label="Fish sandwich", pos=(20, 82))
        self.radio_btn4 = wx.RadioButton(pnl, label="Dönner", pos=(20, 102))

        wx.StaticLine(pnl, pos=(35, 35), size=(305, 1))

        wx.StaticBox(pnl, label=' Additional', pos=(180, 40), size=(190, 120))
        self.check_list_item1 = wx.CheckBox(pnl, label='Fried egg', pos=(190, 60))
        self.check_list_item2 = wx.CheckBox(pnl, label='Cheese', pos=(190, 80))

        self.quantity = wx.StaticText(pnl, label=' Quantity', pos=(15, 180))
        self.spin_ctrl = wx.SpinCtrl(pnl, value='0', pos=(90, 175))
        self.spin_ctrl.SetRange(0, 20)

        order_btn = wx.Button(pnl, label='Confirm order', pos=(220, 175), size=(100, -1))
        order_btn.Bind(wx.EVT_BUTTON, self.OnOrder)

        order_font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        self.ordered_food = wx.StaticText(pnl, label="", pos=(20, 215))
        self.ordered_food.SetFont(order_font)


        self.radio_btn1.Bind(wx.EVT_RADIOBUTTON, self.SetVal, id=self.radio_btn1.GetId())
        self.radio_btn2.Bind(wx.EVT_RADIOBUTTON, self.SetVal, id=self.radio_btn2.GetId())
        self.radio_btn3.Bind(wx.EVT_RADIOBUTTON, self.SetVal, id=self.radio_btn3.GetId())
        self.radio_btn4.Bind(wx.EVT_RADIOBUTTON, self.SetVal, id=self.radio_btn4.GetId())

        self.Centre()
        self.Show(True)

    def SetVal(self, e):
        print("TODO")
        # TODO

    def OnOrder(self, e):
        order_descr = ''

        if self.radio_btn1.GetValue():
            order_descr += f"{self.radio_btn1.GetLabel()}"
        if self.radio_btn2.GetValue():
            order_descr += f"{self.radio_btn2.GetLabel()}"
        if self.radio_btn3.GetValue():
            order_descr += f"{self.radio_btn3.GetLabel()}"
        if self.radio_btn4.GetValue():
            order_descr += f"{self.radio_btn4.GetLabel()}"

        print(self.check_list_item1.GetId())
        if self.check_list_item1.GetValue():
            order_descr += f", with {self.check_list_item1.GetLabel()}"
        if self.check_list_item2.GetValue():
            order_descr += f", with {self.check_list_item2.GetLabel()}"
        print(f"{self.spin_ctrl.GetValue()} x {order_descr}")
        self.ordered_food.SetLabel(f"Your order: {self.spin_ctrl.GetValue()} x {order_descr}")


ex = wx.App()
MyApp(None)
ex.MainLoop()
