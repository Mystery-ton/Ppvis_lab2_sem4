import os

from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


class DialogContent(BoxLayout):
    pass


class InputDialogContent(DialogContent):
    pass


class FilterDialogContent(DialogContent):
    pass


class DeleteDialogContent(DialogContent):
    pass


class UploadDialogContent(DialogContent):
    pass


class SaveDialogContent(DialogContent):
    pass


class DialogWindow(MDDialog):
    def __init__(self, **kwargs):
        super().__init__(
            title=kwargs['title'],
            type='custom',
            content_cls=kwargs['content_cls'],
            buttons=[
                MDFlatButton(text='OK', theme_text_color='Custom', on_release=self.close),
            ],
        )
        self.mode = kwargs['mode']
        self.view = kwargs['view']

    def close(self, obj):
        self.dismiss()
        self.view.close_dialog()


class InputWindow(DialogWindow):
    def __init__(self, **kwargs):
        super().__init__(
            title='Fill new student data:',
            content_cls=InputDialogContent(),
            mode='input',
            view=kwargs['view'],
        )

    def close(self, obj):
        self.dismiss()
        self.view.close_dialog(
            [
                self.content_cls.ids.input_name.text,
                self.content_cls.ids.input_father_name.text,
                self.content_cls.ids.input_father_wage.text,
                self.content_cls.ids.input_mother_name.text,
                self.content_cls.ids.input_mother_wage.text,
                self.content_cls.ids.input_brothers_number.text,
                self.content_cls.ids.input_sisters_number.text,
            ]
        )


class FilterWindow(DialogWindow):
    def __init__(self, **kwargs):
        super().__init__(
                title='''#Note: if you don't need some term of search, just don't fill it.\nFilter students:''',
                content_cls=FilterDialogContent(),
                mode="filter",
                view=kwargs["view"],
        )

    def close(self, obj):
        self.dismiss()
        self.view.close_dialog(
            [
                self.content_cls.ids.filter_first_name.text,
                self.content_cls.ids.filter_last_name.text,
                self.content_cls.ids.filter_parent_first_name.text,
                self.content_cls.ids.filter_parent_last_name.text,
                self.content_cls.ids.filter_siblings_number.text,
                self.content_cls.ids.filter_wage_lower.text,
                self.content_cls.ids.filter_wage_upper.text,
            ]
        )


class DeleteWindow(DialogWindow):
    def __init__(self, **kwargs):
        super().__init__(
                title="#Note: if you don't need some term of search, just don't fill it.\nDelete students: ",
                content_cls=DeleteDialogContent(),
                mode="delete",
                view=kwargs["view"],
        )

    def close(self, obj):
        self.dismiss()
        self.view.close_dialog(
            [
                self.content_cls.ids.delete_first_name.text,
                self.content_cls.ids.delete_last_name.text,
                self.content_cls.ids.delete_parent_first_name.text,
                self.content_cls.ids.delete_parent_last_name.text,
                self.content_cls.ids.delete_siblings_number.text,
                self.content_cls.ids.delete_wage_lower.text,
                self.content_cls.ids.delete_wage_upper.text,
            ]
        )


class SaveWindow(DialogWindow):
    def __init__(self, **kwargs):
        super().__init__(
                title="Saving: ",
                content_cls=SaveDialogContent(),
                mode="save",
                view=kwargs["view"],
        )

    def close(self, obj):
        self.dismiss()
        self.view.close_dialog(self.content_cls.ids.save_path.text)


class UploadWindow(DialogWindow):
    def __init__(self, **kwargs):
        super().__init__(
                title="Upload: ",
                content_cls=UploadDialogContent(),
                mode="upload",
                view=kwargs["view"],
        )

    def close(self, obj):
        self.dismiss()
        self.view.close_dialog(self.content_cls.ids.upload_path.text)


Builder.load_file(r'D:\Ppvis_lab2_sem4\utility\windows\windows.kv')
