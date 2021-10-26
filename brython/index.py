import browser as br
#from browser import document
from browser.widgets.dialog import InfoDialog

import time

start = time.time()

msg = 'It has been {} seconds since you clicked the button.'
msg1 = 'It has been 1 second since you clicked the button.'
my_div = br.document['bry-playground']
my_text = my_div.select('p')[0]
my_text.textContent = 'Press the button to start.'


special_keys = {
    'metaKey': 'meta',
    'ctrlKey': 'ctrl',
    'altKey': 'alt',
    'shiftKey': 'shift',
}

@br.bind('#echo', 'click')
def my_click(ev):
    global start
    now = time.time()
    total = int(now - start)
    start = now

    if cmd := '-'.join(v for k, v in special_keys.items() if getattr(ev, k)):
        my_text.textContent = f"you {cmd}-clicked that button uwu"
    else:
        my_text.textContent = msg.format(total) if total != 1 else msg1
    #my_text.textContent = str(vars(ev))
#print(my_text)
#print(dir(my_text))
#def click(ev):
#    InfoDialog("hi", "Hello uwu!~")

# bind event 'click' on button to function echo
# document["echo"].bind("click", click)
