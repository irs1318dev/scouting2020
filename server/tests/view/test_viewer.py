import pandas as pd

import server.view.bk_app.viewer as svv
import server.model.event as sme


def test_viewer():
    viewer = svv.Viewer(event='test_event_2', season='2020')
    evt = sme.EventDal.get_current_event()
    assert evt[1] == 'test_event_2'
    assert evt[2] == '2020'
    assert isinstance(viewer.measures, pd.DataFrame)
    assert viewer.measures.shape[0] > 1000
    assert viewer.measures.shape[1] == 20
    assert isinstance(viewer.schedule, pd.DataFrame)
    assert isinstance(viewer.teams, pd.DataFrame)
    matches = viewer.list_matches()
    assert len(matches) > 10
    assert matches[0] == '001-q'
