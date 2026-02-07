import webbrowser as browser
import os
def autoopen():
    websites = input(" Enter the website(s) to open: ").lower().split()
    inpapp = input(" Enter the apps to open: ").lower().split()
    apps ={
        "vscode" : "C://Users//mdi72//OneDrive//ドキュメント//Desktop//VS Code.lnk",
        'winrar' : "C://Users//mdi72//AppData//Roaming//Microsoft//Windows//Start Menu//Programs//WinRAR//WinRAR.lnk",
        'oracle' : "C://Users//mdi72//OneDrive//ドキュメント//Desktop//sqldeveloper.lnk"
    }
    for ap in inpapp:
        if ap in apps:
            os.startfile(apps[ap])
        else:
            print("The app does not exist")
    path = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s'
    for link in websites:
        browser.get(path).open(link+".com")


autoopen()