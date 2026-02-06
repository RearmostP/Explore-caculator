from kivy.app import App
from datetime import date

class Root(App):
    def save_expense(self):
        item = self.root.ids.item.text
        amount = self.root.ids.amount.text
        
        if not item or not amount:
            return
        
        self.logic.add_item(
            expense_name="כללי",
            list_name="יומי",
            item=item,
            amount=amount
        )
        
        self.root.ids.item.text = ""
        self.root.ids.amount.text = ""

    def calc_month(self):
        today = date.today()
        total = self.logic.total_for_month(
            str(today.year),
            today.month
        )
        self.root.ids.total_label.text = f"סך החודש: ₪ {total}"