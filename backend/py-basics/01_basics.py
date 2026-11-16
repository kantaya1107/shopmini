print("Hello Python")

shop_name = "ShopMini"          # str
price = 590                     # int
vat_rate = 0.07                 # float
is_active = True                # bool (ตัวพิมพ์ใหญ่ T)
discount = None                 # None เทียบได้กับ null ใน JavaScript

print(shop_name,price,vat_rate,is_active,discount);
print(f"{shop_name} ราคา {price} บาท VAT {vat_rate*100:.2f}% ราคาสุทธิ {price * (1+vat_rate):.2f}")

#การเขียนเงื่อนไข 
if price > 500:
    print("Free Shipping")
elif price > 300:
    print("Shipping fee 50")
else:
    print("Shipping fee 100")

print(type(price),type(vat_rate),type(discount))