print("without graphics")
z = int(input("How many calculations do you want to make   "))
for x in range(z):
	print("1 = Addition")
	print("2 = Subtraction")
	print("3 = Multiplication")
	print("4 = division")
	print("5 = Average")
	print("6 = power ")
	print("7 = exit")
	a = int(input("Which of the following do you choose  "))
	b = int(input("Type a number   "))
	c = int(input("Type a 2nd number   "))
	if a == 1:
		print("The sum of ", b," and ", c, " is ", b+c)
	elif a == 2:
		print("The difference between ", b," and ", c, " is ", b-c)
	elif a == 3:
		print("The product of ", b," and ", c, " is ", b*c)
	elif a == 4:
		print("The quotient of ", b," and ", c, " is ", b/c)
	elif a==5:
		print("The average of ", b," and ", c, " is ", (b+c)/2)
	elif a == 6:
		print("the power of ", b, " and ", c, " is ", b^c)
	elif a == 7:
		exit()
print("With Graphics")
import math
import tkinter as tk
numer = ""
n = ""
a = 0
def number(no, fake):
    global numer, n, a
    if no == "":
        a = 1
    numer += no
    n += fake
    S.set(n)
    return
def bal(blabla):
    global numer, n, a
    if a == 1:
        asb = str(math.sqrt(eval(numer)))
        S.set(asb)
        numer = asb
        n = asb 
        a = 0
    else:
        try:
            asb = str(eval(numer))
            S.set(asb)
            numer = asb
            n = asb
        except:
            S.set(" Error ")
    return
def screen():
    global numer, a, n
    numer = ""
    n = ""
    S.set(n)
    return
root = tk.Tk()
root.configure(bg = "blue")
S = tk.StringVar()
E = tk.Label(root, textvariable = S, width = 15)
E.grid(columnspan = 4, ipadx = 40)
E.bind('<Return>', bal)
S.set("this is a calclator")
tk.Button(root, text = " clear ", width = 10, height = 4, command = lambda: screen()\
         , bg = "red").grid(row = 1, column = 0)
tk.Button(root, text = " exit ", width = 10, height = 4, command = lambda: exit()\
         , bg = "red").grid(row = 1, column = 1)
tk.Button(root, text = " % ", width = 10, height = 4, command = lambda: number("/100", "%")\
         , bg = "red").grid(row = 1, column = 2)
tk.Button(root, text = " / ", width = 10, height = 4, command = lambda: number("/", "÷")\
         , bg = "red").grid(row = 1, column = 3)
tk.Button(root, text = " √ ", width = 10, height = 4, command = lambda: number("", "√")\
         , bg = "red").grid(row = 1, column = 4)
tk.Button(root, text = " 7 ", width = 10, height = 4, command = lambda: number("7", "7")\
         , bg = "red").grid(row = 2, column = 0)
tk.Button(root, text = " 8 ", width = 10, height = 4, command = lambda: number("8", "8")\
         , bg = "red").grid(row = 2, column = 1)
tk.Button(root, text = " 9 ", width = 10, height = 4, command = lambda: number("9", "9")\
         , bg = "red").grid(row = 2, column = 2)
tk.Button(root, text = " ( ", width = 10, height = 4, command = lambda: number("(", "(")\
         , bg = "red").grid(row = 2, column = 3)
tk.Button(root, text = " × ", width = 10, height = 4, command = lambda: number("*", "×")\
         , bg = "red").grid(row = 2, column = 4)
tk.Button(root, text = " 4 ", width = 10, height = 4, command = lambda: number("4", "4")\
         , bg = "red").grid(row = 3, column = 0)
tk.Button(root, text = " 5 ", width = 10, height = 4, command = lambda: number("5", "5")\
         , bg = "red").grid(row = 3, column = 1)
tk.Button(root, text = " 6 ", width = 10, height = 4, command = lambda: number("6", "6")\
         , bg = "red").grid(row = 3, column = 2)
tk.Button(root, text = " ) ", width = 10, height = 4, command = lambda: number(")", ")")\
         , bg = "red").grid(row = 3, column = 3)
tk.Button(root, text = " - ", width = 10, height = 4, command = lambda: number("-", "-")\
         , bg = "red").grid(row = 3, column = 4)
tk.Button(root, text = " 1 ", width = 10, height = 4, command = lambda: number("1", "1")\
         , bg = "red").grid(row = 4, column = 0)
tk.Button(root, text = " 2 ", width = 10, height = 4, command = lambda: number("2", "2")\
         , bg = "red").grid(row = 4, column = 1)
tk.Button(root, text = " 3 ", width = 10, height = 4, command = lambda: number("3", "3")\
         , bg = "red").grid(row = 4, column = 2)
tk.Button(root, text = " π ", width = 10, height = 4, command = lambda: number("3.14285714285", "π")\
         , bg = "red").grid(row = 4, column = 3)
tk.Button(root, text = " + ", width = 10, height = 4, command = lambda: number("+", "+")\
         , bg = "red").grid(row = 4, column = 4)
tk.Button(root, text = " Exp ", width = 10, height = 4, command = lambda: number("e", "E")\
         , bg = "red").grid(row = 5, column = 0)
tk.Button(root, text = " ^ ", width = 10, height = 4, command = lambda: number("**", "^")\
         , bg = "red").grid(row = 5, column = 1)
tk.Button(root, text = " 0 ", width = 10, height = 4, command = lambda: number("0", "0")\
         , bg = "red").grid(row = 5, column = 2)
tk.Button(root, text = " . ", width = 10, height = 4, command = lambda: number(".", ".")\
         , bg = "red").grid(row = 5, column = 3)
tk.Button(root, text = " = ", width = 10, height = 4, command = lambda: bal(0)\
         , bg = "red").grid(row = 5, column = 4)
root.mainloop()