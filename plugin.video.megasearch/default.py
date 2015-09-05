# -*- coding: utf-8 -*-
import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,datetime,base64
username=xbmcplugin.getSetting(int(sys.argv[1]), 'username')
password=xbmcplugin.getSetting(int(sys.argv[1]), 'password')
ADDON = xbmcaddon.Addon(id='plugin.video.megasearch')
AddonID = 'plugin.video.megasearch'
Addon = xbmcaddon.Addon(AddonID)
BASE='http://letwatch.us/'
# Edit line below
addonDir = Addon.getAddonInfo('path').decode("utf-8")
bingurl = 'http://prod.video.msn.com/tenant/amp/entityid/'
bingimage='http://img-s-msn-com.akamaized.net/tenant/amp/entityid/AAbGK17.img'
def CATEGORIES():
            addDir('[B]SELECT A CATAGORY[/B]','m',8800,'')
            addDir('[COLOR gold]MY MOVIE LIST[/COLOR]','file:///%s\movies.m3u'%addonDir,555,'')
            addDir('[COLOR gold]MY FRENCH TV LIST[/COLOR]','file:///%s\TV2.m3u'%addonDir,555,'')
            addDir('[COLOR gold]MY TV LIST[/COLOR]','file:///%s\TV.m3u'%addonDir,555,'')
            addDir('[COLOR gold]MOVIES[/COLOR]','m',8801,'')
            addDir('[COLOR gold]VIDEOS[/COLOR]','m',8802,'https://www.ucmo.edu/technology/grants/images/VideoLogo.jpg')
            addDir('[COLOR gold]DOCUMENTRYS[/COLOR]','m',8803,'http://www.4rfv.co.uk/logo/37290lo.jpg')
            addDir('[COLOR gold]ANIME & CARTOONS[/COLOR]','m',8804,'http://www.polyvore.com/cgi/img-thing?.out=jpg&size=l&tid=40579470')
            addDir('[COLOR gold]IPTV[/COLOR]','m',8805,'http://androidtivibox.net/sanpham/30-08-2015/files/unnamed.png')
            addDir('[COLOR gold]MUSIC[/COLOR]','m',8806,'http://img2-1.timeinc.net/ew/i/2011/10/20/Napster-Logo_400.jpg')
            add_item('11','TITLE','PLOT','URL','55','PLOT','77')
def CATMOVIES():
            addDir2('[COLOR yellow]MEGA SEARCH BY PIPCAN[/COLOR]','',1000,'')
            searchStr = ''
            addDir('Search letwatch.us','http://letwatch.us/?op=search&k=',3,'http://letwatch.us/images/logo.png')
            addDir('Search Vodlocker','http://vodlocker.com/?op=search&k=',5,'http://vodlocker.com/images/logo.png')
            addDir('Search cloudy.ec','http://www.cloudy.ec/search?search=',6,'http://www.cloudy.ec/img/logo.png')
            addDir('Dedibox','http://sd-41445.dedibox.fr/',8,'ww')
            addDir('Filmgozar','http://dl.filmgozar.com/',8,'ww')
            addDir('LOADS OF FILMS','http://46.105.122.150/',8,'ww')
            addDir('Moviefarsi','http://dl5.moviefarsi.org/',8,'ww')
            addDir('Free Upload .IR ','http://dl8.freeupload.ir/',8,'ww')
            addDir('NFilm','http://dl.nfilm.org/DL/',8,'ww')
            addDir('Canflix','http://cdn.alpha.canflix.net',8,'ww')
            addDir('Tehmovies','http://dl.tehmovies.com/',8,'ww')
            addDir('Yukinoshita','http://yukinoshita.eu/ddl/',12,'ww')
            addDir('Seed Cows','http://seed.cows.io/',8,'ww')
            addDir('Hastidownload','http://dl.hastidownload.net/ali/film/',8,'ww')
            addDir('Kino Kong','http://kinokong.net',18,'http://smarttvnews.ru/wp-content/uploads/2015/05/32731097.png')

def CATMUSIC():
            addDir2('[COLOR yellow]MEGA SEARCH BY PIPCAN[/COLOR]','',1000,'')
            addDir('[COLOR yellow]MUSIC [/COLOR]ARTISTS','http://e-mp3bul.com/albumler/2/yabanci-mp3-indir.html',5000,'https://lh5.ggpht.com/is1Mt-5l5uoysOrEZ9MhCn8JAe5_QokIcLdxI_6k-105AB9WTeycHDHbLiX37EYcXg=w300')
            addDir('[COLOR yellow]MUSIC [/COLOR]ALBUMS','http://e-mp3bul.com/album/142/2015.html',5000,'https://lh5.ggpht.com/is1Mt-5l5uoysOrEZ9MhCn8JAe5_QokIcLdxI_6k-105AB9WTeycHDHbLiX37EYcXg=w300')
