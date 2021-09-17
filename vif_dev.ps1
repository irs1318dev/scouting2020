<# Starts the Vif application in development mode, Windows only.

 Vif stands for *V*iewer of *I*rs *F*ile scouting data. The Vif
 application loads data from a Python pickle file and displays scouting
 data as charts and tables. It does not do  anything else, such as
 accept connections from tablets or write data to the SQL database.
 
 The first argument must be the name of the pickle file. The pickle
 file must be in the same folder as this shell script.

 The Python pickle file must have been created by the Vis application.

 In development mode, the bokeh server will automatically restart when
 it detects changes to the application files. Use this file when
 debugging or developing the Vis application.

 This *.ps1 file is a Windows PowerShell scripting file that will only
 work on Windows. For Apple or Linux computers, use a shell script.
#>
python -m bokeh serve --dev --show viewer_app --args $args[0]