from kivy.app import App
from kivy.lang import Builder

Builder.load_file('box_layout.kv')


class BoxLayoutDemo(App):
    def build(self):
        """
        Build the root widget for the application.
        """
        return Builder.load_file('box_layout.kv')

    def handle_greet(self):
        """
        Handle the greeting action.
        """
        print("greet")
        name = self.root.ids.input_name.text
        self.root.ids.output_label.text = f"Hello {name}"

    def handle_clear(self):
        """
        Handle the clear action.
        """
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = ''


if __name__ == '__main__':
    BoxLayoutDemo().run()