def CATANIME():
            addDir2('[COLOR yellow]MEGA SEARCH BY PIPCAN[/COLOR]','',1000,'')
            addDir('[COLOR yellow]VIDEOS [/COLOR]FAILARMY','http://www.failarmy.com',4444,'http://www.failarmy.com/2.0.39/media/img/site-logo-sm.png')
            addDir('[COLOR yellow]CARTOONS [/COLOR]Toonova','http://www.toonova.com/cartoon',8000,'http://www.toonova.com/images/site/front/logo.png')
            addDir('[COLOR yellow]CARTOONS [/COLOR]www.animetoon.eu','http://www.animetoon.eu/cartoon',8000,'http://www.animetoon.eu/images/site/front/logo.png')
            addDir('[COLOR yellow]CARTOONS MOVIES[/COLOR]www.animetoon.eu','http://www.animetoon.eu/movies',8000,'http://www.animetoon.eu/images/site/front/logo.png')
            addDir('Animewow','http://www.animewow.eu/anime',8000,'http://www.animewow.eu/images/site/front/logo.png')
            addDir('Animakai.tv','http://www.animakai.tv/animes/1/',13,'http://www.animakai.tv/sys_misc/images/logo.png')
            addDir('[COLOR yellow]DUBBED ANIME [/COLOR]http://www.animetoon.eu/dubbed-anime','http://www.animetoon.eu/dubbed-anime',8000,'http://www.animetoon.eu/images/site/front/logo.png')
            addDir('[COLOR yellow]ANIME MOVIES [/COLOR]videozoo','http://www.videozoo.me/category/anime-movies',8000,'http://www.videozoo.me/wp-content/themes/anime/images/header.jpg')
            addDir('videozoo','http://www.videozoo.me/new-anime-list',8000,'http://www.videozoo.me/wp-content/themes/anime/images/header.jpg')
            addDir('[COLOR yellow]ANIME,CARTOONS,MOVIES [/COLOR]watchcartoonweb','http://watchcartoonweb.com/',9000,'http://watchcartoonweb.com/themes/default/img/icon/logo.png')
def CATVIDEOS():
            addDir2('[COLOR yellow]MEGA SEARCH BY PIPCAN[/COLOR]','',1000,'')
            addDir('[COLOR yellow]VIDEOS [/COLOR]FAILARMY','http://www.failarmy.com',4444,'http://www.failarmy.com/2.0.39/media/img/site-logo-sm.png')
            addDir('Search Bing Videos','http://www.msn.com/en-us/video/searchresults?q=',37,'http://microsoft-news.com/wp-content/uploads/2014/09/Bing-logo-1.jpg')
def CATDOCS():
            addDir2('[COLOR yellow]MEGA SEARCH BY PIPCAN[/COLOR]','',1000,'')
            addDir('[COLOR yellow]Documentary[/COLOR] Top Documentary Films','http://www.topdocumentaryfilms.com/watch-online/',4448,'')
