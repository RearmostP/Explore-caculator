from ui.main_ui import *

class ExpenseApp(App):
    def build(self):
        return Root()

if __name__ == "__main__":
    ExpenseApp().run()
