# Instance variables belong to each object. Each object can have different values.
class Phone:
    def __init__(self, brand , storage):
        self.brand=brand
        self.storage=storage

Phone1=Phone('iphone','512 gb')
Phone2=Phone('samsung','256 gb')

print(Phone1.brand)
print(Phone2.brand)