def CATIPTV():
            addDir2('[COLOR yellow]MEGA SEARCH BY PIPCAN[/COLOR]','',1000,'')
            searchStr = ''
            addDir('Search PASTEBIN','https://www.googleapis.com/customsearch/v1element?key=AIzaSyCVAXiUzRYsML1Pv6RwSG1gunmMikTzQqY&rsz=filtered_cse&num=20&hl=en&prettyPrint=false&source=gcsc&gss=.com&sig=56f70d816baa48bdfe9284ebc883ad41&cx=013305635491195529773:0ufpuq-fpt0&sort=date&q=',503,'http://pastebin.com/i/fb2.jpg')
            addDir('http://80.80.160.168/live/','http://80.80.160.168/live',8,'ww')
            addDir('TV Online Streams','http://tvonlinestreams.com',100,'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTdHvBF68jexfm7JTjh692IRi4xC5EbtIy5fDsMcE3ItOqMhXpN')
            addDir('IPTV Filmover','http://iptv.filmover.com',200,'http://website.informer.com/thumbnails/280x202/i/iptv.filmover.com.png')
            addDir('FreeTux TV','http://database.freetuxtv.net',300,'http://lh5.googleusercontent.com/-3BqBJNvGN-E/TqQWikkIrfI/AAAAAAAAAnk/nGx_J8pK1mU/s1600/freetuxtv.png')
            addDir('I-PTV BLOGSPOT','http://i-ptv.blogspot.co.uk',401,'http://4.bp.blogspot.com/-nHAYhJE46Vg/VG27mtXmXYI/AAAAAAAAA4Q/-_QhnzBJ8M4/s1600/logo2%2B-%2B500.png')
            addDir('I-PTV BLOGSPOT RUSSIA','http://i-ptv.blogspot.co.uk/p/russia-big.html',401,'http://4.bp.blogspot.com/-nHAYhJE46Vg/VG27mtXmXYI/AAAAAAAAA4Q/-_QhnzBJ8M4/s1600/logo2%2B-%2B500.png')
            addDir('Pastebin m3u','https://www.googleapis.com/customsearch/v1element?key=AIzaSyCVAXiUzRYsML1Pv6RwSG1gunmMikTzQqY&rsz=filtered_cse&num=20&hl=en&prettyPrint=false&source=gcsc&gss=.com&sig=56f70d816baa48bdfe9284ebc883ad41&cx=013305635491195529773:0ufpuq-fpt0&q=m3u&sort=date',501,'http://pastebin.com/i/fb2.jpg')
            addDir('Pastebin M3U8','https://www.googleapis.com/customsearch/v1element?key=AIzaSyCVAXiUzRYsML1Pv6RwSG1gunmMikTzQqY&rsz=filtered_cse&num=20&hl=en&prettyPrint=false&source=gcsc&gss=.com&sig=56f70d816baa48bdfe9284ebc883ad41&cx=013305635491195529773:0ufpuq-fpt0&q=m3u8&sort=date',501,'http://pastebin.com/i/fb2.jpg')
            addDir('TV Degunino','http://tv.degunino.net/m3u/',8,'')
            addDir('tunisia-dreambox','http://www.tunisia-dreambox.info/e2-addons-manager/Tunisiasat-plugins/softupdates/TSmedia/',8,'')
            addDir('iptvm3u','http://www.iptvm3u.com/search?updated-max=2016-03-03T15%3A14%3A00-08%3A00&max-results=7000',600,'http://3.bp.blogspot.com/-mMVnbnRsISw/U7c8sb8Z2uI/AAAAAAAAAL8/_6Vfvpcfa7c/s1600/freeiptv.png')
            addDir('VLC','http://www.vlchistory.eu.pn',701,'http://www.vlchistory.eu.pn/images/vlcstreamhistory.jpg')
            addDir('langamepp','http://langamepp.com/playlist/pipcan/Snooker85',504,'http://langamepp.com/iptv/img/logo.png')
            addDir('http://www.iptvlinks.com/','http://www.iptvlinks.com/feeds/posts/summary?alt=json-in-script&callback=pageNavi&max-results=200',2000,'http://4.bp.blogspot.com/-D4Nbf7BM52c/VIzTSja7qdI/AAAAAAAACe4/u7PSn24mxK8/s1600/iptvlinkslogo.png')
            addDir('Newstvgenre Altervista/?s=IPTV','http://newstvgenre.altervista.org/?s=IPTV',8005,'http://www.videozoo.me/wp-content/themes/anime/images/header.jpg')
            addDir('[COLOR yellow]VIDEOS [/COLOR]http://free-links-iptv.blogspot.co.uk/','https://www.blogger.com/feeds/7582140021242686461/posts/summary?alt=json-in-script&start-index=1&max-results=10',2000,'')
            addDir('NAVI-XTREAM','http://www.navixtreme.com/wiilist/',730,'')
def NAVIX(url):
        link = OPEN_URL(url)
        match=re.compile('type=playlist\nname=(.+?)\nthumb=(.+?)\nURL=(.+?)\n').findall(link)
        match3=re.compile('name=>>>.+?URL=http:\/\/www\.navixtreme\.com\/wiilist\/(.+)', re.DOTALL).findall(link)
        match1=re.compile('type=video\nname=(.+?)\nthumb=(.+?)\nURL=(.+?)\n').findall(link)
        for name,thumb,url in match:
            addDir(name,url,730,thumb)
        for name,thumb,url in match1:
            addDir2('%s'%(name),'%s'%(url),9,thumb)
        for url in match3:
            addDir('NEXT >>>','http://www.navixtreme.com/wiilist/%s'%url,730,'')
