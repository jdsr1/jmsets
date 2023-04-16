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

        # Fractal Jl/Ml sets variables
        self.chosen_set = tk.IntVar(value=1)
        self.jl_param_r = tk.DoubleVar(value=0.285)
        self.jl_param_i = tk.DoubleVar(value=0.0)
        self.jl_cardioid = tk.DoubleVar(value=0.0)

        # Customization variables
        self.region_bool = tk.BooleanVar(value=False)
        self.region_x = tk.DoubleVar(value=None)
        self.region_y = tk.DoubleVar(value=None)
        self.region_dx = tk.DoubleVar(value=None)
        self.region_dy = tk.DoubleVar(value=None)

        self.custom_maxiter = tk.IntVar(value=64)
        self.custom_width = tk.IntVar(value=400)
        self.custom_height = tk.IntVar(value=400)
        self.custom_colormap = tk.StringVar(value="Blues")

        self.create_window()

    def create_window(self):
        frame = tk.Frame(self)
        last_state = tk.IntVar(value=2)

        # Objects from fractal label frame
        lbf_fractal = tk.LabelFrame(frame, text="Fractal")

        rbt_julia = tk.Radiobutton(lbf_fractal, text="Julia", value=1, 
            variable=self.chosen_set)
        lbl_jl_param = tk.Label(lbf_fractal, text="Parameter:")
        box_param_r = tk.Entry(lbf_fractal, width=10, textvariable=self.jl_param_r)
        box_param_i = tk.Entry(lbf_fractal, width=10, textvariable=self.jl_param_i)
        chk_cardioid = tk.Checkbutton(lbf_fractal, text="Cardioid", onvalue=True,
            offvalue=False)
        box_cardioid = tk.Entry(lbf_fractal, width=10, textvariable=self.jl_cardioid,
            state=tk.DISABLED)
        rbt_mandelbrot = tk.Radiobutton(lbf_fractal, text="Mandelbrot", value=2,
            variable=self.chosen_set)
        btn_plotter = tk.Button(lbf_fractal, text="Plot", command=self.submit)
        
        # Objects for customization label frame
        lbf_custom = tk.LabelFrame(frame, text="Customization")

        chk_region = tk.Checkbutton(lbf_custom, text="Region around",
            variable=self.region_bool, onvalue=True, offvalue=False)
        lbl_region_pt = tk.Label(lbf_custom, text="Point (x,y):")
        lbl_region_dt = tk.Label(lbf_custom, text="Delta (x,y):")
        box_region_x = tk.Entry(lbf_custom, width=10,
            textvariable=self.region_x, state=tk.DISABLED)
        box_region_y = tk.Entry(lbf_custom, width=10, 
            textvariable=self.region_y, state=tk.DISABLED)
        box_region_dx = tk.Entry(lbf_custom, width=10, 
            textvariable=self.region_dx, state=tk.DISABLED)
        box_region_dy = tk.Entry(lbf_custom, width=10,
            textvariable=self.region_dy, state=tk.DISABLED)

        lbl_custom_maxiter = tk.Label(lbf_custom, text="Max iteration:")
        spb_custom_maxiter = tk.Spinbox(lbf_custom, from_=1, to=1000,
            width=10, textvariable=self.custom_maxiter, wrap=True)
        lbl_custom_width = tk.Label(lbf_custom, text="Width & height:")
        lbl_custom_height = tk.Label(lbf_custom, text="Height:")
        box_custom_width= tk.Entry(lbf_custom, width=10,
            textvariable=self.custom_width)
        box_custom_height = tk.Entry(lbf_custom, width=10,
            textvariable=self.custom_height)
        lbl_custom_colormap = tk.Label(lbf_custom, text="Colormap:")
        cmb_custom_colormap = ttk.Combobox(lbf_custom, values=jms.colormaps,
            width=10, textvariable=self.custom_colormap)

        # Status bar
        status_bar = tk.Frame(frame)
        status_bar.columnconfigure(0, weight=3)
        status_bar.columnconfigure(1, weight=1)
        self.progress_bar = ttk.Progressbar(status_bar, mode="indeterminate")

        # Place objects from fractal frame
        frame.grid(column=0, row=0, **padding)
        lbf_fractal.grid(column=0, row=0, sticky=tk.NSEW, **padding)

        rbt_julia.grid(column=0, row=0, sticky=tk.W, **padding)
        rbt_mandelbrot.grid(column=0, row=3, sticky=tk.W, **padding)
        lbl_jl_param.grid(column=0, row=1, sticky=tk.W, **padding)
        box_param_r.grid(column=1, row=1, sticky=tk.EW, **padding)
        box_param_i.grid(column=2, row=1, sticky=tk.EW, **padding)
        chk_cardioid.grid(column=1, row=2, sticky=tk.W, **padding)
        box_cardioid.grid(column=2, row=2, sticky=tk.EW, **padding)
        btn_plotter.grid(column=3, row=3, sticky=tk.E, **padding)
        box_param_r.focus()

        # Place objects from customization frame
        lbf_custom.grid(column=0, row=1, sticky=tk.NSEW, **padding)

        chk_region.grid(column=0, row=0, **padding)
        lbl_region_pt.grid(column=0, row=1, sticky=tk.W, **padding)
        lbl_region_dt.grid(column=0, row=2, sticky=tk.W, **padding)
        box_region_x.grid(column=1, row=1, sticky=tk.EW, **padding)
        box_region_y.grid(column=2, row=1, sticky=tk.EW, **padding)
        box_region_dx.grid(column=1, row=2, sticky=tk.EW, **padding)
        box_region_dy.grid(column=2, row=2, sticky=tk.EW, **padding)

        lbl_custom_maxiter.grid(column=0, row=3, sticky=tk.W, **padding)
        spb_custom_maxiter.grid(column=1, row=3, sticky=tk.EW, **padding)
        lbl_custom_width.grid(column=0, row=4, sticky=tk.W, **padding)
        #lbl_custom_height.grid(column=2, row=4, **padding)
        box_custom_width.grid(column=1, row=4, sticky=tk.EW, **padding)
        box_custom_height.grid(column=2, row=4, sticky=tk.EW, **padding)
        lbl_custom_colormap.grid(column=0, row=5, sticky=tk.W, **padding)
        cmb_custom_colormap.grid(column=1, row=5, sticky=tk.EW, **padding)

        # Place status bar
        status_bar.grid(column=0, row=2, sticky=tk.EW, padx=5)
        self.progress_bar.grid(column=1, row=0, sticky=tk.E)

        # Events and methods
        def toggle_limits(self):
            state = box_region_x.config("state")[-1]
            if state == tk.DISABLED:
                box_region_x.config(state=tk.NORMAL)
                box_region_y.config(state=tk.NORMAL)
                box_region_dx.config(state=tk.NORMAL)
                box_region_dy.config(state=tk.NORMAL)
            else:
                box_region_x.config(state=tk.DISABLED)
                box_region_y.config(state=tk.DISABLED)
                box_region_dx.config(state=tk.DISABLED)
                box_region_dy.config(state=tk.DISABLED)

        def toggle_cardioid(self):
            state = box_cardioid.config("state")[-1]
            if state == tk.DISABLED:
                box_cardioid.config(state=tk.NORMAL)
                box_param_r.config(state=tk.DISABLED)
                box_param_i.config(state=tk.DISABLED)
                last_state.set(1)
            else:
                box_cardioid.config(state=tk.DISABLED)
                box_param_r.config(state=tk.NORMAL)
                box_param_i.config(state=tk.NORMAL)
                last_state.set(2)

        def update_cparam(dummy):
            alpha = self.jl_cardioid.get()
            cparam = jms.main_cardioid(alpha)
            real = cparam.real
            imag = cparam.imag
            self.jl_param_r.set(real)
            self.jl_param_i.set(imag)

        def toggle_jlml():
            lstate = last_state.get()
            choice = self.chosen_set.get()
            if choice == 2 and lstate == 2:
                box_param_r.config(state=tk.DISABLED)
                box_param_i.config(state=tk.DISABLED)
                chk_cardioid.config(state=tk.DISABLED)
            elif choice == 2:
                chk_cardioid.config(state=tk.DISABLED)
                box_cardioid.config(state=tk.DISABLED)
            elif choice == 1 and lstate == 2:
                box_param_r.config(state=tk.NORMAL)
                box_param_i.config(state=tk.NORMAL)
                chk_cardioid.config(state=tk.NORMAL)
            else:
                chk_cardioid.config(state=tk.NORMAL)
                box_cardioid.config(state=tk.NORMAL)

        chk_region.bind("<Button-1>", toggle_limits)
        chk_region.bind("<space>", toggle_limits)
        chk_cardioid.bind("<Button-1>", toggle_cardioid)
        chk_cardioid.bind("<space>", toggle_cardioid)
        box_cardioid.bind("<Return>", update_cparam)
        rbt_julia.config(command=toggle_jlml)
        rbt_mandelbrot.config(command=toggle_jlml)

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
            args = [*thread.return_values, colormap]
            #thread_plotter = MyThread(jms.plotter, args)
            #thread_plotter.start()
            jms.plotter(*args)

    def submit(self):
        choice = self.chosen_set.get()
        # Julia c parameter
        a = self.jl_param_r.get()
        b = self.jl_param_i.get()
        c_param = complex(a, b)

        # Region point and limits
        region = None
        if self.region_bool.get():
            point_x = self.region_x.get()
            point_y = self.region_y.get()
            delta_x = self.region_dx.get()
            delta_y = self.region_dy.get()
            region = [point_x, point_y, delta_x, delta_y]

        # Customization
        width = self.custom_width.get()
        height = self.custom_height.get()
        maxiter = self.custom_maxiter.get()

        # Create thread and run
        if choice == 1:
            thread_choice = MyThread(
                jms.julia_set, 
                [c_param, region, width, height, maxiter]
            )
        elif choice == 2:
            thread_choice = MyThread(
                jms.mandelbrot_set, 
                [region, width, height, maxiter]
            )

        thread_choice.start()
        self.progress_bar.start(20)
        self.monitor_thread(thread_choice)


if __name__ == "__main__":
    app = App()
    app.mainloop()