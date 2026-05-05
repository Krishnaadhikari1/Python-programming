# Polymorphism means same method name but different behavior.
 
class djangodeveloper:
    def work(self):
        print("building backend APIs")

class mldeveloper:
    def work(self):
        print("training  ml models")

developers=[ djangodeveloper(),mldeveloper()]

for dev in developers:
    dev.work()