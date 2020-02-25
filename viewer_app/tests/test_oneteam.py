import viewer_app.oneteam_climb as otc
import viewer_app.data_source as ds

def test_oneteam():
    data = ds.DataSource()
    oneteam = otc.OneTeam(data)
    return oneteam.total_1t('1318', ['shootUpper', 'climbPosition'])

