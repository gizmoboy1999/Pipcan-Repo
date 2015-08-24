import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,datetime,os
ADDON = xbmcaddon.Addon(id='plugin.video.password')
AddonID = 'plugin.video.firstaddon'
Addon = xbmcaddon.Addon(AddonID)
addonDir = Addon.getAddonInfo('path').decode("utf-8")
#################################################################################################################################
##############################                                ###################################################################
##############################      The First LIST ITEMS      ###################################################################


def CATEGORIES():
        addDir2('NAME','url',4,'icon')
#################################################################################################################################
#################################################################################################################################
#################################################################################################################################

















def OPEN_URL(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent' , "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36")
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
#################################################################################################################################
##############################                                ###################################################################
##############################      Read The Page             ###################################################################



def REGEX(url):
#                        V----- This Meens It Will Read The Url In The Link Item That Was Pressed
        link = OPEN_URL(url)
#                          V---- REGEX  CODE GOES HERE
        match=re.compile('  ').findall(link)
#              V---- For Every (.+?) In You REGEX You Must Give It A Name so if you have 2 and its  name and url put name,url
        for channelid in match:
#                   V -- if you want the name to appper here you could remove to ' ' and just put name or you could put %s in the middle
#                        then after the ' put %(name) so sould look like '%s'%(name)
#                           V ----- this is the mode set it to the def() you wana run see bottom 
            addDir(' ',' ',1,'','')

			
#################################################################################################################################
#################################################################################################################################
#################################################################################################################################

















                
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

















#################################################################################################################################
##############################                                ###################################################################
############################## DEFINING YOUR DEF () FUNCTIONS ###################################################################

if mode==None or url==None or len(url)<1:
        print ""
        CATEGORIES()
#          V ----- GIVE YOU MODE A NUMBER
elif mode==1:
#        V ---- Then The Name Of A def name() you have made
        INDEX(url)
#             ^------- and witch bit you want to keep so you want it to remember the name in addDir so put name    



xbmcplugin.endOfDirectory(int(sys.argv[1]))


#################################################################################################################################
#################################################################################################################################
#################################################################################################################################
