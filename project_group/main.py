from api import summary1
from cash_on_hand import summary2
from profit_loss import summary3
from overheads import summary4

def modular1() :
    return summary1
def modular2():
    return summary2
def modular3():
    return summary3
def modular4():
    return summary4
#create def for all the summary to write all the data into summary_report.txt

print(modular1())
print(modular2())
print(modular3())
print(modular4())
#print out all the def to run the function
