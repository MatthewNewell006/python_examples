import webbrowser

url_1 = 'https://learn-2.galvanize.com/cohorts/2066'

temp_url = 'https://levelup.gitconnected.com/how-to-manipulate-web-browsers-using-python-21a69a17fe46'

'''

You will need to use two functions from the webbrowser module,
which is “webbrowser.open()” and “webbrowser.open_new_tab().”
“webbrowser.open()” is used to open your default web browser and goes to the first URL. “webbrowser.open_new_tab()”
will open the next URL onto the next tab.

#   webbrowser.open(url_1)
#   webbrowser.open_new_tab(url_2)
#   webbrowser.open_new_tab(url_3)
#   webbrowser.open_new_tab(url_4)
#   webbrowser.open_new_tab(url_5)

'''

webbrowser.open(url_1)
webbrowser.open(temp_url)