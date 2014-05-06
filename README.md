A python script to change the Desktop Background on your Linux Box.

<em>Installations:</em> 

sudo pip install beautifulsoup4

<em>Usage:-</em> 

python nasa_background.py

The script has been tested on Linux Mint Cinnamon. The last line of the script can be modified based on your machine's desktop environment.

For Ubuntu with Unity or Gnome Shell, modify the last line as follows:- 

os.system("gsettings set org.gnome.desktop.background picture-uri file://" + path + "/" + str(datetime.date.today())+".jpg")



==========================
