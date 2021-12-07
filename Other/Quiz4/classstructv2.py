from ctypes import *

class Vehicle(Structure):
    _fields_ = [ 
        ('model', (c_char * 30)),
        ('make', (c_char * 30)),
        ('max_speed_km', c_int),
        ('spare', c_int),
        ('owner', (c_char * 30))
    ]

myCar = Vehicle(b"Mercedes",b"GLK250", 240, 0, b"Jack")

model = ((c_char * 30)(*b'Mercedes'))                                            
make = ((c_char * 30)(*b'GLK250'))                                      
max_speed_km = (c_int)(240)                                                
spare = (c_int)(0)                                
owner = (c_char * 30)(*(b'Jack'))

print(model.value)
print(make.value)
print(max_speed_km.value)
print(spare.value)
print(owner.value)