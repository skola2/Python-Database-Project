from Tkinter import *

global datafile
datafile = open("UsersInfo.txt",'a')
  
def main(ent):
  try:
    rows = ''
    k = 0
    for i in ent:
      k += 1
      q = i[1].get()
      
      if k == 1 or k == 2 or k == 3:
        if q.isalpha():
          rows += str(q + ', ')
        else:
          print "Enter only alphabets in First Name, Last Name and Program"
          return False
      else:
        if q.isdigit():
          rows += str(q)
        else:
          print "Enter only Numbers in Phone Number"
          return False
    print rows
    datafile.write(rows+"\n")
    return True

  except Exception, e:
    datafile.close()
    print e
  
fields = 'First Name', 'Last Name', 'Program', 'Phone Number'
#field_entries = 'aaaa','bbb', 'MBA', '123555566'

def close(root):
  datafile.close()
  print "Closed"
  root.destroy()
  

def makeform(root, fields):
  count = 0
  entries = []
  for field in fields:
    row = Frame(root)
    lab = Label(row, width=15, text=field, anchor='w')
    ent = Entry(row,state=NORMAL)
    #ent.insert(INSERT, field_entries[count])
    row.pack(side=TOP, fill=X, padx=5, pady=5)
    lab.pack(side=LEFT)
    ent.pack(side=RIGHT, expand=YES, fill=X)
    entries.append((field, ent))
    count += 1
  return entries

if __name__ == "__main__":
  root = Tk()
  root.title('Application Form')
  ents = makeform(root, fields)
  b1 = Button(root, text='Submit')
  b1.bind('<Button-1>', (lambda event, e=ents: main(e)))
  b1.pack(side=LEFT, padx=5, pady=5)
  b2 = Button(root, text='Quit', command = lambda: close(root))
  b2.pack(side=LEFT, padx=5, pady=5)
  root.mainloop()
