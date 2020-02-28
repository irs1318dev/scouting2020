import sys

import bokeh.plotting as bk_plt
import bokeh.models as bk_models

import viewer_app.data_source as va_data_source
import viewer_app.sixteam as va_sixteam
import viewer_app.oneteam as va_oneteam
import viewer_app.file_management as va_fm

if sys.argv[1] == 'sql':
    data_source = va_data_source.DataSource(event='test_event_2',
                                            season='2020')
else:
    data_source = va_data_source.DataSource(fname= 'vif.pickle')

panels = []

file_manager = va_fm.DataFile(data_source)
panels.append(file_manager.panel_file_management())

sixteam = va_sixteam.SixTeam(data_source)
panels.append(sixteam.panel('001-q'))

oneteam_tasks = ['launchOuter', 'climbPosition']
oneteam = va_oneteam.OneTeam(data_source)
panels.append(oneteam.panel_1t('1318', ['launchOuter', 'launchLower']))

tabs = bk_models.Tabs(tabs=panels)
bk_plt.curdoc().add_root(tabs)



