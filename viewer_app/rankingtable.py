import pandas as pd
import bokeh.plotting
import bokeh.models as bmodels
import bokeh.models.widgets as bmw
import bokeh.layouts as blt
import bokeh.plotting as plt
import bokeh.palettes as bpalettes
import bokeh.transform as btransform
import bokeh.io


class rankingTable:

    def __init__(self, data):
        self.data = data
        self.df = None
        self.datatable = None
        self.layout = None

    def df_ranktable(self):
        dft = self.data.teams.copy()
        dft = dft.set_index(['team'])
        df = dft.filter('team')
        dftotal = self.data.measures.copy()
        dftele = dftotal[dftotal.phase != 'auto']
        dfauto = dftotal[dftotal.phase == 'auto']
        dfclimb = dftotal[dftotal.task == 'climbPosition']
        dfclimb['successes'] = dfclimb['successes'] + 1
        shootertasks = ['shootLower', 'shootUpper']
        tasks = ['positionControl', 'rotationControl', 'movedAuto']
        for task in shootertasks:
            dft = dfauto[dfauto.task == task].groupby(['team']).mean()
            dft = dft[['successes']]
            dft = dft.rename(columns={'successes': task})
            df[task + 'Auto'] = dft[task]
        for task in shootertasks:
            dft = dftele[dftele.task == task].groupby(['team']).mean()
            dft = dft[['successes']]
            dft = dft.rename(columns={'successes': task})
            df[task + 'Tele'] = dft[task]
        for task in tasks:
            dft = dftotal[dftotal.task == task].groupby(['team']).sum()
            dft = dft[['successes']]
            dft = dft.rename(columns={'successes': task})
            df[task] = dft[task]
        dft = dfclimb[dfclimb.task == 'climbPosition'].groupby(['team']).sum()
        dft = dft[['successes']]
        dft = dft.rename(columns={'successes': 'climbPosition'})
        df['climbPosition'] = dft['climbPosition']
        self.df = df.fillna(0)
        return self.df

    def total_rt(self):
        Rank_cds = bmodels.ColumnDataSource(self.df)
        fixed2 = bmw.NumberFormatter(format='0.00')
        cols = [
            bmw.TableColumn(field='team', title='Team'),
            bmw.TableColumn(field='shootLowerAuto', title='Average Shoot Lower Auto', formatter=fixed2),
            bmw.TableColumn(field='shootUpperAuto', title='Average Shoot Upper Auto', formatter=fixed2),
            bmw.TableColumn(field='shootLowerTele', title='Average Shoot Lower Tele', formatter=fixed2),
            bmw.TableColumn(field='shootUpperTele', title='Average Shoot Upper Tele', formatter=fixed2),
            bmw.TableColumn(field='positionControl', title='Total position control', formatter=fixed2),
            bmw.TableColumn(field='rotationControl', title='Total Rotation Control', formatter=fixed2),
            bmw.TableColumn(field='movedAuto', title='Total moved auto', formatter=fixed2),
            bmw.TableColumn(field='climbPosition', title='Total Climbs', formatter=fixed2)
        ]
        self.datatable = bmw.DataTable(source=Rank_cds, columns=cols, width=1200, height=380)
        return self.datatable

    def create_layout(self):
        self.df = self.df_ranktable()
        self.datatable = self.total_rt()
        self.layout = blt.row(self.datatable)
        return self.layout

    def panel(self):
        self.layout = self.create_layout()
        return bmodels.Panel(child=self.layout, title='Ranking Table')