def DOC(url):
        link = OPEN_URL(url)
        match=re.compile('<a href="http://topdocumentaryfilms.com/category/(.+?)" title="Browse.+?">(.+?)</a>(.+?)</h2>').findall(link)
        match2=re.compile('<a href="(.+?)" title="(.+?)"><img width="95" height="125" src="(.+?)"').findall(link)
        match3=re.compile('embedUrl" content="(.+?)"').findall(link)
        match4=re.compile('href="/(.+?)">Next<\/a>"').findall(link)
        for url,name,count in match:
            addDir('%s - %s'%(name,count),'http://www.topdocumentaryfilms.com/category/%s'%url,4448,'')
        for url,name,image in match2:
            addDir2('%s'%(name),url,4448,image)
        for url in match4:
            addDir('[COLOR yellow]NEXT PAGE[/COLOR]',('http://www.topdocumentaryfilms.com/category/%s')%url,4448,'')
        for url in match3:
            import urlresolver
            from urlresolver import common
            dp = xbmcgui.DialogProgress()
            dp.create('Featching Your Video','Opening ')
            play=xbmc.Player(GetPlayerCore())
            url=urlresolver.HostedMediaFile(url.replace('youtube.com/embed/','youtube.com/watch?v=')).resolve() 
            play.play(url)
def failarmy(url):
        link = OPEN_URL(url)
        match=re.compile('<li data-tag="(.+?)"><figure><a href="(.+?)"><div class="img"><img src="(.+?)"').findall(link)
        match2=re.compile('<a href="/video/(.+?)/.+?"><div class="img"><img src="(.+?)" alt="(.+?)"><span class="time">(.+?)</span>').findall(link)
        for name,url,image in match:
            addDir('[UPPERCASE]%s[/UPPERCASE]'%name,'http://www.failarmy.com%s'%url,4444,image)
        for url,image,name,time in match2:
            addDir2('%s - %s'%(name,time),'http://makerplayer.com/embed/failarmy/%s?maker=1&autoplay=true&no_postroll=true&embed_params=brandlink=http://www.failarmy.com&brandname=Fail'%url,4445,image)
def failarmy2(url):
        link = OPEN_URL(url)
        match=re.compile('file":"(.+?)"').findall(link)
        for url in match:
            dp = xbmcgui.DialogProgress()
            dp.create('Featching Your Video','Opening')
            play=xbmc.Player(GetPlayerCore())
            play.play(url)
def watchcartoonweb(url):
        link = OPEN_URL(url)
        match=re.compile('<li class=".+?"><a href="http://watchcartoonweb.com/(.+?)" title="(.+?)">.+?</a></li>').findall(link)
        match2=re.compile(' <a href="(.+?)" title="(.+?)">\n.+?<div class="thumbnail-recent" style="background: url\(\'(.+?)\'\);">').findall(link)
        match3=re.compile('<a href="http://watchcartoonweb.com/category/(.+?)" title="(.+?)">.+?</a>').findall(link)
        match4=re.compile('<img src="(.+?)">\n.+?<h1>(.+?)</h1>').findall(link)
        match5=re.compile('<span>Plot Summary: </span>(.+?)</p>').findall(link)
        match6=re.compile('<li><a href="(.+?)" title="(.+?)">.+?</a>\n.+?<div class="go_time">').findall(link)
        match7=re.compile('<option value="(.+?)">(\d\d\d\w)</option>').findall(link)
        for url,name in match:
            addDir('[B]%s[/B]'%(name),'http://watchcartoonweb.com/%s'%url,9000,'')
        for url,name,image in match2:
            addDir2('[COLOR yellow]V--------------------------COVER & NAME--------------------------V[/COLOR]','',9000,'')
            addDir('%s'%(name),'%s'%url,9000,image)
        for url,name in match3:
            addDir(name,'http://watchcartoonweb.com/category/%s'%url,9000,'')
        for image,name in match4:
            addDir(name,'',9000,image)
        for name in match5:
            addDir2('[COLOR yellow]V--------------------------PLOT-------------------------V[/COLOR]','',9000,'')
            addDir('[I]%s[/I]'%name,'',9000,'')
            addDir2('[COLOR yellow]V--------------------------MEDIA--------------------------V[/COLOR]','',9000,'')
        for url,name in match6:
            addDir('%s'%name,url,9000,'')
        for url,name in match7:
            addDir2('[COLOR yellow]V--------------------------SELECT QUALITY--------------------------V[/COLOR]','',9000,'')
            addDir2('%s'%name,url,9,'')
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
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36')
        req.add_header('Referer', '%s'%url)
        req.add_header('Connection', 'keep-alive')
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
def altervista(url):
        link = OPEN_URL(url)
        match=re.compile('<a href="(.+?)" title="Permalink to (.+?)" rel="bookmark">').findall(link)
        match2=re.compile('#EXTINF:.+?,(.+?)<br />\n(.+?)<br />').findall(link)
        match3=re.compile('#EXTINF:.+?,(.+?)<br />(.+?)<').findall(link)
        match4=re.compile('<p>(.+?)<br/>(.+?) </p>').findall(link)
        match5=re.compile('#EXTINF:.+?,(.+?)<br />\n(.+?)</p>').findall(link)
        match6=re.compile('a href="(.+?)" ><span class="meta-nav">&larr;</span>(.+?)</a>').findall(link)
        for url,name in match:
            addDir('%s'%(name),'%s'%url,8005,'')
        for name,url in match2:
            addDir2('%s'%(name),'%s'%url,9,'')
        for name,url in match3:
            addDir2('%s'%(name),'%s'%url,9,'')
        for name,url in match4:
            addDir2('%s'%(name),'%s'%url,9,'')
        for name,url in match5 	:
            addDir2('%s'%(name),'%s'%url,9,'')
        for url,name in match6 	:
            addDir('%s'%(name),'%s'%url,8005,'')
