<# Starts the Vis application in normal mode, Windows only.

 Vis stands for *V*iewer of *I*rs *S*ql scouting data. The Vis
 application connects directly to the IRS scouting system's SQL server
 and displays scouting data as charts and tables. It does not do
 anything else, such as accept connections from tablets or write
 data to the SQL database.

This *.ps1 file is a Windows PowerShell scripting file that will only
 work on Windows. For Apple or Linux computers, use a shell script.
#>
write-host $args
bokeh serve --show viewer_app --args sql $args[0]