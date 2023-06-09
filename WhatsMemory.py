import datetime
from datetime import *
import pywhatkit as kit



x=0
y=1

while(x<y):
    now = datetime.today()
    if(now.strftime('%I')=='00'):
       x=1
       y=0
       kit.sendwhatmsg('+393202133183','Ricordati le heets! Dopo ti do i soldi',7,30)
       kit.sendwhatmsg('+393490913375','Sei arrivata?',8,00)
       kit.sendwhatmsg('+393515704377', 'è ora di lavorare!', 8,30)
    x=0
    y=1



