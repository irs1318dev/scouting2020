import bokeh.models as bk_models
import bokeh.models.widgets as bk_widgets
import bokeh.layouts as bk_layouts
import viewer_app.data_source as va_data_source
import bokeh.io


class DataFile:

    def __init__(self, data_source):
        # self.update_button = bk_widgets.Button(label='Update graphs')
        self.layout = None
        self.data_source = data_source

    def callback_button(self):
        # ds1 = va_data_source.DataSource(event='test_event_2', season='2020')
        # check boolean attribute in data_source to see whether it's from a file or sql
        # if not self.data_source.from_sql:
        #     # bokeh.io.output_file('file_input.html')
        #     print("PRESSED THE FILE INPUT BUTTON!")
        #     file_input = bk_widgets.FileInput()
        #     print("ABOUT TO DISPLAY FILE INPUT DIALOG")
        #     bokeh.io.show(file_input)
        #     print("FILE SELECTED:", file_input.filename)
        #     # self.data_source.refresh(fname=file_input.filename)

        # else:
        #     self.data_source.refresh()
        # # for obj in self.data_source:
        # #     obj = ds1
        self.data_source.refresh()

    def layout_file_management(self):

        btn = bk_widgets.Button(label='Update graphs')
        btn.on_click(self.callback_button)
        # self.layout = bk_layouts.row(btn)

        col_layout = bk_layouts.Column(
            # bk_layouts.row(btn),
            btn,
            bk_models.Div(
                text=f'<h2>Data File: {self.data_source.fname}')
        )
        self.layout = col_layout
        return self.layout

    def panel_file_management(self):
                              # list_objects):
        self.layout_file_management()
            # list_objects)
        return bk_models.Panel(child=self.layout,
                               title='Data Management')
