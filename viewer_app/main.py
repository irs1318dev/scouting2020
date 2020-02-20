import bokeh.plotting as bk_plt
import bokeh.models as bk_models

import viewer_app.data_source as va_data_source
import viewer_app.sixteam as va_sixteam
import viewer_app.oneteam_pc as va_oneteam_pc

data_source = va_data_source.DataSource(event='test_event_2', season='2020')
sixteam = va_sixteam.SixTeam(data_source)
oneteam = va_oneteam_pc.OneTeam(data_source)
panels = []
panels.append(sixteam.panel('001-q'))
panels.append(oneteam.panel('6350'))
tabs = bk_models.Tabs(tabs=panels)
bk_plt.curdoc().add_root(tabs)


