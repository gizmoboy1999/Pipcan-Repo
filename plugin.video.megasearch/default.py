# -*- coding: utf-8 -*-
import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,datetime,base64
username=xbmcplugin.getSetting(int(sys.argv[1]), 'username')
password=xbmcplugin.getSetting(int(sys.argv[1]), 'password')
ADDON = xbmcaddon.Addon(id='plugin.video.megasearch')
AddonID = 'plugin.video.megasearch'
Addon = xbmcaddon.Addon(AddonID)
#LiveLeak.com- by Oneadvent 2012.
BASE='http://letwatch.us/'
# Edit line below
addonDir = Addon.getAddonInfo('path').decode("utf-8")
bingurl = 'http://prod.video.msn.com/tenant/amp/entityid/'
bingimage='http://img-s-msn-com.akamaized.net/tenant/amp/entityid/AAbGK17.img'
def CATEGORIES():
            addDir2('[COLOR yellow]MEGA SEARCH BY PIPCAN[/COLOR]','',1000,'')
            searchStr = ''
            addDir('[COLOR yellow]IPTV [/COLOR]Search PASTEBIN','https://www.googleapis.com/customsearch/v1element?key=AIzaSyCVAXiUzRYsML1Pv6RwSG1gunmMikTzQqY&rsz=filtered_cse&num=20&hl=en&prettyPrint=false&source=gcsc&gss=.com&sig=56f70d816baa48bdfe9284ebc883ad41&cx=013305635491195529773:0ufpuq-fpt0&sort=date&q=',503,'')
            addDir('Search Bing Videos','http://www.msn.com/en-us/video/searchresults?q=',37,'')
            addDir('[COLOR yellow]VIDEO [/COLOR]Search letwatch.us','http://letwatch.us/?op=search&k=',3,'')
            addDir('Search Vodlocker','http://vodlocker.com/?op=search&k=',5,'')
            addDir('[COLOR yellow]VIDEO [/COLOR]Search cloudy.ec','http://www.cloudy.ec/search?search=',6,'http://thumbs.cloudy.ec//thumbs/62b3a545e36115ff7a45f452073cecb1-%s.jpg'%(password))
            addDir('[COLOR yellow]VIDEO [/COLOR]Dedibox','http://sd-41445.dedibox.fr/',8,'ww')
            addDir('[COLOR yellow]IPTV [/COLOR]http://80.80.160.168/live/','http://80.80.160.168/live',8,'ww')
            addDir('[COLOR yellow]VIDEO [/COLOR]Filmgozar','http://dl.filmgozar.com/',8,'ww')
            addDir('[COLOR yellow]VIDEO [/COLOR]LOADS OF FILMS','http://46.105.122.150/',8,'ww')
            addDir('[COLOR yellow]VIDEO [/COLOR]Moviefarsi','http://dl5.moviefarsi.org/',8,'ww')
            addDir('[COLOR yellow]VIDEO [/COLOR]Free Upload .IR ','http://dl8.freeupload.ir/',8,'ww')
            addDir('[COLOR yellow]VIDEO [/COLOR]NFilm','http://dl.nfilm.org/DL/',8,'ww')
            addDir('[COLOR yellow]VIDEO [/COLOR]Canflix','http://cdn.alpha.canflix.net',8,'ww')
            addDir('[COLOR yellow]VIDEO [/COLOR]Tehmovies','http://dl.tehmovies.com/',8,'ww')
            addDir('[COLOR yellow]VIDEO [/COLOR]Yukinoshita','http://yukinoshita.eu/ddl/',12,'ww')
            addDir('[COLOR yellow]VIDEO [/COLOR]Seed Cows','http://seed.cows.io/',8,'ww')
            addDir('[COLOR yellow]VIDEO [/COLOR]Hastidownload','http://dl.hastidownload.net/ali/film/',8,'ww')
            addDir('[COLOR yellow]VIDEO [/COLOR]Animakai.tv','http://www.animakai.tv/animes/1/',13,'ww')
            addDir('[COLOR yellow]VIDEO [/COLOR]Kino Kong','http://kinokong.net',18,'ww')
            addDir('[COLOR yellow]IPTV [/COLOR]TV Online Streams','http://tvonlinestreams.com',100,'ww')
            addDir('[COLOR yellow]IPTV [/COLOR]IPTV Filmover','http://iptv.filmover.com',200,'ww')
            addDir('[COLOR yellow]IPTV [/COLOR]FreeTux TV','http://database.freetuxtv.net',300,'ww')
            addDir('[COLOR yellow]IPTV [/COLOR]I-PTV BLOGSPOT','http://i-ptv.blogspot.co.uk',401,'')
            addDir('[COLOR yellow]IPTV [/COLOR]I-PTV BLOGSPOT RUSSIA','http://i-ptv.blogspot.co.uk/p/russia-big.html',401,'')
            addDir('[COLOR yellow]IPTV [/COLOR]Pastebin m3u','https://www.googleapis.com/customsearch/v1element?key=AIzaSyCVAXiUzRYsML1Pv6RwSG1gunmMikTzQqY&rsz=filtered_cse&num=20&hl=en&prettyPrint=false&source=gcsc&gss=.com&sig=56f70d816baa48bdfe9284ebc883ad41&cx=013305635491195529773:0ufpuq-fpt0&q=m3u&sort=date',501,'http://pastebin.com/i/fb2.jpg')
            addDir('[COLOR yellow]IPTV [/COLOR]Pastebin M3U8','https://www.googleapis.com/customsearch/v1element?key=AIzaSyCVAXiUzRYsML1Pv6RwSG1gunmMikTzQqY&rsz=filtered_cse&num=20&hl=en&prettyPrint=false&source=gcsc&gss=.com&sig=56f70d816baa48bdfe9284ebc883ad41&cx=013305635491195529773:0ufpuq-fpt0&q=m3u8&sort=date',501,'http://pastebin.com/i/fb2.jpg')
            addDir('[COLOR yellow]IPTV [/COLOR]TV Degunino','http://tv.degunino.net/m3u/',8,'')
            addDir('[COLOR yellow]IPTV [/COLOR]tunisia-dreambox','http://www.tunisia-dreambox.info/e2-addons-manager/Tunisiasat-plugins/softupdates/TSmedia/',8,'')
            addDir('[COLOR yellow]IPTV [/COLOR]iptvm3u','http://www.iptvm3u.com/search?updated-max=2016-03-03T15%3A14%3A00-08%3A00&max-results=7000',600,'')
            addDir('[COLOR yellow]IPTV [/COLOR]VLC','http://www.vlchistory.eu.pn',701,'')
            addDir('[COLOR yellow]IPTV [/COLOR]langamepp','http://langamepp.com/playlist/pipcan/Snooker85',504,'')
            addDir('[COLOR yellow]IPTV [/COLOR]http://www.iptvlinks.com/','http://www.iptvlinks.com/feeds/posts/summary?alt=json-in-script&callback=pageNavi&max-results=200',2000,'')
            addDir('[COLOR yellow]MUSIC [/COLOR]ARTISTS','http://e-mp3bul.com/albumler/2/yabanci-mp3-indir.html',5000,'')
            addDir('[COLOR yellow]MUSIC [/COLOR]ALBUMS','http://e-mp3bul.com/album/142/2015.html',5000,'')

