if text== "=":
        if value.get().isdigit():
            val=int(value.get())
        else:
            val=eval(screen.get())
        value.set(val)
        screen.update()