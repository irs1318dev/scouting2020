import bokeh.plotting as plt
import viewer_app.data_source as ds
import viewer_app.oneteam_climb as otc


oneteam = otc.OneTeam(ds.DataSource(event='test_event_2', season='2020'))
plot = oneteam.total_1t('1318', ['shootUpper', 'climbPosition'])
plt.curdoc().add_root(plot)

# import viewer_app.viewer as svv
#
# viewer = svv.Viewer()
# layout = viewer.layout_6t('001-q')
# plt.curdoc().add_root(layout)