def CARTOONS(url):
        link = OPEN_URL(url)
        match=re.compile('<td><a href="(.+?)">(.+?)</a>').findall(link)
        match2=re.compile('&nbsp;&nbsp;<a href="(.+?)">(.+?)</a>').findall(link)
        match3=re.compile('<a href="(.+?)" title="View all posts filed under .+?">(.+?)</a>').findall(link)
        match4=re.compile('href="(.+?)" rel="bookmark" title="(.+?)"').findall(link)
        for url,name in match:
            addDir('%s'%(name),'%s'%url,8000,'')
        for url,name in match2:
            addDir('%s'%(name),'%s'%url,8001,'')
        for url,name in match3:
            addDir('%s'%(name),'%s'%url,8000,'')
        for url,name in match4:
           addDir('%s'%(name),'%s'%url,8001,'')
def CARTOONS2(url):
        link = OPEN_URL(url)
        match=re.compile('<iframe src="(.+?)"').findall(link)
        for url in match:
            addDir2('%s'%(url.replace('&#038;','&')),'%s'%url.replace('&#038;','&'),8003,'')
def CARTOONS3(url):
        link = OPEN_URL(url)
        match=re.compile("url: '(.+?)'").findall(link)
        for url in match:
            dp = xbmcgui.DialogProgress()
            dp.create('Featching Your Video','Opening Ready')
            play=xbmc.Player(GetPlayerCore())
            play.play(url)
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
def show_countdown(self, time_to_wait, title='', text=''):       
        dialog = xbmcgui.DialogProgress()
        ret = dialog.create(title)        
        secs = 0
        increment = 100 / time_to_wait
        cancelled = False
        while secs <= time_to_wait:
            if (dialog.iscanceled()):
                cancelled = True
                break
            if secs != 0: 
                xbmc.sleep(1000)
            secs_left = time_to_wait - secs
            if secs_left == 0: 
                percent = 100
            else: 
                percent = increment * secs            
            remaining_display = ('Wait %d seconds for the ' +
                    'video stream to activate...') % secs_left
            dialog.update(percent, text, remaining_display)
            secs += 1
        if cancelled == True:     
            return False
        else:
            return True        


