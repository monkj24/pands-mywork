import myfunctions as mf

balance = 100

def withdraw(amount):
    global balance
    if amount < 0: 
        raise ValueError(" amount should always be greater then 0")
    if amount > balance:
        raise ValueError("not enough founds")
    balance =balance - amount
    return balance

if __name__ == "_main_":
    assert withdraw(20) == 80, "incorrect calculation"
    try:
      withdraw(-1)
      assert False, "should have thrown a value error"
    except ValueError as ve:
        pass
    
    try:
        withdraw(110)
        assert False, "can't withdraw more than is in balance"
    except ValueError as ve:
        pass

    print("all good")