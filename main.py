from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class CalculatorApp(App):
    def build(self):
        self.expression = ""
        
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.display = Label(
            text="0", 
            font_size=40,
            size_hint=(1, 0.3),
            halign='right'
        )
        self.display.bind(size=self.display.setter('text_size'))
        main_layout.add_widget(self.display)
        
        buttons = [
            ['C', '⌫', '/', '*'],
            ['7', '8', '9', '-'],
            ['4', '5', '6', '+'],
            ['1', '2', '3', '='],
            ['0', '.', '(', ')']
        ]
        
        for row in buttons:
            h_layout = BoxLayout(spacing=5)
            for label in row:
                button = Button(
                    text=label,
                    font_size=25,
                    on_press=self.button_pressed
                )
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)
        
        return main_layout
    
    def button_pressed(self, instance):
        current_text = instance.text
        
        if current_text == '=':
            try:
                result = str(eval(self.expression))
                self.display.text = result
                self.expression = result
            except:
                self.display.text = "Error"
                self.expression = ""
        elif current_text == 'C':
            self.expression = ""
            self.display.text = "0"
        elif current_text == '⌫':
            self.expression = self.expression[:-1]
            self.display.text = self.expression if self.expression else "0"
        else:
            if self.display.text == "0" or self.display.text == "Error":
                self.expression = current_text
            else:
                self.expression += current_text
            self.display.text = self.expression

if __name__ == '__main__':
    CalculatorApp().run()
