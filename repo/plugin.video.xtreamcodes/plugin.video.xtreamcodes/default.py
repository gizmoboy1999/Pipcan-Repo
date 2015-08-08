import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,datetime,os
usern=xbmcplugin.getSetting(int(sys.argv[1]), 'usern')
passw=xbmcplugin.getSetting(int(sys.argv[1]), 'passw')
site=xbmcplugin.getSetting(int(sys.argv[1]), 'website')
port=xbmcplugin.getSetting(int(sys.argv[1]), 'port')
type=xbmcplugin.getSetting(int(sys.argv[1]), 'type')
ADDON = xbmcaddon.Addon(id='plugin.video.xtreamcodes')
AddonID = 'plugin.video.xtreamcodes'
Addon = xbmcaddon.Addon(AddonID)
addonDir = Addon.getAddonInfo('path').decode("utf-8")
#Created By Pipcan.
BASE = ""
def CATEGORIES():
        addDir('Refresh Channels List','updates',3,'')
        addLink('Channels','%s/channels.m3u'%(addonDir),'','')
        
                       
def INDEX(url):
	if url=="browse?q=":
	  searchString = addSearch()
	  url="browse?q="+searchString
	after = url
	url = BASE + url
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
	try:
	  appdg = after.split('&')[1]
	  before = after.split('&')[0]
	  appdg = int(appdg.split('=')[1]) + 1
	  newURL = before + "&page=" + str(appdg)
	except:
	  newURL = after + "&page=2"
	  appdg = 2
	addDir("Go To Page " + str(appdg), newURL, 1, "")
        match=re.compile('<a href="(.+?)"><img class="thumbnail_image" src="(.+?)" alt="(.+?)"').findall(link)
        for url,thumbnail,name in match:
	  req = urllib2.Request(url)
	  req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	  response = urllib2.urlopen(req)
	  link=response.read()
	  response.close()
	  match=re.compile('file: "(.+?)",').findall(link)
	  for url in match:
                addLink(name,url,thumbnail,"")
          match=re.compile('src="http://www.youtube.com/embed/(.+?)?rel=0').findall(link)
          for url in match:
	    youtubeurl = 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % url
	    addLink(name,youtubeurl,thumbnail,"")
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
def UpdateMe():
    dialog = xbmcgui.Dialog()
    if dialog.yesno("Update", 'Do you Wish To update Channels','', "",'Close','Yes'):
        dp = xbmcgui.DialogProgress()
        dp.create('UPDATING')
        dp.update(20)
        dialog = xbmcgui.Dialog()
        dp = xbmcgui.DialogProgress()
        dp.create('Downloading Zip')
        dp.update(60)
        url = "%s:%s/get.php?username=%s&password=%s&type=m3u_plus&output=mpegts"%(site,port,usern,passw,)
        localfile = os.path.join(addonDir,"channels.m3u")
        urllib.urlretrieve(url,localfile)
        dp.update(70)
        xbmc.executebuiltin("UpdateLocalAddons")
        xbmc.executebuiltin("UpdateAddonRepos")
        dp.update(100)
        dp.close()
        dialog.ok("All Done", " Update Is Complete")
    else:
        return                
def VIDEOLINKS(url,name):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('file: "(.+?)",').findall(link)
        for url in match:
                addLink(name,url,'',"")
        

                
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


def addSearch():
	searchStr = ''
	keyboard = xbmc.Keyboard(searchStr, 'Search')
	keyboard.doModal()
	if (keyboard.isConfirmed()==False):
	  return
	searchStr=keyboard.getText()
	if len(searchStr) == 0:
	  return
	else:
	  return searchStr
	  
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
       
elif mode==1:
        print ""+url
        INDEX(url)
        
elif mode==2:
        print ""+url
        addSearch()
elif mode==3:
    UpdateMe()



xbmcplugin.endOfDirectory(int(sys.argv[1]))
