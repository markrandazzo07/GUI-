import tkinter as gui

def display(name):
    window = gui.Tk()
    window.title('Login Screen')

    userName = f"Welcome {name}!"  
    welcome = gui.Label(window, text=userName)
    welcome.pack()

    grid_frame = gui.Frame(window)
    grid_frame.pack()

    fwd_btn     = gui.Button(grid_frame, text = "FORWARD")
    fwd_btn.grid(row = 0, column = 1)

    left_btn    = gui.Button(grid_frame, text = "LEFT")
    left_btn.grid(row = 1, column = 0)

    right_btn   = gui.Button(grid_frame, text = "RIGHT")
    right_btn.grid(row = 1, column = 2)

    stop_btn    = gui.Button(grid_frame, text = "STOP")
    stop_btn.grid(row = 1, column = 1)

    bwd_btn     = gui.Button(grid_frame, text = "BACKWARD")
    bwd_btn.grid(row = 2, column = 1)

    video_frame = gui.Frame(window)
    video_frame.pack()

    log_text = gui.Text(window)
    log_text.pack()

    black_field = gui.Text(window)
    black_field.pack()

    window.mainloop()