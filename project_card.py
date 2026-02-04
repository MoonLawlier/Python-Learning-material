''' 1 usd = 86.448 rupee'''

currencies = {
    "INR":1,
    "USD":86.448,
    "EUR":91.63488,
    "YEN":0.5792061,
    "GBP":106.33104,
    "AUD":55.32672,
    "CAD":63.97152,
}
def to_inr():
    cur = input("")
    amt = int(input())
    if(cur == "USD"):
        rate = 86.448
    elif(cur == "INR"):
        rate = (amt)
    elif(cur == "EUR"):
        rate = 91.63488
    elif(cur == "YEN"):
        rate =0.5792061
    elif(cur == "GBP"):
        rate = 106.33104
    elif(cur == "AUD"):
        rate = 55.32672
    elif(cur == "CAD"):
        rate = 63.97152
    else:
        raise Exception(f"{cur} is not supported")
    
    if (amt<0):
        return ("Invalid input")
    
    return amt*rate

def to_inr():
    cur = input("")
    amt = int(input())
    if(cur == "USD"):
        rate = 0.0115676
    elif(cur == "INR"):
        rate = 1
    elif(cur == "EUR"):
        rate = 0.01091287
    elif(cur == "YEN"):
        rate =1.726501153
    elif(cur == "GBP"):
        rate = 0.009404591
    elif(cur == "AUD"):
        rate = 0.018074449
    elif(cur == "CAD"):
        rate = 0.015631956
    else:
        raise Exception(f"{cur} is not supported")
    
    if (amt<0):
        return ("Invalid input")
    
    return round(amt*rate,4)
        
change = to_inr()
print(change)    


