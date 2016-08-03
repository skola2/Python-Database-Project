from Tkinter import *

def show(s):
  val = False
  k = ''
  search = s.get().lower()
  datafile = open('UsersInfo.txt', 'r')
  for i in datafile:
    b = i.lower()
    if search in b:
      k += i + "\n"
      val = True
  if val == False:
    k = "No record found"
  frame(k)
  datafile.close()

def frame(v):
  root = Tk()
  root.title('Output')
  label = Label(root, text = v)
  label.pack()
  root.mainloop()


if __name__ == "__main__":
  root = Tk()
  root.title('Search')
  label1 = Label(root, text = "Search String")
  entry1 = Entry(root)
  label1.grid(row = 0, sticky = E)
  entry1.grid(row = 0, column = 1)
  button1 = Button(root, text = "Submit", fg = 'blue', command = lambda: show(entry1))
  button1.grid(row = 4, column = 0, columnspan = 2)
  root.mainloop()
