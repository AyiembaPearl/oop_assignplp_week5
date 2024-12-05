#defining the class
class Phone:

    #initializing attributes
    def __init__(self, model, design, operating_system, colour, for_sale):
        #assigning attributes using self
        self.model = model
        self.design = design
        self.operating_system = operating_system
        self.colour = colour
        self.for_sale = for_sale

    #method/action/behaviour
    def features(self):
        print("{} phone has associated feautes:" .format(self.model))
        print("Design: {}" .format(self.design))
        print("Operating System: {}" .format(self.operating_system))
        print("Colour: {}" .format(self.colour))
        print("For Sale? {}" .format('Yes' if self.for_sale else 'No'))

    # Adding string representation method for meaningful printing
    def __str__(self):
        return "{} phone ({}), Operating System: {}, Colour: {}, For Sale: {}".format(
            self.model, self.design, self.operating_system, self.colour, 'Yes' if self.for_sale else 'No'
        )

#inheritance tablet inherits features of phone
class Tablet(Phone):
    #Initializing attributes
    def __init__(self, model, design, operating_system, colour, for_sale, screen_size):
        super(Phone, self).__init__(model, design, operating_system, colour, for_sale)  # call to Phone's __init__()
        self.screen_size = screen_size  # additional attribute for Tablet

    # overriding the features method to include screen size
    def features(self):
        super(Phone, self).features()  # call the parent class features method
        print("Screen Size: {} inches" .format(self.screen_size))

#objects with unique attributes
phone1 = Phone("Samsung", "Sleek", "Android", "Blue", False)
phone2 = Phone("Iphone", "Compact", "Apple", "Cream", True)
phone3 = Phone("Google pixel", "Sleek", "Android", "Green", True)
phone4 = Phone("Blackberry", "Compact", "Blackberry", "Orange", False)
phone5 = Phone("Burryn", "Sleek", "Windows", "Blue", True)
phone6 = Phone("Neold", "Compact", "Linux", "White",True)
#creating an instance for the tablet
tablet = Tablet("Hewlett-Packward Tab", "Sleek", "Android", "Black", True, 10.5)

#calling phone attributes
phone1.features()
phone2.features()
phone3.features()
phone4.features()
phone5.features()
phone6.features()
# #calling Tablet class function
tablet.features()