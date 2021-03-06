from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable

from contoller.controller import ControllerComponent
from model.model import ModelComponent

from kivy.core.window import Window
from kivy.metrics import dp


class TableApplication(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.54},
            size_hint={0.9, 0.8},
            use_pagination=True,
            rows_num=7,
            column_data=[
                ('Full name', dp(40)),
                ('Father name', dp(40)),
                ('Father wage', dp(30)),
                ('Mother name', dp(40)),
                ('Mother wage', dp(30)),
                ('Brothers', dp(25)),
                ('Sisters', dp(25)),
            ],
        )
        self.model = ModelComponent(table=self.table)
        self.controller = ControllerComponent(self.model)
        self.controller.upload_from_file('excellent.xml')

    def build(self):
        Window.size = (1280, 800)
        return self.controller.get_screen()


TableApplication().run()
