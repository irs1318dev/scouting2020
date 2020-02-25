import bokeh.models.widgets as bk_model_widgets
import viewer_app.data_source as va_data_source
import viewer_app.main as va_main
from bokeh.io import curdoc


class DataFile:

    def __init__(self, data):
        self.data = data
        self.update_button = bk_model_widgets.Button(label='Update graphs')

    def callback_button(self):
        ds = va_data_source()
        for obj in va_main.plot_objects:
            obj.data = ds

    def layout_buttons(self):
        pass

    def panel_buttons(self):
        pass

    # update_button = bk_model_widgets.Button(label='Update graphs')
