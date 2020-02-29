<# Starts the Vif application in normal mode, Windows only.

 Vif stands for *V*iewer of *I*rs *F*ile scouting data. The Vif
 application loads data from a Python pickle file and displays scouting
 data as charts and tables. It does not do  anything else, such as
 accept connections from tablets or write data to the SQL database.
 The pickle file must be named vif.pickle.

 The Python pickle file must have been created by the Vis application.

 This *.ps1 file is a Windows PowerShell scripting file that will only
 work on Windows. For Apple or Linux computers, use a shell script.
#>
bokeh serve --show viewer_app --args data.pickle