def UPDATE():
    if ADDON.getSetting(id='password') == '4':
        ADDON.setSetting(id='password', value='0')
        xbmc.executebuiltin('Container.Refresh')
        return
    elif ADDON.getSetting(id='password') == '0':
        ADDON.setSetting(id='password', value='1')
        xbmc.executebuiltin('Container.Refresh')
        return
    elif ADDON.getSetting(id='password') == '1':
        ADDON.setSetting(id='password', value='2')
        xbmc.executebuiltin('Container.Refresh')
        return
    elif ADDON.getSetting(id='password') == '2':
        ADDON.setSetting(id='password', value='3')
        xbmc.executebuiltin('Container.Refresh')
        return
    elif ADDON.getSetting(id='password') == '3':
        ADDON.setSetting(id='password', value='4')
        xbmc.executebuiltin('Container.Refresh')
        return
def addSearch(searchStr):
	searchStr = searchStr
	keyboard = xbmc.Keyboard(searchStr, 'Search')
	keyboard.doModal()
	if (keyboard.isConfirmed()==False):
	  return
	searchStr=keyboard.getText()
	if len(searchStr) == 0:
	  return
	else:
	  return searchStr
def openSettings():
    ADDON.openSettings()
def OPEN_URL(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent' , "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36")
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link
def MEDIAITEMS(url):
        searchStr = ''
        keyboard = xbmc.Keyboard(searchStr, 'Search')
        keyboard.doModal()
        searchStr=keyboard.getText()
        link = OPEN_URL('%s%s'%(url,searchStr))
        match=re.compile('<a href="http://letwatch.us/(.+?)" class="video_img_link processing_bg">.+?\n.+?<img src="(.+?)" height="121" alt="(.+?)"').findall(link)
        for url,image,name in match:
            addDir2('%s'%(name),'http://letwatch.us/embed-%s-640x400.html'%(url),4,'%s'%(image))
def VOD(url):
        searchStr = ''
        keyboard = xbmc.Keyboard(searchStr, 'Search')
        keyboard.doModal()
        searchStr=keyboard.getText()
        link = OPEN_URL('%s%s'%(url,searchStr))
        match=re.compile('background-image:url\((.+?)\);"><span>(.+?)</span></a></TD>.+?\n.+?<TD valign=top>.+?\n.+?<div class="link"><a href="(.+?)">(.+?)</a></div>').findall(link)
        for image,time,url,name in match:
            addDir2('%s - %s'%(name,time),url,4,'%s'%(image))
def canflix(url):
        link = OPEN_URL(url)
        match=re.compile('<td data-sort-value="(.+?)"><i class="fa fa-(.+?) fa-fw"></i>&nbsp;<a href="(.+?)">.+?\n.+?value=".+?">(.+?)<').findall(link)
        for name,type,url,size in match:
            addDir2('%s - %s'%(name,size),'%s'%url,4,'%s'%(type))
def freetuxtv(url):
        link = OPEN_URL(url)
        match=re.compile('src="(.+?)" alt="" /> <i>(.+?)</i>.+<a href="(.+?)">(.+?)<').findall(link)
        for flag,name,url,count in match:
            addDir('%s - %s'%(name,count),'http://database.freetuxtv.net%s'%url,301,'http://database.freetuxtv.net%s'%(flag))
def MP3(url):
        link = OPEN_URL(url)
        match=re.compile('<img src="(.+?)"/>(.+?)</a></li> <li><a href="(.+?)"').findall(link)
        match2=re.compile('id="player2" src="(.+?)"').findall(link)
        match3=re.compile('<li><a href="(.+?)" data-ajax="false" title="(.+?)">').findall(link)
        for image,name,url in match:
            addDir('%s'%(name.replace('<span class="ui-li-count">',' [COLOR yellow]').replace('</span>','[/COLOR]')),'%s'%url,5000,'%s'%(image))
        for url in match2:
            addDir2('PLAY','%s'%url,9,'')
            addDir2('DOWNLOAD','%s'%url,9,'')
            addDir2('ADD TO PLAYLIST','%s'%url,9,'')
        for url,name in match3:
            addDir(name,'%s'%url,5000,'')
def VLC(url):
        link = OPEN_URL(url)
        match=re.compile('<h5><span style=" color:#06C">(.+?)</span>').findall(link)
        match2=re.compile('<a href="http://www.vlchistory.eu.pn/index.php/vlchistory/show/\d\d\d\d/\d\d/(.+?)">').findall(link)
        for url in match:
            addDir2('%s'%(url),'%s'%url,9,'')
        for url in match2:
            addDir('%s'%(url),'http://www.vlchistory.eu.pn/index.php/vlchistory/show/2015/08/%s'%url,701,'')
def iptvm3u(url):
        link = OPEN_URL(url)
        match=re.compile('#EXTINF:.+?,(.+?)<.+?\n.+?">(.+?)<').findall(link)
        for name,url in match:
            addDir2('%s'%(name),'%s'%url,9,'')
def iptvm3u2(url):
        link = OPEN_URL(url)
        match=re.compile("<h2 class='post-title entry-title' itemprop='name'>\n<a href='(.+?)'>(.+?)</a>").findall(link)
        for url,name in match:
            addDir('%s'%(name),'%s'%url,601,'')
        addDir('page 2','http://www.iptvm3u.com/search?updated-max=2015-08-28T13%3A30%3A00-07%3A00&max-results=70',600,'')
def freetuxtv2(url):
        link = OPEN_URL(url)
        match=re.compile('<td>(.+?)<br />=&gt; <a href="(.+?)">').findall(link)
        match2=re.compile('<li class="next"><a href=".+?Language%5D=(.+?)&.+?WebStream_page=(.+?)">').findall(link)
        for name,url in match:
            addDir2('%s'%(name),'%s'%url,9,'')
        for lang,url in match2:
            addDir('NEXT','http://database.freetuxtv.net/webStream/index?WebStreamSearchForm[Type]=1&WebStreamSearchForm[Language]=%s&WebStreamSearchForm[Status]=2&WebStream_page=%s'%(lang,url),301,'')
        urllib2.quote(url.encode("utf8"))
def BLOGSPOT(url):
        link = OPEN_URL(url)
        match=re.compile('#EXTINF:.+?,(.+?)\n(.+?)\n').findall(link)
        match2=re.compile('<a href="https://sites.google.com/site/iptvblogspot/config/pagetemplates/m3u/(.+?)"> Download (.+?)</a>').findall(link)
        for url,name in match2:
            addDir('[COLOR yellow]%s[/COLOR]'%name,'https://sites.google.com/site/iptvblogspot/config/pagetemplates/m3u/%s'%url,401,'')
        for name,url in match:
            addDir2(name,url,9,'')
def IPTVLINKS(url):
        link = OPEN_URL(url)
        match=re.compile('{"rel":"alternate","type":"text/html","href":"(.+?)","title":"(.+?)"}].+?".+?"url":"(.+?)"').findall(link)
        for url,name,image in match:
            addDir(name,'%s'%(url.replace('\/', '/')),2001,image.replace('\/','/'))
def IPTVLINKS2(url):
        id = 0
        link = OPEN_URL(url)
        match2=re.compile('#EXTINF:.+?,(.+?)<br />(.+?)<').findall(link)
        match3=re.compile('>(.+?)</b><br />\n(.+?)<').findall(link)
        for name,url in match2:
            addDir2(name,'%s'%(url),9,'')
        for name,url in match3:
            id = id + 1
            if id == '1':
                addDir2('%s) - %s'%(id,name.replace('<span style="color: red;">','').replace('</span>','')),'%s'%(url),9,'')
            else:
                addDir2('%s) - %s'%(id,name.replace('<span style="color: red;">','').replace('</span>','')),'%s'%(url),9,'')

def kinokong(url):
        link = OPEN_URL(url)
        match=re.compile('<a href="/films/(.+?)/">.+?<b>(.+?)</b>').findall(link)
        match2=re.compile('<a href="/serial/(.+?)/">.+?<b>(.+?)</b>').findall(link)
        match3=re.compile('<a href="/anime/(.+?)/">.+?<b>(.+?)</b>').findall(link)
        addDir('[COLOR yellow][B]-------------- FILMS --------------[/B][/COLOR]','',19,'')
        for name,count in match:
            addDir('%s [COLOR red]%s[/COLOR]'%(name,count),'%s/films/%s/'%(url,name),19,'%s'%(count))
        addDir('[COLOR yellow][B]-------------- SERIALS --------------[/B][/COLOR]','',19,'')
        for name,count in match2:
            addDir('%s [COLOR red]%s[/COLOR]'%(name,count),'%s/serial/%s/'%(url,name),19,'%s'%(count))
        addDir('[COLOR yellow][B]-------------- ANIME --------------[/B][/COLOR]','',19,'')
        for name,count in match3:
            addDir('%s [COLOR red]%s[/COLOR]'%(name,count),'%s/anime/%s/'%(url,name),19,'%s'%(count))
def kinokong2(url):
        link = OPEN_URL(url)
        match=re.compile('<a href="(.+?)" class="main-sliders-play"><svg viewBox=".+?"><polygon points=".+?"></polygon></svg></a>\n.+</span>\n.+<img src="(.+?)" alt="(.+?)"').findall(link)
        for url,image,name in match:
            addDir(name,'%s'%url,20,image)
def kinokong3(url):
        link = OPEN_URL(url)
        match=re.compile('file:"(.+?)",').findall(link)
        match2=re.compile('file:".+?,(.+?)"').findall(link)
        match3=re.compile('file:"(.+?)"').findall(link)
        for url in match:
            addDir2('%s'%(url),'%s'%url,9,'')
        for url in match2:
            addDir2('%s'%(url),'%s'%url,9,'')
        for url in match3:
            addDir2('%s'%(url),'%s'%url,9,'')
def animakai(url):
        link = OPEN_URL(url)
        match=re.compile('<div class="sl_image"><a href="(.+?)" alt="(.+?)" title=".+?"><img src="(.+?)"').findall(link)
        match2=re.compile('</a></div><div class="pgTitle"><a href="http://www.animakai.tv/animes/(.+?)/"').findall(link)
        for url,name,image in match:
            addDir('%s'%(name),'%s'%url,14,'%s'%(image))
        for name in match2:
            addDir('Go To Page %s'%(name),'http://www.animakai.tv/animes/%s/'%name,13,'')
def animakai2(url):
        link = OPEN_URL(url)
        match=re.compile('<span>.+?</span></div><a href="(.+?)"  alt="(.+?)" title=".+?" ><img src="(.+?)"').findall(link)
        for url,name,image in match:
            addDir('%s - '%(name),url,15,image)
def PASTEBIN3(url):
        searchStr = ''
        keyboard = xbmc.Keyboard(searchStr, 'Search')
        keyboard.doModal()
        searchStr=keyboard.getText()
        link = OPEN_URL('%s%s'%(url,searchStr.replace(' ','%20')))
        match=re.compile('titleNoFormatting":"(.+?)","unescapedUrl":"(.+?)"').findall(link)
        for name,url in match:
            addDir('%s'%(name),url.replace('pastebin.com/','pastebin.com/raw.php?i='),502,'')
def PASTEBIN(url):
        addDir('[COLOR yellow]SEARCH[/COLOR]','https://www.googleapis.com/customsearch/v1element?key=AIzaSyCVAXiUzRYsML1Pv6RwSG1gunmMikTzQqY&rsz=filtered_cse&num=20&hl=en&prettyPrint=false&source=gcsc&gss=.com&sig=56f70d816baa48bdfe9284ebc883ad41&cx=013305635491195529773:0ufpuq-fpt0&sort=date&q=',503,'')
        link = OPEN_URL(url)
        match=re.compile('titleNoFormatting":"(.+?)","unescapedUrl":"(.+?)"').findall(link)
        for name,url in match:
            addDir('%s'%(name),url.replace('pastebin.com/','pastebin.com/raw.php?i='),502,'')
def PASTEBIN2(url):
        link = OPEN_URL(url)
        match2=re.compile('#EXTINF:.+?[,?|\s?](.+?)\n(.+?)\n').findall(link)
        match1=re.compile('#EXTINF:.+?[,?|\s?|\.?](.+?)\n(.+?)\B[ ?|\s?]').findall(link)
        for name,url in match2:
            addDir2(name,url,9,'')
        for name,url in match1:
            addDir2(name,url,9,'')
def LANG(url):
        link = OPEN_URL(url)
        match2=re.compile('#EXTINF:0 audio-track="ru" group-title=".+?",(.+?)\n(.+?)\n').findall(link)
        for name,url in match2:
            addDir2(name,url,9,'')

def tvonlinestreams(url):
        addDir('SEARCH','http://www.tvonlinestreams.com/?s=',102,'')
        link = OPEN_URL(url)
        match=re.compile('<h2 class="entry-title"><a href="(.+?)" title=".+?" rel="bookmark">(.+?)</a></h2>').findall(link)
        match2=re.compile('href="(.+?)" class="page" title="(.+?)">').findall(link)
        for url,name in match:
            addDir(name,url,101,'')
        for url,name in match2:
            addDir('GO TO PAGE %s '%name,url,100,'')
def tvonlinestreams2(url):
        link = OPEN_URL(url)
        match=re.compile('#EXTINF:.+?,(.+?)<br />\n(.+?)<br />').findall(link)
        for name,url in match:
            addDir2('%s'%(name.replace(':','[COLOR yellow] - [/COLOR]')),url.replace(' ',''),9,'')
def filmover(url):
        addDir('SEARCH','http://iptv.filmover.com/?s=',203,'')
        link = OPEN_URL(url)
        match=re.compile('<h2 class="post-title entry-title"><a href="(.+?)" rel="bookmark">(.+?)</a></h2>').findall(link)
        match2=re.compile('<a class="next page-numbers" href="http://iptv.filmover.com/page/(.+?)/">').findall(link)
        for url,name in match:
            addDir('%s'%(name.replace(':','[COLOR yellow] - [/COLOR]')),url.replace(' ',''),201,'')
        for name in match2:
            addDir('[COLOR yellow]GO TO PAGE[/COLOR] %s'%(name),'http://iptv.filmover.com/page/%s'%(name),200,'')
def filmover2(url):
        link = OPEN_URL(url)
        match=re.compile('#EXTINF:.+?,(.+?)<br />\n(.+?)<').findall(link)
        match3=re.compile('<br />#EXTINF:.+?,(.+?)<br />(.+?)<br />').findall(link)
        for name,url in match:
            addDir2('%s'%(name.replace(':','[COLOR yellow] - [/COLOR]')),url.replace(' ',''),9,'')
        for name,url in match3:
            addDir2('%s'%(name.replace(':','[COLOR yellow] - [/COLOR]')),url.replace(' ',''),9,'')
def tvonlinestreams3(url):
        searchStr = ''
        keyboard = xbmc.Keyboard(searchStr, 'Search')
        keyboard.doModal()
        searchStr=keyboard.getText()
        link = OPEN_URL('%s%s'%(url,searchStr))
        match=re.compile('<h2 class="entry-title"><a href="(.+?)" title=".+?" rel="bookmark">(.+?)</a></h2>').findall(link)
        match2=re.compile('href="(.+?)" class="page" title="(.+?)">').findall(link)
        for url,name in match:
            addDir(name,url,101,'')
        for url,name in match2:
            addDir('GO TO PAGE %s '%name,url,100,'')
def filmover3(url):
        searchStr = ''
        keyboard = xbmc.Keyboard(searchStr, 'Search')
        keyboard.doModal()
        searchStr=keyboard.getText()
        link = OPEN_URL('%s%s'%(url,searchStr))
        match=re.compile('<h2 class="post-title entry-title"><a href="(.+?)" rel="bookmark">(.+?)</a></h2>').findall(link)
        match2=re.compile('<a class="next page-numbers" href="http://iptv.filmover.com/page/(.+?)/">').findall(link)
        for url,name in match:
            addDir('%s'%(name.replace(':','[COLOR yellow] - [/COLOR]')),url.replace(' ',''),201,'')
        for name in match2:
            addDir('[COLOR yellow]GO TO PAGE[/COLOR] %s'%(name),'http://iptv.filmover.com/page/%s'%(name),200,'')
def animakai3(url):
        link = OPEN_URL(url)
        match2=re.compile('<video src="(.+?)"').findall(link)
        match1=re.compile('"http://player.mais.uol.com.br/embed_v2.swf\?tv=2&mediaId=(.+?)"').findall(link)
        for url in match2:
            addDir2('PlaY Google Video','%s'%(url),9,'')
        for url in match1:
            addDir2('PlaY Google Video','http://videohd1.mais.uol.com.br/%s.mp4?r=http://www.animakai.tv/episodio/'%(url),9,'')
def canflix(url):
        link = OPEN_URL(url)
        match=re.compile('<td data-sort-value="(.+?)"><i class="fa fa-(.+?) fa-fw"></i>&nbsp;<a href="(.+?)">.+?\n.+?value=".+?">(.+?)<').findall(link)
        for name,type,url2,size in match:
            if type == 'folder':
                addDir('[COLOR yellow][FOLDER][/COLOR] %s - %s'%(name,size),'%s%s'%(url,url2),12,'%s'%(type))
            else:
                addDir2('%s - %s'%(name,size),'%s%s'%(url,url2),9,'%s'%(type))
def BING(url):
        searchStr = ''
        keyboard = xbmc.Keyboard(searchStr, 'Search')
        keyboard.doModal()
        searchStr=keyboard.getText()
        link = OPEN_URL('%s%s'%(url,searchStr))
        match=re.compile('<a href="/en-us/video/watch/.+?/vi-(.+?)"  >\n <div class="imgcontainer">\n.+?<img alt="(.+?)".+?entityid/(.+?).img').findall(link)
        match2=re.compile('<a class="nexturl" href="(.+?)">(.+?)</a>').findall(link)
        for id,name,id2 in match:
            addDir2('%s'%name,'http://prod.video.msn.com/tenant/amp/entityid/%s?blobrefkey=103&$blob=1'%(id),9,'http://img-s-msn-com.akamaized.net/tenant/amp/entityid/%s.png'%id2)
        for url,name in match2:
            addDir('%s'%name,url,1000,'')
def BING2(url):
        link = OPEN_URL('%s'%(url))
        match=re.compile('<a href="/en-us/video/watch/.+?/vi-(.+?)"  >\n <div class="imgcontainer">\n.+?<img alt="(.+?)".+?entityid/(.+?).img').findall(link)
        match2=re.compile('<a class="nexturl" href="(.+?)">(.+?)</a>').findall(link)
        for id,name,id2 in match:
            addDir2('%s'%name,'http://prod.video.msn.com/tenant/amp/entityid/%s?blobrefkey=103&$blob=1'%(id),9,'http://img-s-msn-com.akamaized.net/tenant/amp/entityid/%s.png'%id2)
        for url,name in match2:
            addDir('%s'%name,url,1000,'')

def FTP(url):
        link = OPEN_URL(url)
        match=re.compile('<tr><td valign="top"><img src="/icons/.+?.gif" alt="\[(.+?)\]"></td><td><a href="(.+?)">(.+?)</a></td><td align="right">.+?</td><td align="right">(.+?)<').findall(link)
        match2=re.compile('<li><a href="(.+?)\/">(.+?)</a></li>').findall(link)
        match3=re.compile('<li><a href="(.+?)mkv">(.+?)</a></li>').findall(link)
        match4=re.compile('<li><a href="(.+?)mp4">(.+?)</a></li>').findall(link)
        match5=re.compile('<li><a href="(.+?)avi">(.+?)</a></li>').findall(link)
        match6=re.compile('<li><a href="(.+?)\/">(.+?)</a></li>').findall(link)
        match7=re.compile('<a href="(.+?)">(.+?)&gt;</a>').findall(link)
        match8=re.compile('<a href="(.+?)mp4">(.+?)</a>').findall(link)
        match9=re.compile('<a href="(.+?)mkv">(.+?)</a>').findall(link)
        match10=re.compile('<a href="(.+?)\/">(.+?)</A>').findall(link)
        match11=re.compile('<a href="(.+?)mkv">(.+?)</A>').findall(link)
        match12=re.compile('<a href="(.+?)avi">(.+?)</A>').findall(link)
        match13=re.compile('<a href="(.+?)mp4">(.+?)</A>').findall(link)
        match14=re.compile('<a href="(.+?)">(.+?)</a>                                      ').findall(link)
        match15=re.compile('#EXTINF:.+?,(.+?)\n(.+?)\n').findall(link)
        match16=re.compile('<name>(.+?)</name>|<stream_url><!\[CDATA\[(.+?)\]\]></stream_url>').findall(link)
        match17=re.compile('<li><a href="(.+?)/"> (.+?)/</a>').findall(link)
        match18=re.compile('<li><a href="(.+?).xml"> (.+?).xml</a></li>').findall(link)
        match19=re.compile('<li><a href="(.+?).m3u"> (.+?).m3u</a></li>').findall(link)
        match20=re.compile('<a href="(.+?)">(.+?)</a>').findall(link)
        for type,url2,name,size in match:
            if type == 'VID':
                addDir2('%s - [B]%s[/B]'%(name.replace('.',' ').replace('/',' '),size.replace('-','')),'%s%s'%(url,url2),9,'http://static.squarespace.com/static/5130016be4b0c701bd01cea9/t/52bd22a5e4b097881153159e/1388126886945/film-Icon.png')
            else:
                addDir('[COLOR yellow][FOLDER][/COLOR] %s - %s'%(name.replace('.',' ').replace('/',' '),size),'%s%s'%(url,url2),8,'http://pngimg.com/upload/folder_PNG8772.png')
        for url2,name in match2:
                addDir('%s - [B][/B]'%(name),'%s%s/'%(url,url2),8,'http://pngimg.com/upload/folder_PNG8772.png')
        for url2,name in match3:
                addDir2('[B]%s [/B]'%(name),'%s%smkv'%(url,url2),9,'http://static.squarespace.com/static/5130016be4b0c701bd01cea9/t/52bd22a5e4b097881153159e/1388126886945/film-Icon.png')
        for url2,name in match4:
                addDir2('[B]%s [/B]'%(name),'%s%smp4'%(url,url2),9,'http://static.squarespace.com/static/5130016be4b0c701bd01cea9/t/52bd22a5e4b097881153159e/1388126886945/film-Icon.png')
        for url2,name in match5:
                addDir2('[B]%s [/B]'%(name),'%s%savi'%(url,url2),9,'http://static.squarespace.com/static/5130016be4b0c701bd01cea9/t/52bd22a5e4b097881153159e/1388126886945/film-Icon.png')
        for url2,name in match6:
                addDir('[B]%s [/B]'%(name),'%s%s/'%(url,url2),8,'http://pngimg.com/upload/folder_PNG8772.png')
        for url2,name in match7:
                addDir2('[B]%s [/B]'%(name),'%s/%s'%(url,url2),9,'http://static.squarespace.com/static/5130016be4b0c701bd01cea9/t/52bd22a5e4b097881153159e/1388126886945/film-Icon.png')
        for url2,name in match8:
                addDir2('[B]%s [/B]'%(name),'%s/%smp4'%(url,url2),9,'http://static.squarespace.com/static/5130016be4b0c701bd01cea9/t/52bd22a5e4b097881153159e/1388126886945/film-Icon.png')
        for url2,name in match9:
                addDir2('[B]%s [/B]'%(name),'%s%smvk'%(url,url2),9,'http://static.squarespace.com/static/5130016be4b0c701bd01cea9/t/52bd22a5e4b097881153159e/1388126886945/film-Icon.png')
        for url2,name in match10:
                addDir('[B]%s [/B]'%(name),'http://dl.nfilm.org%s'%(url2),8,'http://static.squarespace.com/static/5130016be4b0c701bd01cea9/t/52bd22a5e4b097881153159e/1388126886945/film-Icon.png')
        for url2,name in match11:
                addDir2('[B]%s [/B]'%(name),'http://dl.nfilm.org%smkv'%(url2),9,'http://static.squarespace.com/static/5130016be4b0c701bd01cea9/t/52bd22a5e4b097881153159e/1388126886945/film-Icon.png')
        for url2,name in match12:
                addDir2('[B]%s [/B]'%(name),'http://dl.nfilm.org%savi'%(url2),9,'http://static.squarespace.com/static/5130016be4b0c701bd01cea9/t/52bd22a5e4b097881153159e/1388126886945/film-Icon.png')
        for url2,name in match13:
                addDir2('[B]%s [/B]'%(name),'http://dl.nfilm.org%smp4'%(url2),9,'http://static.squarespace.com/static/5130016be4b0c701bd01cea9/t/52bd22a5e4b097881153159e/1388126886945/film-Icon.png')
        for url2,name in match14:
                addDir('[B]%s [/B]'%(name),'%s/%s/'%(url,url2),8,'http://static.squarespace.com/static/5130016be4b0c701bd01cea9/t/52bd22a5e4b097881153159e/1388126886945/film-Icon.png')
        for name,url2 in match15:
                addDir2('[B]%s [/B]'%(name),'%s'%(url2),9,'')
        for name,url2 in match16:
                addDir2('[B]%s [/B][I]PLAY[/I]'%(name),'%s'%(url2),9,'')
        for name,url2 in match17:
                addDir('[B]%s [/B]'%(name),'%s%s'%(url,url2),8,'')
        for name,url2 in match18:
                addDir('[B]%s [/B]'%(name),'%s%s.xml'%(url,url2),8,'')
        for name,url2 in match19:
                addDir('[B]%s [/B]'%(name),'%s%s.m3u'%(url,url2),8,'')
        for name,url2 in match20:
                addDir2('[B]%s [/B]'%(name),'%s/%s'%(url,url2),9,'')

def CLOUD(url):
        searchStr = ''
        keyboard = xbmc.Keyboard(searchStr, 'Search')
        keyboard.doModal()
        searchStr=keyboard.getText()
        link = OPEN_URL('%s%s'%(url,searchStr))
        match=re.compile('<a title="(.+?)" href="(.+?)"').findall(link)
        for name,url in match:
            addDir2('%s'%(name),'https://www.cloudy.ec/embed.php?id=%s'%(url.replace('/v/','')),4,'http://thumbs.cloudy.ec//thumbs/62b3a545e36115ff7a45f452073cecb1-%s.jpg'%(password))
def PLAYVIDEO(url,name):
    import urlresolver
    from urlresolver import common
    dp = xbmcgui.DialogProgress()
    dp.create('Featching Your Video','Opening %s Ready'%(name))
    play=xbmc.Player(GetPlayerCore())
    url=urlresolver.HostedMediaFile(url).resolve() 
    play.play(url)
def PLAYVIDEO2(url,name):
    dp = xbmcgui.DialogProgress()
    dp.create('Featching Your Video','Opening %s Ready'%(name))
    play=xbmc.Player(GetPlayerCore())
    play.play(url)


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
        percent = 100
        dp.update(percent)
        print "DOWNLOAD CANCELLED" # need to get this part working
        dp.close()
        dp.close()	
def GetPlayerCore(): 
    try: 
        PlayerMethod=getSet("core-player") 
        if   (PlayerMethod=='DVDPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_DVDPLAYER 
        elif (PlayerMethod=='MPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_MPLAYER 
        elif (PlayerMethod=='PAPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_PAPLAYER 
        else: PlayerMeth=xbmc.PLAYER_CORE_AUTO 
    except: PlayerMeth=xbmc.PLAYER_CORE_AUTO 
    return PlayerMeth 
    return True 

                
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
        MEDIAITEMS(url)
elif mode==4:
        PLAYVIDEO(url,name)
elif mode==5:
        VOD(url)
elif mode==6:
        CLOUD(url)
elif mode==7:
        UPDATE()
elif mode==8:
        FTP(url)
elif mode==9:
        PLAYVIDEO2(url,name)
elif mode==12:
        canflix(url)


elif mode==13:
        animakai(url)
elif mode==14:
        animakai2(url)
elif mode==15:
        animakai3(url)
elif mode==18:
        kinokong(url)
elif mode==19:
        kinokong2(url)

elif mode==20:
        kinokong3(url)
elif mode==37:
        BING(url)
elif mode==100:
        tvonlinestreams(url)
elif mode==101:
        tvonlinestreams2(url)
elif mode==102:
        tvonlinestreams3(url)
elif mode==200:
        filmover(url)

elif mode==201:
        filmover2(url)
elif mode==203:
        filmover3(url)
elif mode==300:
        freetuxtv(url)

elif mode==301:
        freetuxtv2(url)
elif mode==401:
        BLOGSPOT(url)
elif mode==501:
        PASTEBIN(url)
elif mode==502:
        PASTEBIN2(url)

elif mode==503:
        PASTEBIN3(url)
elif mode==504:
        LANG(url)
elif mode==600:
        iptvm3u2(url)
elif mode==601:
        iptvm3u(url)
elif mode==701:
        VLC(url)
elif mode==1000:
        BING2(url)
elif mode==2000:
        IPTVLINKS(url)

elif mode==2001:
        IPTVLINKS2(url)
elif mode==5000:
        MP3(url)




xbmcplugin.endOfDirectory(int(sys.argv[1]))
