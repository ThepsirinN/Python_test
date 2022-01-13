from IPython.display import clear_output
import time
s = 59
m = 00
h = 2
x = h*3600 + m*60 + s 
for i in range(x):
    sec = x - i
    print("(H:m:s) - ",sec//(60*60),":",sec//60 - ((60)*(sec//(60*60))),":",sec - 60*(sec//60))
    time.sleep(1)
    clear_output()
