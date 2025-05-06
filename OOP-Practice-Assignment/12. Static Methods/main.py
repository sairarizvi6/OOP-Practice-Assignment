#Assignment No-12:
#Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) 
#that returns the Fahrenheit value.

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 11/5) + 30
    
print(TemperatureConverter.celsius_to_fahrenheit(100))

