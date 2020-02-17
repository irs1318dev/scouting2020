import bokeh.plotting as plt

import viewer_app.viewer as svv

viewer = svv.Viewer()
layout = viewer.layout_6t('001-q')
plt.curdoc().add_root(layout)
