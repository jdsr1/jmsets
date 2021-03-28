#!/usr/bin/python3
#!encoding: utf-8

import tkinter as tk
import tkinter.ttk as ttk
import threading as thread
import jmsets as jms

padding = {"padx": 5, "pady": 5}


class MyThread(thread.Thread):
    def __init__(self, target, arguments):
        super().__init__()
        self.target = target
        self.arguments = arguments
        self.return_values = None
    
    def run(self):
        self.return_values = self.target(*self.arguments)


class App(tk.Tk):
    def __init__(self):     
        super().__init__()
        self.title("JM Sets GUI")
        self.resizable(0,0)
        self.iconphoto(True, tk.PhotoImage(file="icon.png"))

        # Julia set variables
        self.jl_param_r = tk.DoubleVar(value=0.0)
        self.jl_param_i = tk.DoubleVar(value=0.0)
        self.jl_cardioid = tk.DoubleVar(value=0.0)

        self.jl_reg_bool = tk.BooleanVar(value=False)
        self.jl_reg_x = tk.DoubleVar(value=None)
        self.jl_reg_y = tk.DoubleVar(value=None)
        self.jl_reg_dx = tk.DoubleVar(value=None)
        self.jl_reg_dy = tk.DoubleVar(value=None)

        # Customization variables
        self.custom_maxiter = tk.IntVar(value=2)
        self.custom_width = tk.IntVar(value=400)
        self.custom_height = tk.IntVar(value=400)
        self.custom_colormap = tk.StringVar(value="Blues")

        self.create_window()

    def create_window(self):
        frame = tk.Frame(self)
        # Objects
        lbf_jl = tk.LabelFrame(frame, text="Julia set")
        lbl_jl_param = tk.Label(lbf_jl, text="Parameter:")
        box_param_r = tk.Entry(lbf_jl, width=10, textvariable=self.jl_param_r)
        box_param_i = tk.Entry(lbf_jl, width=10, textvariable=self.jl_param_i)
        chk_cardioid = tk.Checkbutton(lbf_jl, text="Cardioid", onvalue=True,
            offvalue=False)
        box_cardioid = tk.Entry(lbf_jl, width=10, textvariable=self.jl_cardioid,
            state=tk.DISABLED)
        btn_jl_plot = tk.Button(lbf_jl, text="Submit", command=self.submit)
        
        chk_jl_region = tk.Checkbutton(lbf_jl, text="Region around",
            variable=self.jl_reg_bool, onvalue=True, offvalue=False)
        lbl_jl_reg_x = tk.Label(lbf_jl, text="Point (x,y):")
        lbl_jl_reg_y = tk.Label(lbf_jl, text="Delta (x,y):")
        box_jl_reg_x = tk.Entry(lbf_jl, width=10,
            textvariable=self.jl_reg_x, state=tk.DISABLED)
        box_jl_reg_y = tk.Entry(lbf_jl, width=10, 
            textvariable=self.jl_reg_y, state=tk.DISABLED)
        box_jl_reg_dx = tk.Entry(lbf_jl, width=10, 
            textvariable=self.jl_reg_dx, state=tk.DISABLED)
        box_jl_reg_dy = tk.Entry(lbf_jl, width=10,
            textvariable=self.jl_reg_dy, state=tk.DISABLED)

        lbf_custom = tk.LabelFrame(frame, text="Customization")
        lbl_custom_maxiter = tk.Label(lbf_custom, text="Max iteration:")
        spb_custom_maxiter = tk.Spinbox(lbf_custom, from_=1, to=1000,
            width=10, textvariable=self.custom_maxiter, wrap=True)
        lbl_custom_width = tk.Label(lbf_custom, text="Width:")
        lbl_custom_height = tk.Label(lbf_custom, text="Height:")
        box_custom_width= tk.Entry(lbf_custom, width=10,
            textvariable=self.custom_width)
        box_custom_height = tk.Entry(lbf_custom, width=10,
            textvariable=self.custom_height)
        lbl_custom_colormap = tk.Label(lbf_custom, text="Colormap:")
        cmb_custom_colormap = ttk.Combobox(lbf_custom, values=jms.colormaps,
            width=10, textvariable=self.custom_colormap)

        status_bar = tk.Frame(frame)
        status_bar.columnconfigure(0, weight=3)
        status_bar.columnconfigure(1, weight=1)
        self.progress_bar = ttk.Progressbar(status_bar, mode="indeterminate")

        # Object placing
        frame.grid(column=0, row=0, **padding)
        lbf_jl.grid(column=0, row=0, **padding)
        lbl_jl_param.grid(column=0, row=1, sticky=tk.W, **padding)
        box_param_r.grid(column=1, row=1, **padding)
        box_param_i.grid(column=2, row=1, **padding)
        chk_cardioid.grid(column=1, row=2, **padding)
        box_cardioid.grid(column=2, row=2, sticky=tk.EW, **padding)
        btn_jl_plot.grid(column=3, row=2, sticky=tk.EW, **padding)
        box_param_r.focus()

        chk_jl_region.grid(column=0, row=3, **padding)
        lbl_jl_reg_x.grid(column=0, row=4, sticky=tk.W, **padding)
        lbl_jl_reg_y.grid(column=0, row=5, sticky=tk.W, **padding)
        box_jl_reg_x.grid(column=1, row=4, **padding)
        box_jl_reg_y.grid(column=2, row=4, **padding)
        box_jl_reg_dx.grid(column=1, row=5, **padding)
        box_jl_reg_dy.grid(column=2, row=5, **padding)

        lbf_custom.grid(column=0, row=1, sticky=tk.NSEW, **padding)
        lbl_custom_maxiter.grid(column=0, row=0, **padding)
        spb_custom_maxiter.grid(column=1, row=0, sticky=tk.EW, **padding)
        lbl_custom_width.grid(column=0, row=1, sticky=tk.W, **padding)
        lbl_custom_height.grid(column=2, row=1, **padding)
        box_custom_width.grid(column=1, row=1, sticky=tk.EW, **padding)
        box_custom_height.grid(column=3, row=1, **padding)
        lbl_custom_colormap.grid(column=0, row=2, sticky=tk.W, **padding)
        cmb_custom_colormap.grid(column=1, row=2, sticky=tk.EW, **padding)

        status_bar.grid(column=0, row=2, sticky=tk.EW, padx=5)
        self.progress_bar.grid(column=1, row=0, sticky=tk.E)

        # Methods
        def toggle_limits(self):
            state = box_jl_reg_x.config("state")[-1]
            if state == tk.DISABLED:
                box_jl_reg_x.config(state=tk.NORMAL)
                box_jl_reg_y.config(state=tk.NORMAL)
                box_jl_reg_dx.config(state=tk.NORMAL)
                box_jl_reg_dy.config(state=tk.NORMAL)
            else:
                box_jl_reg_x.config(state=tk.DISABLED)
                box_jl_reg_y.config(state=tk.DISABLED)
                box_jl_reg_dx.config(state=tk.DISABLED)
                box_jl_reg_dy.config(state=tk.DISABLED)

        def toggle_cardioid(self):
            state = box_cardioid.config("state")[-1]
            if state == tk.DISABLED:
                box_cardioid.config(state=tk.NORMAL)
                box_param_r.config(state=tk.DISABLED)
                box_param_i.config(state=tk.DISABLED)
            else:
                box_cardioid.config(state=tk.DISABLED)
                box_param_r.config(state=tk.NORMAL)
                box_param_i.config(state=tk.NORMAL)

        def update_cparam(dummy):
            alpha = self.jl_cardioid.get()
            cparam = jms.main_cardioid(alpha)
            real = cparam.real
            imag = cparam.imag
            self.jl_param_r.set(real)
            self.jl_param_i.set(imag)


        chk_jl_region.bind("<Button-1>", toggle_limits)
        chk_jl_region.bind("<space>", toggle_limits)
        chk_cardioid.bind("<Button-1>", toggle_cardioid)
        chk_cardioid.bind("<space>", toggle_cardioid)
        box_cardioid.bind("<Return>", update_cparam)

        # Menu
        menubar = tk.Menu(self)
        self.config(menu=menubar)
        file_menu = tk.Menu(menubar, tearoff=False)
        file_menu.add_command(label="Exit", command=self.destroy)
        menubar.add_cascade(label="File", menu=file_menu, underline=0)

    def monitor_thread(self, thread):
        if thread.is_alive():
            self.after(100, lambda: self.monitor_thread(thread))
        else:
            colormap = self.custom_colormap.get()
            self.progress_bar.stop()
            jms.plotter(*thread.return_values, colormap)

    def submit(self):
        # Julia c parameter
        a = self.jl_param_r.get()
        b = self.jl_param_i.get()
        c_param = complex(a, b)

        # Region point and limits
        region = None
        if self.jl_reg_bool.get():
            point_x = self.jl_reg_x.get()
            point_y = self.jl_reg_y.get()
            delta_x = self.jl_reg_dx.get()
            delta_y = self.jl_reg_dy.get()
            region = [point_x, point_y, delta_x, delta_y]

        # Customization
        width = self.custom_width.get()
        height = self.custom_height.get()
        maxiter = self.custom_maxiter.get()

        # Running
        thread_run_julia = MyThread(jms.julia_set, 
            [c_param, region, width, height, maxiter])
        thread_run_julia.start()
        self.progress_bar.start(20)
        self.monitor_thread(thread_run_julia)


if __name__ == "__main__":
    app = App()
    app.mainloop()