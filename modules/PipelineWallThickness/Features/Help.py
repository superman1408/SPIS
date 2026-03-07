from PyQt5.QtWidgets import QMessageBox



# function to use the 
# askquestion() function
def Help(): 
   msgBox = QMessageBox()
   msgBox.setIcon(QMessageBox.Information)
   msgBox.setText("Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files , to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:")
   msgBox.setWindowTitle("Documentation")
   msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
#    msgBox.buttonClicked.connect(msgButtonClick)

   returnValue = msgBox.exec()
   if returnValue == QMessageBox.Ok:
      print('OK clicked')
	
# setting geometry of window 
# instance
# main.geometry("100x100")

# creating Window
# B1 = Button(main, text = "Help", command = Help) 

# Button positioning 
# B1.pack() 

# infinite loop till close
# main.mainloop() 