def MYMOVIES(url):
        xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_TITLE )
        xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_NONE )
        xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_FULLPATH )
        xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_FILE )
        link = OPEN_URL(url)
        match=re.compile('https://openload.co/f/(.+?)/(.+?)\n').findall(link)
        match2=re.compile('id="realGkfuuudownload"><a href="(.+?)"').findall(link)
        for url,name in match:
            addDir2('%s'%(name.replace('720P','[COLOR gold]720p[/COLOR]').replace('720p','[COLOR gold]720p[/COLOR]').replace('4k','[COLOR gold]4K[/COLOR]').replace('4k','[COLOR gold]4K[/COLOR]').replace('1080P','[COLOR gold]1080p[/COLOR]').replace('1080p','[COLOR gold]1080p[/COLOR]').replace('_',' ').replace('mkv',' ').replace('.',' ').replace('mp4',' ').replace('MovieFarsi','')),'https://openload.io/f/%s/%s'%(url,name),555,'')
        for url2 in match2:
            play=xbmc.Player(GetPlayerCore())
            message = 'PLEASE WAIT 5 SECONDS'
            dp = xbmcgui.DialogProgress()
            dp.create('Wait ',message)
            xbmc.sleep(1000)
            dp.update(20,'PLEASE WAIT 4 SECONDS')
            xbmc.sleep(1000)
            dp.update(40,'PLEASE WAIT 3 SECONDS')
            xbmc.sleep(1000)
            dp.update(60,'PLEASE WAIT 2 SECONDS')
            xbmc.sleep(1000)
            dp.update(80,'PLEASE WAIT 1 SECONDS')
            xbmc.sleep(1000)
            dp.update(100,'YOUR VIDEO IS READY')
            xbmc.sleep(1000)
            play.play(url2)
            dp.close
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
    import urlresolver
    from urlresolver import common
    play=xbmc.Player(GetPlayerCore())
    dp = xbmcgui.DialogProgress()
    dp.create('Featching Your Video','Trying To Play Directly')
    try: play.play(url)
    except: pass
    dp.update(50,'Trying Directly')
    try: url=urlresolver.HostedMediaFile(url).resolve()
    except: pass 
    dp.create('Featching Your Video','Trying With Url Resolver')
    dp.update(50,'Trying To Resollver')
    try: play.play(url)
    except: pass 
    dp.close()
    
def PLAYVIDEO3(url):
    import urlresolver
    from urlresolver import common
    dp = xbmcgui.DialogProgress()
    dp.create('Featching Your Video','Opening Ready')
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
def add_item( action="" , title="" , plot="" , url="" ,thumbnail="" , extra="", isPlayable = False, folder=True ):
    listitem = xbmcgui.ListItem( title, iconImage="DefaultVideo.png", thumbnailImage=thumbnail )
    listitem.setInfo( "video", { "Title" : title, "FileName" : title, "Plot" : plot } )
    
    if url.startswith("plugin://"):
        itemurl = url
        listitem.setProperty('IsPlayable', 'true')
        xbmcplugin.addDirectoryItem( handle=int(sys.argv[1]), url=itemurl, listitem=listitem, isFolder=folder)
    elif isPlayable:
        listitem.setProperty("Video", "true")
        listitem.setProperty('IsPlayable', 'true')
        itemurl = '%s?action=%s&title=%s&url=%s&thumbnail=%s&plot=%s&extra=%s' % ( sys.argv[ 0 ] , action , urllib.quote_plus( title ) , urllib.quote_plus(url) , urllib.quote_plus( thumbnail ) , urllib.quote_plus( plot ) , urllib.quote_plus( extra ))
        xbmcplugin.addDirectoryItem( handle=int(sys.argv[1]), url=itemurl, listitem=listitem, isFolder=folder)
    else:
        itemurl = '%s?action=%s&title=%s&url=%s&thumbnail=%s&plot=%s&extra=%s' % ( sys.argv[ 0 ] , action , urllib.quote_plus( title ) , urllib.quote_plus(url) , urllib.quote_plus( thumbnail ) , urllib.quote_plus( plot ) , urllib.quote_plus( extra ))
        xbmcplugin.addDirectoryItem( handle=int(sys.argv[1]), url=itemurl, listitem=listitem, isFolder=folder)

        
              
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
elif mode==10:
        PLAYVIDEO3(url)
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
elif mode==8000:
        CARTOONS(url)
elif mode==8001:
        CARTOONS2(url)

elif mode==8003:
        CARTOONS3(url)
elif mode==8005:
        altervista(url)
elif mode==9000:
        watchcartoonweb(url)
elif mode==4444:
        failarmy(url)
elif mode==4445:
        failarmy2(url)
elif mode==4448:
        DOC(url)
elif mode==8801:
        CATMOVIES()
elif mode==8802:
        CATVIDEOS()
elif mode==8803:
        CATDOCS()
elif mode==8804:
        CATANIME()
elif mode==8805:
        CATIPTV()
elif mode==8806:
        CATMUSIC()
elif mode==555:
        MYMOVIES(url)
elif mode==730:
        NAVIX(url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
