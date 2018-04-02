import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)


import threading

count=0

def printit():
  global count
  threading.Timer(60.0, printit).start()
  count+=1
  print count
  if count==10000:
      count=0
  click(10,10)

printit()
