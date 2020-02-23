import viewer_app.oneteam as otc
import viewer_app.data_source as ds


def test_oneteam():
    data = ds.DataSource(event='test_event_2', season='2020')
    oneteam = otc.OneTeam(data)
    return oneteam.total_1t('1318', ['shootUpper', 'climbPosition'])
