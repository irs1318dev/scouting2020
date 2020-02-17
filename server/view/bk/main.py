import bokeh.models.widgets as bmw
import bokeh.plotting as plt
import bokeh.layouts as blay

import server.view.bk.viewer as svv

viewer = svv.Viewer()
layout = viewer.layout_6t('001-q')
plt.curdoc().add_root(layout)
