import sys

import bokeh.plotting as bk_plt
import bokeh.models as bk_models

import viewer_app.data_source as va_data_source
import viewer_app.sixteam as va_sixteam
import viewer_app.oneteam as va_oneteam

if sys.argv[1] == 'sql':
    data_source = va_data_source.DataSource(event='test_event_2', season='2020')

    panels = []

    sixteam = va_sixteam.SixTeam(data_source)
    panels.append(sixteam.panel('001-q'))

    oneteam_tasks = ['launchOuter', 'climbPosition']
    oneteam = va_oneteam.OneTeam(data_source)
    panels.append(oneteam.panel_1t('1318', ['launchOuter', 'launchLower']))
    tabs = bk_models.Tabs(tabs=panels)
    bk_plt.curdoc().add_root(tabs)

else:
    print(f'You passed the argument {sys.argv[1]}.')
    print('No-SQL viewer not yet implemnted.')
