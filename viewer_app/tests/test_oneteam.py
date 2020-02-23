<<<<<<< HEAD
import viewer_app.oneteam as otc
import viewer_app.data_source as ds


def test_oneteam():
    data = ds.DataSource(event='test_event_2', season='2020')
    oneteam = otc.OneTeam(data)
    return oneteam.total_1t('1318', ['shootUpper', 'climbPosition'])
=======
import viewer_app.oneteam_pc as vao
import viewer_app.data_source as vds
import pandas as pd

data = vds.DataSource(event='test_event_2', season='2020')
oneteam = vao.OneTeam(data)


def test_oneteam():
    assert isinstance(oneteam.measures, pd.DataFrame)
    assert isinstance(oneteam.schedule, pd.DataFrame)
    assert oneteam.measures.shape[1] == 20
    assert len(oneteam.list_teams()) > 15
    plot = oneteam.plot_1t('1318')
    print(plot)
    assert isinstance(oneteam.df_new_1t('1318'), pd.DataFrame)

>>>>>>> 704fd4039efc91ac4c82d265d915c9621699ad76
