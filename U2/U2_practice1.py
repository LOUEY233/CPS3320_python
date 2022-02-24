class info_collected():
    def __init__(self) -> None:
        self.name = 'name'
        self.age = 'age'
        self.address = 'address'
        self.favo_sport = 'favo_sport'

    def get_info(self,attr):
        if self.name == attr:
            self.name = input("please enter your name")
            print("Hello, my name is: {}".format(self.name))
        elif self.age == attr:
            self.age = input("please enter your age")
            print("I am {} years.".format(self.age))
        elif self.address == attr:
            self.adress =input("please enter your address")
            print("I live to {}".format(self.address))
        elif self.favo_sport == attr:
            self.favo_sport = input("please enter your favorite sport")
            print("I like to play {}".format(self.favo_sport))

if __name__ == '__main__':
    Data_Coll = info_collected()
    Data_Coll.get_info('name')
    Data_Coll.get_info('age')
    Data_Coll.get_info('address')
    Data_Coll.get_info('favo_sport')