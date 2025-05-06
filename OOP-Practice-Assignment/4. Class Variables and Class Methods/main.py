#Assignment No-4:
#Create a class Bank with a class variable bank_name. 
#Add a class method change_bank_name(cls, name) that allows changing the bank name. 
#Show that it affects all instances.

class Bank:
    bank_name = "JS Bank"

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name
        return cls.bank_name

# Branch 1
JS_Branch_1 = Bank()
print(JS_Branch_1.bank_name)
print(JS_Branch_1.change_bank_name("JS Bank 1"))

# Branch 2
JS_Branch_2 = Bank() # Branch 2 uses the same bank name as Branch 1, which is "JS Bank 1"
print(JS_Branch_2.bank_name) # Branch 2 will have a different bank name: "JS Bank 2".
print(JS_Branch_2.change_bank_name("JS Bank 2"))

print("Printing Branch 1 again to show that the bank name has been changed to 'JS Bank 2' by Branch 2.")
print(JS_Branch_1.bank_name)