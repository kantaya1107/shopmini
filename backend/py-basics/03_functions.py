# # Default Argument และ Keyword Argument
def calc_total(price, qty=1, discount=0):
    return price * qty - discount

print(calc_total(590))                        # 590
print(calc_total(590, 3))                     # 1770
print(calc_total(590, qty=3, discount=100))   # 1670 (ระบุชื่อพารามิเตอร์ จึงสลับลำดับได้)


# # Class เบื้องต้น
# class CartItem:
#     def __init__(self, name, price, qty=1):
#         self.name = name
#         self.price = price
#         self.qty = qty

#     def subtotal(self):
#         return self.price * self.qty

#     def __repr__(self):
#         return f"CartItem(name={self.name!r}, qty={self.qty})"


# item = CartItem("หูฟังบลูทูธ ANC", 2490, qty=2)
# print(item, item.subtotal())