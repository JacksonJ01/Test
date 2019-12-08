class Wood:

    def __init__(self, wood_name):
        self.wood_name = wood_name

    def des(self):
        return "furnished with " + self.wood_name


class Table(Wood):
    def __init__(self, wood_name, use):
        super().__init__(wood_name)
        self.use = use


class Lights:
    def __init__(self, light_name):
        self.light_name = light_name

    def des1(self):
        return "old fashioned " + self.light_name + " lights"


class Wheels:
    def __init__(self, wheel_material, wheel_size):
        self.wheel_material = wheel_material
        self.wheel_size = wheel_size


class Chair:
    def __init__(self, chair_fabric, wheel_material, wheel_size):
        self.chair_fabric = chair_fabric
        self.wheels = Wheels(wheel_material, wheel_size)


class Classroom(Table, Chair, Lights):
    def __init__(self, wood_name, use, light_name, chair_fabric, wheel_material, wheel_size, room_number):
        Table.__init__(self, wood_name, use)
        Lights.__init__(self, light_name)
        Chair.__init__(self, chair_fabric, wheel_material, wheel_size)
        self.room_number = room_number

    def des2(self):
        return "Room " + str(self.room_number) + " is " + super().des() + " and it has " + super().des1()


wood = input(">>>")
table = input(">>>")
light = input(">>>")
fabric = input(">>>")
material = input(">>>")
size = input(">>>")
room = input(">>>")
MyClassRoom = Classroom(wood, table, light, fabric, material, size, room)

print(MyClassRoom.des2())
