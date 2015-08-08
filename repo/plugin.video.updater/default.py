import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,datetime,os
ADDON = xbmcaddon.Addon(id='plugin.video.updater')
AddonID = 'plugin.video.updater'
Addon = xbmcaddon.Addon(AddonID)
addonDir = Addon.getAddonInfo('path').decode("utf-8")
# Below Is Were You Default.py Should Be So If You Make Changes Just Upload To That Location And It Will Download When Update List Is Hit
BASE=("http://mykodi.co.uk/updater")
#Created By Pipcan.
#addon.xml location
url1 = ("http://mykodi.co.uk/updater/addon.xml")
#settings Location
url2 = ("http://mykodi.co.uk/updater/settings.xml")
#default.py location
url3 = ("http://mykodi.co.uk/updater/default.xml")
#changelog location
url4 = ("http://mykodi.co.uk/updater/changelog.xml")
version = Addon.getAddonInfo('version')
#version number location
current=urllib.urlopen('http://mykodi.co.uk/updater/version.txt').read()

def CATEGORIES():
        if current <> "%s"%(version):
            addDir2('[COLOR red]You Version Out of Date[/COLOR] - [I]Click To Update[/I]','dd',4,'%s/resources/icons/report.png'%(addonDir))
        else:
            addDir2('[COLOR green]You Are Up To Date[/COLOR]','about',4,'%s/resources/icons/report.png'%(addonDir))
        addDir('[B]DEMO[/B] - [I]Click To Install[/I]','http://mykodi.co.uk/downloadtest.zip',3,'')

        
def DownloaderClass(url,dest):
    dp = xbmcgui.DialogProgress()
    dp.create("Iptv Manager","Downloading")
    urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
def _pbhook(numblocks, blocksize, filesize, url=None,dp=None):
    try:
        percent = min((numblocks*blocksize*100)/filesize, 100)
        print percent
        dp.update(percent)
    except:
        percent = 100
        dp.update(percent)
    if dp.iscanceled(): 
        print "DOWNLOAD CANCELLED" # need to get this part working
        dp.close()
def UpdateMe(url):
    dialog = xbmcgui.Dialog()
    if dialog.yesno("Update", 'Do you Wish To Install Addon','', "",'Close','Yes'):
        dp = xbmcgui.DialogProgress()
        dp.create('UPDATING')
        print "DOWNLOAD CANCELLED" # need to get this part working
        dp.update(20)
        dialog = xbmcgui.Dialog()
        dp = xbmcgui.DialogProgress()
        dp.create('Downloading Zip')
        dp.update(30)
        url = ("%s"%(url1))
        localfile = os.path.join(addonDir,"addon.xml")
        urllib.urlretrieve(url,localfile)
        url2 = ("%s"%(url))
        dp.update(40)
        localfile = os.path.join(addonDir,"resources/settings.xml")
        urllib.urlretrieve(url,localfile)
        url3 = ("%s"%(url))
        dp.update(50)
        localfile = os.path.join(addonDir,"default.py")
        urllib.urlretrieve(url,localfile)
        url4 = ("%s"%(url))
        dp.update(60)
        localfile = os.path.join(addonDir,"changelog.txt")
        urllib.urlretrieve(url,localfile)
        dp.update(70)
        xbmc.executebuiltin("UpdateLocalAddons")
        xbmc.executebuiltin("UpdateAddonRepos")
        dp.update(100)
        dp.close()
        dialog.ok("All Done", " Update Is Complete")
    else:
        return                

def Refresh():
    dialog = xbmcgui.Dialog()
    if dialog.yesno("Update", 'Do you Wish To update','', "",'Close','Yes'):
        dp = xbmcgui.DialogProgress()
        dp.create('UPDATING')
        dp.update(20)
        dialog = xbmcgui.Dialog()
        dp = xbmcgui.DialogProgress()
        dp.create('Refreshing List')
        dp.update(60)
        url = "%s/default.py"%(BASE)
        localfile = os.path.join(addonDir,"default.py")
        urllib.urlretrieve(url,localfile)
        dp.update(90)
        xbmc.executebuiltin("UpdateLocalAddons")
        xbmc.executebuiltin("UpdateAddonRepos")
        dp.update(100)
        dp.close()
        dialog.ok("All Done", " Update Is Complete")
        xbmc.executebuiltin('Container.Refresh')
    else:
        return
                
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param

def addLink(name,url,iconimage,urlType):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty('IsPlayable','true')
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        return ok


	  
def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
def addDir2(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok
        
              
params=get_params()
url=None
name=None
mode=None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

if mode==None or url==None or len(url)<1:
        print ""
        CATEGORIES()

elif mode==3:
    UpdateMe(url)
elif mode==4:
    Refresh()



xbmcplugin.endOfDirectory(int(sys.argv[1]))
