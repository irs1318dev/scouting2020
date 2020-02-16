import bokeh.models.widgets as bmw
import bokeh.plotting as plt
import bokeh.layouts as blay

import viewer as svv

viewer = svv.Viewer()
plot_6t = viewer.total_6t('001-q')
select = bmw.Select(title='Match', options=viewer.list_matches())
select.on_change('value', viewer.callback_6t)
plt.curdoc().add_root(blay.row(select, plot_6t))

