import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy import Config
from kivy.properties import ObjectProperty, StringProperty

class MyGrid(FloatLayout):
    slider1 = ObjectProperty(None)
    cm = 0
    kg = 0
    BMI = 0
    State = StringProperty('')
    cm_value = StringProperty('Height: 0 cm')
    kg_value = StringProperty('Height: 0 kg')
    BMI_value = StringProperty('BMI: 0')

    def slider_value_cm(self, instance, value):
        self.cm = int(value)
        self.cm_value = f"Height: {str(int(value))} cm"

    def slider_value_kg(self, instance, value):
        self.kg = int(value)
        self.kg_value = f"Weight: {str(int(value))} kg"

    def btn(self):
        self.BMI = int(self.kg / (self.cm / 100) ** 2)
        self.BMI_value = f"BMI: {int(self.kg / (self.cm / 100) ** 2)}"

        if self.BMI < 18.5:
            self.State = "Underweight"
        elif self.BMI >= 18.5 and self.BMI < 25:
            self.State = "Normal"
        elif self.BMI >= 25 and self.BMI < 30:
            self.State = "Overweight"
        else:
            self.State = "Obesity"

class MyApp(App):
    def build(self):
        self.title = "BMI calculator"
        self.icon = "img\icon.png"
        Window.clearcolor = 0.733, 0.749, 0.737, 1
        Window.size = 500, 600
        Config.set('graphics', 'resizable', False)
        Config.write()

        return MyGrid()
    
if __name__ == "__main__":
    MyApp().run()