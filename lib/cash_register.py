#!/usr/bin/env python3

class CashRegister:


  def __init__(self, discount = 0, total = 0):
    self.discount  = discount 
    self.total = total
    self.items = list()
    self.last_transaction =0

  def add_item(self, title, price, quantity=1,):
    self.title = title
    self.last_transaction = price * quantity
    self.total += self.last_transaction
    for _ in range(quantity):
      self.items.append(title)
    return self.items
  

  def apply_discount(self):
    if (self.discount > 0):
      self.total  *= ((100 - self.discount)/100)
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")


  def void_last_transaction(self):
    self.total -= self.last_transaction





  
  



