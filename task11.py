'''11. 🛒 Ecommerce Products
# C → PhysicalProduct, DigitalProduct
# `get_delivery_method()` yoki `download()` metodlari har xil


11. 🛒 Elektron tijorat mahsulotlari
# Mahsulot → FizikaviyMahsulot, DigitalMahsulot
# `yetkazib_berish_usuli()` yoki `yuklab olish()` metodlari har xil


'''

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        return f"Mahsulot: {self.name}, Narxi: {self.price} so'm"

    def get_delivery_method():
        raise NotImplementedError("Hali bu metod mavjud emas!")

    def download():
        raise NotImplementedError("Hali bu metod mavjud emas!")


class PhysicalProduct(Product):

    def get_delivery_method(self):
        return f"{self.name} pochta orqali yetkazib beriladi."
    
    def download(self):
        return f"{self.name} yuklab bo'lamydi.Chunki u fizikaviy mahsulot."
    
class DigitalProduct(Product):
    
    def get_delivery_method(self):
        return f"{self.name} elektron pochta orqali yetkazib beriladi."
   
    def download(self):
        return f"{self.name} raqamli fayl orqali yuklash mumkin."
    
book = PhysicalProduct("Matematika", 30000)
online_kurs = DigitalProduct("Matematika bo'yicha Online Kurs", 200000)


print(book.info())
print(book.get_delivery_method())
print(book.download())
print()

print(online_kurs.info())
print(online_kurs.get_delivery_method())
print(online_kurs.download())