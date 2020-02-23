import bokeh.plotting as bk_plt
import bokeh.models as bk_models

import viewer_app.data_source as va_data_source
import viewer_app.sixteam as va_sixteam
import viewer_app.rankingtable as va_rankingtable
import viewer_app.tests.test_rankingtable as rt


rt.test_rankingtable()
data_source = va_data_source.DataSource(event='test_event_2', season='2020')
sixteam = va_sixteam.SixTeam(data_source)
rankingtable = va_rankingtable.rankingTable(data_source)
panels = []
panels.append(sixteam.panel('001-q'))
panels.append(rankingtable.panel())
tabs = bk_models.Tabs(tabs=panels)
bk_plt.curdoc().add_root(tabs)


