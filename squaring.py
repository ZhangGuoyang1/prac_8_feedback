from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class SquaringWidget(BoxLayout):
    pass


class SquaringApp(App):
    def build(self):
        return SquaringWidget()

    def handle_calculate(self, input_text):
        try:
            # Convert the input text to an integer
            number = int(input_text)
            squared = number * number
            self.root.ids.result_label.text = f"Result: {squared}"
        except ValueError:
            # Display an error message if the conversion fails
            self.root.ids.result_label.text = "Error: Please enter a valid integer!"


if __name__ == '__main__':
    SquaringApp().run()
