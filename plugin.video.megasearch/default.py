# -*- coding: utf-8 -*-
import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,datetime,os,requests,HTMLParser,httplib,traceback,mechanize

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
            addDir('[B]SELECT A CATAGORY[/B]','m',8800,'http://icons.iconseeker.com/png/fullsize/toolbar-icons-6/favorites-7.png')
            addDir('[COLOR green]SEARCH[/COLOR] [I]Click here For By 50 + Host[/I]','search',4291,'http://icons.iconseeker.com/png/fullsize/pastel/search-10.png')
            addDir('[COLOR green]SEARCH[/COLOR] [I]Click here For Normal Searches[/I]','search',345,'http://icons.iconseeker.com/png/fullsize/pastel/search-10.png')
#            addDir('[COLOR red][DOWN][/COLOR] [COLOR gold]Direct Movie List[/COLOR]','file:///%s\movies.m3u'%addonDir,555,'')
#            addDir('[COLOR red][DOWN][/COLOR] [COLOR gold]Direct French TV List[/COLOR]','file:///%s\TV2.m3u'%addonDir,555,'')
#            addDir('[COLOR red][DOWN][/COLOR] [COLOR gold]Direct TV List[/COLOR]','file:///%s\TV.m3u'%addonDir,4558,'')
#            addDir('[COLOR red][DOWN][/COLOR] [COLOR gold]TRAILERS[/COLOR]','file:///%s\l.m3u'%addonDir,4559,'')
            addDir('[COLOR gold]MOVIES[/COLOR]','m',8801,'http://icons.iconseeker.com/png/fullsize/smoothicons-5/movies-46.png')
            addDir('[COLOR gold]VIDEOS[/COLOR]','m',8802,'http://icons.iconseeker.com/png/fullsize/on-stage/video-11.png')
            addDir('[COLOR gold]TORRENTS[/COLOR]','m',8899,'http://icons.iconseeker.com/png/fullsize/soft-dimension/utorrent.png')
            addDir('[COLOR gold]DOCUMENTRYS[/COLOR]','m',8803,'http://icons.iconseeker.com/png/fullsize/crystal-project-application/camera-8.png')
            addDir('[COLOR gold]ANIME & CARTOONS[/COLOR]','m',8804,'http://icons.iconseeker.com/png/fullsize/cartoons/disc-3.png')
            addDir('[COLOR gold]IPTV[/COLOR]','m',8805,'http://www.unidat.sk/images/icon_iptv.png')
            addDir('[COLOR gold]TV Guides[/COLOR]','m',8855,'http://apk-dl.com/detail/image/net.micene.minigroup.palimpsests.lite-w250.png')
            addDir('[COLOR gold]MUSIC[/COLOR]','m',8806,'http://icons.iconseeker.com/png/fullsize/fush-folders/music.png')
            addDir('[COLOR gold]ADDONS[/COLOR]','s',1655,'http://icons.iconseeker.com/png/fullsize/fresh-addon/part.png')
            addDir('[COLOR gold]RADIO[/COLOR]','http://listenlive.eu',8890,'http://icons.iconseeker.com/png/fullsize/antique/radio.png')
            addDir('[COLOR gold]CCAMS[/COLOR]','http://laughfactory.com/jokes',731,'http://icons.iconseeker.com/png/fullsize/forum-faces/joker.png')
            addDir('[COLOR gold]MISC[/COLOR]','http://www.tv-logo.com',4913,'http://icons.iconseeker.com/png/fullsize/slate/misc.png')
            addDir('[COLOR gold]Test My M3u [I]Click Here To Test Your Ownn M3u For Broken Links[/I][/COLOR]','f',1457,'http://icons.iconseeker.com/png/fullsize/nova/test-tubes.png')
            addDir('[COLOR gold]OPEN TESTING STOREAGE M3u [I]Click Here [/I][/COLOR]','file:///%s\Links.txt'%addonDir,1458,'http://icons.iconseeker.com/png/fullsize/toolbar-icons-6/favorites-7.png')
def MISC(url):
            addDir('[COLOR gold]TV LOGOS[/COLOR]','http://www.tv-logo.com',5464,'http://img2-1.timeinc.net/ew/i/2011/10/20/Napster-Logo_400.jpg')
            addDir('[COLOR gold]HQ FLAGS[/COLOR]','CONTRRYD',4912,'http://img2-1.timeinc.net/ew/i/2011/10/20/Napster-Logo_400.jpg')
            addDir('[COLOR gold]LANGSAT LOGOS[/COLOR]','http://www.lyngsat-logo.com/tvcountry/tvcountry.html',4915,'http://www.lyngsat-logo.com/images/ls_logo.gif')
            addDir('[COLOR gold]LOTTERY RESULT[/COLOR]','http://www.testious.com/free-cccam-servers',5691,'http://www.lyngsat-logo.com/images/ls_logo.gif')
            addDir('[COLOR gold]News From Torrent Freak[/COLOR]','https://torrentfreak.com/',977,'http://www.lyngsat-logo.com/images/ls_logo.gif')
            addDir('[COLOR gold]LOGOPIDA[/COLOR]','http://logos.wikia.com/wiki/Special:Search?fulltext=Search&search=',9777,'http://www.lyngsat-logo.com/images/ls_logo.gif')
            addDir('[COLOR gold]VIPERGIRLS[/COLOR]','http://vipergirls.to/forum.php',9778,'http://www.lyngsat-logo.com/images/ls_logo.gif')
            addDir('[COLOR gold]EROTIC STORYS[/COLOR]','http://www.asstr.org/files/Collections/',9788,'http://www.lyngsat-logo.com/images/ls_logo.gif')
            addDir('[COLOR gold]TV Player.com[/COLOR]','http://api.tvplayer.com/api/v2/epg/?service=1&platform=website&from=now&hours=0',4927,'http://api.tvplayer.com/assets/img/tvplayer-logo-full.png')
def trailers(url):
        link = OPEN_URL(url)
        match=re.compile('(.+?)\n').findall(link)
        for name in match:
            addDir2(name,name,40,'')
def hostselect(url):
        if url == 'search':
            xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_TITLE)
            page = 1
            searchStr = ''
            keyboard = xbmc.Keyboard(searchStr, 'Search')
            keyboard.doModal()
            searchStr=keyboard.getText()
            list = ['docs.google.com','play.google.com','nowvideo.sx','youtube.com','novamov.com','videoweed.es','vodlocker.com','movshare.net','divxstage.to','vk.com','youwatch.org','vimeo.com','filenuke.com','nowvideo.ch','streamcloud.eu','ishared.eu','cloudtime.to','nowvideo.co','vidbull.com','bloomberg.com','sharesix.com','vidto.me','thevideo.me','comcast.net','freakshare.com','gorillavid.in','abcnews.go.com','movpod.in','videopremium.tv','dailymotion.com','mooshare.biz','powvideo.net','ted.com','thefile.me','edition.cnn.com','itunes.apple.com','myvideo.de','stagevu.com','amazon.com','hulu.com','filehoot.com','flashx.tv','allmyvideos.net','vidzi.tv','vidspot.net','firedrive.com','veehd.com','vid.me','movdivx.com','grifthost.com']
            dialog = xbmcgui.Dialog()
            ret = dialog.select('Select A Host',list)
            url = "https://www.alluc.com/stream/"+searchStr+"+host:"+list[ret]
        r = requests.get(url)
        match=re.compile('<div class="title"> <a href="(.+?)" target="_blank">(.+?)</a> </div>.+?<div style="max-height:68px;overflow:hidden;float:left;display:inline-block;margin-right:8px;">.+?<img alt=".+?" src=".+?"', re.DOTALL).findall(r.content)
        for url2,name in match:
            addDir(name,'https://www.alluc.com%s'%url2,4292,'https://www.alluc.com/thumbnail/SS4/29e1d121178a4ae99eb83afd2b3fd111')
        page = page + 1
        pagecount = page
        addDir('NEXT >>>','%s?page=%s'%(url,pagecount),4291,'')
def hostselect2(url):
    r = requests.get(url)
    match=re.compile('<textarea onClick="this\.select\(\);">(.+?)\n').findall(r.content)
    for url in match:
        addDir2('PLAY VIDEO',url,4,'')
def genccam(url):
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.open(url)
    br.select_form(nr=0)
    result = br.submit().read()
    match=re.compile('<br>(.+?)<br>').findall(result)
    for name in match:
        addDir2(name,name,4287,'')
def joke():
            addDir('[COLOR green]Generator[/COLOR][COLOR gold] kingsat196[/COLOR]','http://kingsat196.ddns.net/index.php',4928,'http://api.tvplayer.com/assets/img/tvplayer-logo-full.png')
            addDir('[COLOR green]Generator[/COLOR][COLOR gold] kader-sat[/COLOR]','http://kader-sat.ddns.net/',4928,'http://api.tvplayer.com/assets/img/tvplayer-logo-full.png')
            addDir('[COLOR green]Generator[/COLOR][COLOR gold] shasha-tv[/COLOR]','http://shasha-tv.blogsyte.com/',4928,'http://api.tvplayer.com/assets/img/tvplayer-logo-full.png')
            addDir('[COLOR green]Generator[/COLOR][COLOR gold] c-generator.blogsyte[/COLOR]','http://c-generator.blogsyte.com/c2015/',4928,'http://api.tvplayer.com/assets/img/tvplayer-logo-full.png')
            addDir('[COLOR green]Generator[/COLOR][COLOR gold] star-cccam[/COLOR]','http://star-cccam.sytes.net/CCcam/',4928,'http://api.tvplayer.com/assets/img/tvplayer-logo-full.png')
            addDir('[COLOR green]Generator[/COLOR][COLOR gold] star-cccam[/COLOR]','http://www.clinefree.com/',4928,'http://api.tvplayer.com/assets/img/tvplayer-logo-full.png')
            addDir('[COLOR gold]CCAMS[/COLOR]','http://www.hack-sat.com/cccam&newcamd.html',4286,'http://www.lyngsat-logo.com/images/ls_logo.gif')
            addDir('[COLOR gold]ocbfreeservers[/COLOR]','https://sites.google.com/site/ocbfreeservers/home/free-servers/cccam-free-servers',4286,'http://www.lyngsat-logo.com/images/ls_logo.gif')
            addDir('[COLOR gold]CCams select-pedia [/COLOR]','http://select-pedia.com/tutos/category/cccam-servers/',4289,'http://www.lyngsat-logo.com/images/ls_logo.gif')
            addDir('[COLOR gold]CCAMS Testious.com[/COLOR]','http://www.testious.com/free-cccam-servers',4286,'http://www.lyngsat-logo.com/images/ls_logo.gif')

def megasearch(url):
    dialog = xbmcgui.Dialog()
    ret = dialog.select('Select A Host',['Mega', 'Uptobox', 'Uplea', '1fichier', 'Uploaded', 'Rapidgator', 'Turbobit', 'Keep2share', 'Bitshare', 'Filefactory', 'Free', 'Oboom', 'Filepost', 'Depfile', 'Firedrive', 'Mediafire', 'Uploadable', 'Hugefiles', 'ClicknUpload', 'ZippyShare', 'Ryushare', '2shared', 'Depositfiles', 'Purevid', 'Exashare', 'Youwatch'])  
    searchStr = ''
    keyboard = xbmc.Keyboard(searchStr, 'Search')
    keyboard.doModal()
    searchStr=keyboard.getText()
    r = requests.get(url+searchStr)
    match=re.compile('<a class="link_result" target="_blank" href="(.+?)">.+?<span class="img"><img src="(.+?)"', re.DOTALL).findall(r.content)
    for url,img in match:
        addDir(url.replace('http://megasearch.co/link/',''),url,9711,img)
def Guidecat():
            xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_TITLE)
            addDir('...Search','http://en.timefor.tv/search/?channels=all&title=on&period=1209600&q=',4118,'https://img01.bt.co.uk/s/assets/170815/tve/img/BT-Logo.png')
            addDir('UK','https://voila.metabroadcast.com/1.0/schedules/?annotations=broadcasts,locations,description&apiKey=public:64a03c33f9a64c2b80b6f58cd218e5c8&from=now&count=2&id=hkq7,hkq7,hn2v,hkvp,hkvp,hkvb,hkvb,hkvk,hk7x,hkyp,hmbs,hm77,hky6,hm4r,hk5v,hkzp,hkzt,hn6s,hn6t,hn7d,hkwj,hkwm,hkwp,hk7y,hkyn,hn8c,hk8t,hn4f,hmhb,hkzw,hk5s,hk4s,hnz2,hkwb,hn2c,hm6d,hkwz,hkwx,hkwx,hkxc,hkxb,hnzn,hkxf,hm2w,hkqz,hkrh,hkrh,hmb4,hk9n,hkxz,hk9x,hm6w,hk92,hk9z,hkzq,hny5,hk56,hk57,hn29,hk5q,hn6h,hm27,hn4m,hk5t,hpbt,hkx2,hmb2,hky7,hk8k,hnyj,hkvh,hmb5,hk5n,hkvn,hn68,hkvm,hkvj,hkv7,hn86,hkw9,hm6z,hn97,hn4k,hmbc,hnxq,hnz6,hmcj,hk47,hk9b,hkxk,hnz5,hpdr,hkxd,hkzs,hk9p,hkx4,hn6k,hn8t,hn9m,hn6b,hkzr,hkvf,hnw7,hkzn,hkzv,hkxh,hpbg,hn8b,hkrq,hkrr,hn9k,hk87,hk45,hk2f,hn9t,hmb7,hkxr,hmbx,hmbr,hk2z,hkwh,hkzm,hkwy,hn6y,hkvc,hk9f,hk8m,hn28,hn9g,hn6g,hn9h,hpcj,hk4t,hk2g,hk2h,hk54,hk4d,hkx5,hk86,hk44,hkzk,hk95,hkxt,hk96,hkxv,hn9f,hk8p,hmbg,hk4c,hn9c,hn9p,hkwk,hn8g,hn9y,hk89,hkwn,hn7t,hkxs,hn9b,hpdp,hk68,hk67,hmbv,hk7r,hn2y,hk7g,hk7d,hk7b,hk65,hk7j,hk7m,hk7t,hk66,hk2c,hk2d,hnyf,hn5q,hk5d,hk5f,hk55,hk8y,hm7h,hm22,hk8w,hk8x,hmcf,hmcg,hn7y,hmbt,hk7q,hn2x,hk7f,hk7c,hk69,hk64,hk7h,hk7k,hk7s,hkzy,hkvd,hpb8,hmb8,hkxq,hkxp,hk27,hkyk,hkzd,hkzc,hk94,hny2,hkx8,hkvg,hk2p,hk4p,hk4n,hnbd,hk4j,hn87,hk4w,hk4q,hm6h,hpdw,hn9w,hk4v,hk8s,hk4x,hn96,hn95,hn94,hk9c,hn92,hn9z,hm4h,hk6q,hk6r,hk8r,hmbq,hn8n,hnxp,hk2k,hk2s,hk2n,hnz8,hk2m,hn4y,hpck,hk4f,hn4v,hn8y,hk26,hpb5,hk5h,hk9s,hn4x,hnw6,hm62,hk5g,hpcm,hk2t,hk2v,hn85,hk2w,hn8p,hnxn,hk5p,hk52,hmbf,hkqk,hk2j,hpbc,hn4w,hk9r,hpdm,hn84,hpby,hpbz,hkyj,hkx7,hn6x,hkrv,hn2d,hkx9,hnxb,hn7q,hnzd,hny7,hk7v,hkyh,hnw5,hk6k,hkzg,hk9d,hm6y,hkzj,hkyv,hk6m,hky5,hk9m,hk7w,hky2,hk84,hk5b,hk49,hmck,hkys,hkyt,hk4k,hk4m,hk4r,hky4,hk6t,hkyz,hkyg,hn4h,hk9k,hk6w,hk6v,hkyw,hkzf,hkyf,hk48,hkrs,hn9n,hn98,hkyc,hm7c,hn7k,hpcf,hnx4,hkz2,hk4g,hk9w,hk9v,hm54,hky9,hn4d,hk2r,hn6v,hn6r,hkz5,hk8h,hk8j,hkz7,hk7z,hk99,hkxj,hk9t,hnyz,hkry,hm5c,hm6t,hn7c,hk2q,hn8z,hny4,hky8,hkzz,hkrx,hkyb,hkz6,hk2y,hk72,hk76,hnx7,hnyt,hkx6,hk6n,hk24,hkzx,hn4z,hnz7,hkxy,hkxx,hn24,hm55,hpb2,hkxw,hn46,hn4r,hnw4,hn45,hk78,hn5h,hn4b,hk28,hn88,hmcb,hnx9,hnxg,hkzb,hnxy,hnzx,hnzc,hny9,hnzf,hkqs,hkq2,hkrg,hkrf,hkq4,hkrd,hkqy,hkqx,hnwz,hkq8,hnwx,hkrc,hkrb,hnwy,hkrm,hkrn,hkrj,hkq6,hkq9,hkqt,hmbn,hmbn,hkth,hktk,hktm,hktn,hktp,hmcx,hmcn,hmcy,hmc5,hmxb,hmc6,hmvy,hmcm,hmrp,hktv,hktw,hkt4,hktz,hm56,hktr,hmsy,hmvz,hmpy,hkt9,hktj,hkty,hkt8,hktq,hkrz,hkt7,hmyk,hmqf,hmyj,hmyn,hmcv,hmv9,hmqt,hmvc,hmcs,hmwz',5691,'%s/resources/flags/Akrotiri.png'%addonDir)
            addDir('India','http://tv.burrp.com/channels.html',4111,'%s/resources/flags/India.png'%addonDir)
            addDir('POLAND','http://www.teleman.pl',4113,'%s/resources/flags/Akrotiri.png'%addonDir)
            addDir('Poland','http://tv.wp.pl/?ticaid=115939',4113,'%s/resources/flags/Poland.png'%addonDir)
            addDir('Portugal','http://cabovisao.pt/tv_guiatv.php?y=2015&m=9&d=13&h=9&c=1000&f=Todos&o=iziepg_schedule&epg_face=yes',4114,'%s/resources/flags/Akrotiri.png'%addonDir)
            addDir('Portugal2','http://meogo.meo.pt/tv/guiatv/Pages/default.aspx',4114,'%s/resources/flags/Akrotiri.png'%addonDir)
            addDir('Romania','http://programetv.program24.ro/acum-la-tv.html',4115,'%s/resources/flags/Romania.png'%addonDir)
            addDir('Canadian','http://tvmds.tvpassport.com/snippet/white_label/php/grid.php?subid=tvpassport&lu=3895D&wd=940&ht=445&mode=json&&items=180',4113,'%s/resources/flags/Canada.png'%addonDir)
            addDir('UK','http://en.timefor.tv/ajax/channel_list.php?language=uk',4117,'%s/resources/flags/Akrotiri.png'%addonDir)
            addDir('Denmark','http://en.timefor.tv/ajax/channel_list.php?language=dk',4117,'%s/resources/flags/Denmark.png'%addonDir)
            addDir('Finland','http://en.timefor.tv/ajax/channel_list.php?language=fi',4117,'%s/resources/flags/Finland.png'%addonDir)
            addDir('France','http://en.timefor.tv/ajax/channel_list.php?language=fr',4117,'%s/resources/flags/France.png'%addonDir)
            addDir('Germany','http://en.timefor.tv/ajax/channel_list.php?language=de',4117,'%s/resources/flags/Germany.png'%addonDir)
            addDir('Italy','http://en.timefor.tv/ajax/channel_list.php?language=it',4117,'%s/resources/flags/Italy.png'%addonDir)
            addDir('SPORTS','http://tecbox.tv/repo/teciptvguide/sports.xml',4560,'%s/resources/flags/Italy.png'%addonDir)
            addDir('STALKER','http://tecbox.tv/repo/teciptvguide/stalker1.xml',4560,'%s/resources/flags/Italy.png'%addonDir)
            addDir('SPORTS DONKY','http://tecbox.tv/repo/teciptvguide/donkey.xml',4560,'%s/resources/flags/Italy.png'%addonDir)
            addDir('USVTV','http://tecbox.tv/repo/teciptvguide/guide3.xmltv',4560,'%s/resources/flags/Italy.png'%addonDir)
            addDir('NTV','http://tecbox.tv/repo/teciptvguide/guide2.xml',4560,'%s/resources/flags/Italy.png'%addonDir)
            addDir('MOBSTERS','http://tecbox.tv/repo/teciptvguide/mobsters.xml',4560,'%s/resources/flags/Italy.png'%addonDir)
            addDir('AMYS','http://tecbox.tv/repo/teciptvguide/amylist.xml',4560,'%s/resources/flags/Italy.png'%addonDir)
            addDir('Netherlands','http://en.timefor.tv/ajax/channel_list.php?language=nl',4117,'%s/resources/flags/Netherlands.png'%addonDir)
            addDir('Norway','http://en.timefor.tv/ajax/channel_list.php?language=no',4117,'%s/resources/flags/Norway.png'%addonDir)
            addDir('Poland','http://en.timefor.tv/ajax/channel_list.php?language=po',4117,'%s/resources/flags/Poland.png'%addonDir)
            addDir('Russia','http://en.timefor.tv/ajax/channel_list.php?language=ru',4117,'%s/resources/flags/Russia.png'%addonDir)
            addDir('Spain','http://en.timefor.tv/ajax/channel_list.php?language=es',4117,'%s/resources/flags/Spain.png'%addonDir)
            addDir('Sweden','http://en.timefor.tv/ajax/channel_list.php?language=se',4117,'%s/resources/flags/Sweden.png'%addonDir)
            addDir('Switzaland','http://en.timefor.tv/ajax/channel_list.php?language=sw',4117,'%s/resources/flags/Switzerland.png'%addonDir)
            addDir('Turkey','http://en.timefor.tv/ajax/channel_list.php?language=tr',4117,'%s/resources/flags/Turkey.png'%addonDir)
            addDir('Austria','http://en.timefor.tv/ajax/channel_list.php?language=at',4117,'%s/resources/flags/Austria.png'%addonDir)
            addDir('Benelux','http://en.timefor.tv/ajax/channel_list.php?language=be',4117,'%s/resources/flags/Akrotiri.png'%addonDir)
            addDir('Bailtikum','http://en.timefor.tv/ajax/channel_list.php?language=ee,lv,lt',4117,'%s/resources/flags/Akrotiri.png'%addonDir)
            addDir('Ireland','http://entertainment.ie/tv/whats-on-now.asp?utm_source=entertainment.ie&utm_medium=navmenu&utm_campaign=fullmenu',191,'%s/resources/flags/Ireland.png'%addonDir)
            addDir('Ireland','https://web-api-salt.horizon.tv/oesp/api/IE/eng/web/channels?includeInvisible=true&byLocationId=6651943228&personalised=false',192,'%s/resources/flags/Ireland.png'%addonDir)
            addDir('Germany','https://web-api-salt.horizon.tv/oesp/api/DE/deu/web/channels?includeInvisible=true&byLocationId=97245734974&personalised=false',192,'%s/resources/flags/Germany.png'%addonDir)
            addDir('Netherlands','https://web-api-salt.horizon.tv/oesp/api/NL/nld/web/channels?includeInvisible=true&byLocationId=24443942973&personalised=false',192,'%s/resources/flags/Netherlands.png'%addonDir)
            addDir('Switzaland','https://web-api-salt.horizon.tv/oesp/api/CH/deu/web/channels?includeInvisible=true&byLocationId=21656615412&personalised=false',192,'%s/resources/flags/Switzerland.png'%addonDir)
            addDir('Czech','https://web-api-salt.horizon.tv/oesp/api/CZ/ces/web/channels?includeInvisible=true&byLocationId=546677286980&personalised=false',192,'%s/resources/flags/Czech Republic.png'%addonDir)
            addDir('Poland','https://web-api-salt.horizon.tv/oesp/api/PL/pol/web/channels?includeInvisible=true&byLocationId=239100967286&personalised=false',192,'%s/resources/flags/Poland.png'%addonDir)
            addDir('Romania','https://web-api-salt.horizon.tv/oesp/api/RO/ron/web/channels?includeInvisible=true&byLocationId=552441895089&personalised=false',192,'%s/resources/flags/Romania.png'%addonDir)
            addDir('Austria','https://web-api-salt.horizon.tv/oesp/api/AT/deu/web/channels?includeInvisible=true&byLocationId=554823207312&personalised=false',192,'%s/resources/flags/Austria.png'%addonDir)
            addDir('Hungary','https://web-api-salt.horizon.tv/oesp/api/HU/hun/web/channels?includeInvisible=true&byLocationId=552442407296&personalised=false',192,'%s/resources/flags/Hungary.png'%addonDir)
            addDir('Kosovo','http://tvim.tv/script/webepg/nowontv/',198,'%s/resources/flags/Hungary.png'%addonDir)
            addDir('Kosovo2','http://ipko.com/epg/admin/channels.php',199,'%s/resources/flags/Hungary.png'%addonDir)
            addDir('Eygpt','http://elcinema.com/en/tvguide/',120,'%s/resources/flags/Hungary.png'%addonDir)
            addDir('Hong Kong','http://tvbnetworkvision.com/en/epg/',205,'%s/resources/flags/Hungary.png'%addonDir)
            addDir('New Zeland','http://www.freeviewnz.tv/tvguide/whats-on/?nowAndNext=true',206,'%s/resources/flags/Hungary.png'%addonDir)
def newz(url):
    r = requests.get(url)
    test = [url for url in re.findall(r'/nonumbracoimages/ChannelsOpg/(.+?)\?w=140&amp;h=90&amp;mode=crop" alt="(.+?)"', r.text)]
    for img,name in test:
        addDir(name,'',206,'http://www.freeviewnz.tv/nonumbracoimages/ChannelsOpg/%s?w=140&amp;h=90&amp;mode=crop'%img)
def EROTIC(url):
    url = url
    r = requests.get(url)
    match=re.compile('href="(.+?)/">(.+?)<').findall(r.content)
    match2=re.compile('href="(.+?)txt">(.+?)<').findall(r.content)
    for url2,name in match:
        addDir('[COLOR yellow]FOLDER[/COLOR] - %s'%name,'%s%s/'%(url,url2),9788,'')
    for url2,name in match2:
        addDir2('[COLOR green]READ[/COLOR] - %s'%name,'%s%stxt'%(url,url2),9789,'')
def EROTIC2(url):
    r = requests.get(url)
    showText('READ',r.content)
def hongkong(url):
    r = requests.get(url)
    test = [url for url in re.findall(r'<li><a href="/en/epg/(.+?)">(.+?)<', r.text)]
    for url,name in test:
        addDir(name,'http://tvbnetworkvision.com/en/epg/%s'%url,205,'')
def elcinema(url):
    r = requests.get(url)
    test = [url for url in re.findall(r'title=".+?" src="(.+?)" />', r.text)]
    for img in test:
        addDir('','',120,img)
def trimtv(url):
    r = requests.get(url)
    test = [url for url in re.findall(r'<a href=\\"/epg/(.+?)\\".+?img src=\\"(.+?)\\', r.text)]
    for url,img in test:
        addDir(url,'http://tvim.tv/script/webepg/%s'%url,198,img)
def ipko(name,url):
    r = requests.get(url)
    test = [url for url in re.findall(r'channel_id":.+?,"name_short":"(.+?)","channel_name":".+?","receiver_id":.+?,"icon":"(.+?)"', r.text)]
    for name,img in test:
        addDir(name,'http://ipko.com/epg/admin/programs.php?date=2015-09-19',199,'http://ipko.com/epg/logo/%s'%img)
    test2 = [url for url in re.findall(r'channel_id":.+?,"program_name":"(.+?)","name_short":".+?".+?duration":(.+?),', r.text)]
    for name,runtime in test2:
        addDir('%s - [%smins]'%(name,runtime),'',199,'')
def torrent(url):
        xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_TITLE)
        link = OPEN_URL(url)
        match=re.compile('<a href="(.+?)" rel="bookmark" title="Permanent Link to (.+?)" class="entry-link">\n<div class="entry-image" style="background-image: url\(\'(.+?)\'\)"></div>').findall(link)
        match2=re.compile('<div class="posts-nav-next">\n<a class="btn" href="(.+?)"><span class="btn-text">Older&hellip;</span>').findall(link)
        for url,name,image in match:
            addDir2('%s'%(name),'https://torrentfreak.com/%s'%url,955,'https://torrentfreak.com/%s'%image)
        for url in match2:
            addDir('NEXT >>>','https://torrentfreak.com%s'%url,977,'')
def torrent2(url):
        link = OPEN_URL(url)
        match=re.compile('<div class="entry-content">(.+?)</article>', re.DOTALL).findall(link)
        for text in match:
            showText('read',text.replace('<p>','\n').replace('</p>','').replace('<a href="','[COLOR red]').replace('/">','[/COLOR][COLOR blue]').replace('</a>','[/COLOR]'))
def torrent3(name,image):
            showText('read',name,image)
def showText(heading, text, image):
    id = 10147
    xbmc.executebuiltin('ActivateWindow(%d)' % id)
    xbmc.sleep(100)
    win = xbmcgui.Window(id)
    retry = 50
    while (retry > 0):
        try:
            xbmc.sleep(10)
            retry -= 1
            win.getControl(1).setLabel(heading)
            win.getControl(5).setText(text)
            win.getControl(6).setImage(image)
        except:
            pass
def erase():
    dialog = xbmcgui.Dialog()
    if dialog.yesno("WARNING", 'You Are About To Erase Your List','', "",'NO','YES'):
        LF = open('%s/Links.txt'%addonDir, 'w')
        LF.write('#EXTM3U\n')
        LF.close()
        xbmc.executebuiltin("Container.Refresh")
    else:
        return	

def tvplayer(url):
    r = requests.get(url)
    match=re.compile('"name":"(.+?)".+?"channelId":".+?",".+?","end":".+?","title":"(.+?)","subtitle":.+?,"category".+?,"synopsis":"(.+?)","thumbnail":"(.+?)","blackout":.+?}').findall(r.text)
    for name2,name,synopsis,thumbnail in match:
        name2 = '[LOWERCASE]%s[/LOWERCASE]'%name2
        addDir2('[COLOR yellow]%s[/COLOR] - [B]%s[/B] - [I]%s[/I]'%(name2,name,synopsis),'http://live.tvplayer.com/%s/5/prog_index.m3u8'%name2,10,thumbnail)
def shadow(url):
    link = OPEN_URL(url)
    match=re.compile('#EXTINF:.+?,(.+?)\n(.+?)\n').findall(link)
    for name,url in match:
        addDir2(name,url,10,'')

def worldstar(url):
    r = requests.get(url)
    match=re.compile('"urlVideo": "(.+?)",.+?"imageSrc": "(.+?)",.+?"width": "300",.+?"height": "200",.+?"altImage": "(.+?)"', re.DOTALL).findall(r.text)
    match2=re.compile('<img src="(.+?)" width="222" height="125" alt="(.+?)">', re.DOTALL).findall(r.text)
    match3=re.compile('<a href="(.+?)" class="next" rel="next">next<').findall(r.text)
    addDir('[COLOR green]SEARCH[/COLOR]','http://worldstarhiphop.com/videos/search.php?s=s',4557,'')
    addDir2('[COLOR yellow]----- TRENDING ----[/COLOR]','',10,'')
    for url,image,name in match:
        addDir(name,url,10,image)
    for image,name in match2:
        addDir2(name,'',10,image)
    for url in match3:
        addDir('NEXT >>>>>','http://worldstarhiphop.com%s'%url,4557,'')
def TESTLINKS(url):
    read_timeout = 1.0
    counting = 0
    list = []
    count = 0
    dialog = xbmcgui.Dialog()
    r = requests.get(url)
    dp = xbmcgui.DialogProgress()
    dp.create('STARTING','COUNTING LINKS')
    match=re.compile('#EXTINF:.+?,(.+?)[\n<"].+?http(.+?)[\n#>" ]', re.DOTALL).findall(r.text.replace('\n\n','\n'))
    xbmc.sleep(5000)
    dp.close()
    LF = open('%s/Links.txt'%addonDir, 'a')
    for name,url in match:
        count = count + 1
        count2 = count
    percent = (count2 * 100)/count
    dp.create('FOUND %s'%(count2),'DONE COUNTING')
    xbmc.sleep(2000)
    dp.update(percent,'FOUND %s'%(count2))
    for name,url in match:
        try:
            try:
                name =  name
                url = "http"+url
                count = count - 1
                r = requests.get(url, timeout=(5.0, read_timeout), allow_redirects=True)
                stat = r.reason
                stat2 = stat+' '+name
                if r.reason == 'OK':
                    dp.update(percent,'[B]Testing Link[/B] - [COLOR yellow]%s[/COLOR] [B]Result[/B] - [COLOR green]%s[/COLOR]'%(count,stat))
                    addDir2("[COLOR green]WORKING[/COLOR] - %s"%name,url,10,'')
                    list.append(stat)
                if dp.iscanceled(): break;
                else:
                    dp.update(percent,'[B]Testing Link[/B] - [COLOR yellow]%s[/COLOR] [B]Result[/B] - [COLOR red]%s[/COLOR]'%(count,stat))

            except requests.exceptions.ReadTimeout as e:
                    continue
        except:
            pass
    ret = dialog.select('Working',list)
    dp.close()
    dialog = xbmcgui.Dialog()
    dialog.ok("SCAN COMPLETE", "TESTING IS COMPLETE")
    return

def TESTLINKS2(url):
    read_timeout = 1.0
    counting = 0
    list = []
    count = 0
    dialog = xbmcgui.Dialog()
    link = OPEN_URL(url)
    dp = xbmcgui.DialogProgress()
    dp.create('STARTING','COUNTING LINKS')
    match=re.compile('#.+?,(.+?)[<\n"].+?http(.+?)[<\n#"\s ]', re.DOTALL).findall(link)
    xbmc.sleep(5000)
    dp.close()
    for name,url in match:
        count = count + 1
        count2 = count
    dp.create('FOUND %s'%(count),'DONE COUNTING')
    if dp.iscanceled():
        dp.close()
        return
    xbmc.sleep(2000)
    dp.update(count,'FOUND %s'%(count2))
    for name,url in match:
        try:
            try:
                name =  name
                url = "http"+url
                count = count - 1
                r = requests.get(url, timeout=(10.0, read_timeout), allow_redirects=True)
                stat = r.reason
                stat2 = stat+' '+name
                if r.reason == 'OK':
                    dp.update(count,'[B]Testing Link[/B] - [COLOR yellow]%s[/COLOR] [B]Result[/B] - [COLOR green]%s[/COLOR]'%(count,stat))
                    addDir2("[COLOR green]WORKING[/COLOR]%s"%name,url,10,'')
                    list.append(stat)

                if dp.iscanceled():
                        dp.close()
                        return
                else:
                    dp.update(count,'[B]Testing Link[/B] - [COLOR yellow]%s[/COLOR] [B]Result[/B] - [COLOR red]%s[/COLOR]'%(count,stat))

            except requests.exceptions.ReadTimeout as e:
                    continue
        except:
            pass
    dialog.ok("SCAN COMPLETE", "TESTING IS COMPLETE")
    ret = dialog.select('Working',list)
    dp.close()
    dialog = xbmcgui.Dialog()
    return

def INDIA(url):
        xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_TITLE)
        link = OPEN_URL(url)
        match=re.compile('href="(.+?)" title="(.+?)">\n.+?<img src="(.+?)"').findall(link)
        for url,title,image in match:
            addDir(title,url,4112,image)
def SHOOT(url):
        link = OPEN_URL(url)
        match=re.compile('url\((.+?)\).+?<p style="font-size:10px; line-height:20px; overflow:hidden; height:18px; margin:-5px 0px 0px 0px; padding:0px 2px;">(.+?)<.+?onclick="document.location.href=\'(.+?)\'', re.DOTALL).findall(link)
        match2=re.compile('<td class="time"><p>(.+?)<.+?<td class="title"><p><a href=".+?" class="programsummary" programid=".+?">(.+?)<', re.DOTALL).findall(link)
        match3=re.compile('h3 class="epg">.+?<span programid=".+?"> </span><a href=".+?" class="programsummary" programid=".+?">(.+?)<', re.DOTALL).findall(link)
        for url,name,url in match:
            addDir(name,'http://en.timefor.tv%s'%url,4117,'http://en.timefor.tv%s'%url)
        for name in match3:
            addDir('[COLOR yellow]Now Playing [/COLOR]%s '%(name),'',4117,'')
        for name,name2 in match2:
            addDir('%s %s'%(name,name2),'',4117,'')
def SHOOTs(url):
        searchStr = ''
        keyboard = xbmc.Keyboard(searchStr, 'Search')
        keyboard.doModal()
        searchStr=keyboard.getText()
        link = OPEN_URL('%s%s'%(url,searchStr))
        match2=re.compile('<td class="time"><p>(.+?)<.+?<td class="title"><p><a href=".+?" class="programsummary" programid=".+?">(.+?)<|<td class="logo">.+?<a href="/listings/(.+?)"><img src="(.+?)"', re.DOTALL).findall(link)
        for name,name2,name3,image in match2:
            addDir('%s %s %s'%(name3.replace('-',' '),name,name2),'',4117,image)

def ie(url):
    r = requests.get(url)
    match=re.compile('data-original="(.+?)"  title="(.+?)".+?title="(.+?)".+?<em>(.+?)</em>', re.DOTALL).findall(r.content)
    for image,name,now,timee in match:
        addDir('[B]%s[/B] - [COLOR yellow]NOW:[/COLOR] %s - 	%s'%(name,now.replace('View','').replace('programme details',''),timee),'',191,'http:%s'%image)
def ie2(url):
    r = requests.get(url)
    match=re.compile('languageCode":"(.+?)","deviceCode":".+?","locationId":".+?","channelNumber":.+?,"stationSchedules":\[{"station":{"id":"(.+?)","countryCode":"(.+?)","locationId":"(.+?)","title":"(.+?)"').findall(r.content)
    match2=re.compile('"startTime":\d\d\d\d\d\d\d(\d\d)(\d\d)(\d\d),"endTime":.+?,"stationId":".+?","imi":".+?","program":{"id":"crid:.+?","title":"(.+?)","description":"(.+?)"').findall(r.content)
    for lan,id,CC,LID,name in match:
        addDir('%s'%(name),'https://web-api-salt.horizon.tv/oesp/api/%s/%s/web/listings?range=1-12&byStationId=%s&byLocationId=%s'%(CC,lan,id,LID),192,'http:%s'%name)
    for start,start1,start2,name,de in match2:
        addDir('[%s:%s:%s] - [B]%s[/B] - [I]%s[/I]'%(start,start1,start2,name,de),'',192,'http:%s'%name)
def VIAT(url):
        xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_TITLE)
        link = OPEN_URL(url)
        match=re.compile('class="station">(.+?)<div class=".+?"></div></a><div class="grid-col"><div class="grid.+?"><div class=".+?"><a href="(.+?)" class="prog-title" data-time="(.+?)">(.+?)</a>').findall(link)
        match2=re.compile('<img src="(.+?)" alt="(.+?)" class="pic">').findall(link)
        match3=re.compile('<img src=\\"(.+?)" alt=\\"(.+?)"').findall(link)
        for channel,url,dandt,title in match:
            addDir('%s  - [COLOR yellow]Now[/COLOR] - %s  - %s'%(channel,title,dandt),url,4113,'')
        for image,name in match2:
            addDir(name,'',4113,image)
        for image,name in match3:
            addDir(name,'',4113,image)
def PG(url):
        xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_TITLE)
        link = OPEN_URL(url)
        match=re.compile('<img src="/resources/logos_canais/(.+?)_thumb9\.png" class="resp-image" />.+?<p class="name">(.+?)</p>', re.DOTALL).findall(link)
        match2=re.compile('<img alt="(.+?)" src="/SiteCollectionImages/Canais_logos/(.+?)"', re.DOTALL).findall(link)
        for name,now in match:
            addDir('%s  - [COLOR yellow]Now[/COLOR] - %s '%(name.replace('_',' '),now),'http://cabovisao.pt/%s'%name,4114,'http://cabovisao.pt/resources/logos_canais/%s.png'%(name))
        for name,image in match2:
            addDir('%s '%(name),'',4114,'http://meogo.meo.pt/SiteCollectionImages/Canais_logos/%s'%(image))
def RO(url):
        xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_TITLE)
        link = OPEN_URL(url)
        match=re.compile('<a href="http://programetv.program24.ro/post/.+?" class="station_link">(.+?)</a></td><td colspan=".+?" class=".+?"><a href=".+?" title="(.+?)"').findall(link)
        for channel,now in match:
            addDir('%s  - [COLOR yellow]Now[/COLOR]  -  %s'%(channel,now),'',4115,'')

#romainain http://port.ro/horizontal_tv/req.php?i_link=http://port.ro/pls/w/tv_xml.events_xml?i_area_id=1&i_channel_id=10282&i_date_from=201509130500&i_date_to=201509131600&i_debug=no
def INDIA2(url):
        link = OPEN_URL(url)
        match=re.compile('(\d\d:\d\d)<sup class="ap">(.+?)</sup>\n.+?</b>\n.+?</td>\n.+?<td class="resultThumb">\n.+?\n.+?<a href="(.+?)" title="(.+?)">\n.+?\n.+?<img src="(.+?)"/>').findall(link)
        for time3,time4,url,name,image in match:
            addDir('[COLOR yellow]%s%s[/COLOR]  - %s   '%(time3,time4,name),url,4112,image)
def LOTTEY(url):
            link = OPEN_URL(url)
            match=re.compile('<h2>(.+?)<span class="draw-date">(.+?)</span>.+?<div class="drawn-number">(.+?)<.+?<div class="drawn-number">(.+?)<.+?<div class="drawn-number">.+?<div class="drawn-number">(.+?)<.+?<div class="drawn-number">(.+?)<.+?<div class="drawn-number">(.+?)<.+?<div class="drawn-number">(.+?)<.+?<div class="drawn-number">(.+?)<').findall(link)
            for name,drawdate,ball1,ball2,ball3,ball4,ball5,bonus in match:
                addDir('%s%s%s%s%s%s%s'%(name,drawdate,ball1,ball2,ball3,ball4,ball5,bonus),url,5679,'')
def TVGUIDEUS(name):
        link = OPEN_URL(url)
        match=re.compile('parent":{"title":"(.+?)","id":"(.+?)"}.+?".+?"title":"(.+?)".+?"title":"(.+?)".+?"image":"(.+?)"').findall(link)
        for channel,id,next,now,image in match:
            addDir('%s - [COLOR gold]Now[/COLOR] - %s [COLOR brown]Next[/COLOR] - %s  '%(channel,now,next),'https://voila.metabroadcast.com/1.0/schedules/?annotations=broadcasts,locations,description&apiKey=public:64a03c33f9a64c2b80b6f58cd218e5c8&from=now&count=10&id=%s'%id,61,image)
def TVGUIDEUS2(url):
        link = OPEN_URL(url)
        match=re.compile('locationId":".+?","title":"(.+?)".+?"width":59,"height":20,"url":"(.+?)"').findall(link)
        for name,image in match:
            addDir(name,'',61,image)
def SEARCHCAT(url):
            addDir2('[COLOR yellow]MEGA SEARCH BY PIPCAN[/COLOR]','',1000,'')
            addDir2('[COLOR green]Still Work In Progrss Some Dont Work Fully[/COLOR]','',1000,'')
            addDir('[COLOR green]100% [/COLOR]Search Navix','http://www.navixtreme.com/playlist/search/video/',735,'http://media.navi-x.org/images/logos/search.png')
            addDir('[COLOR green]100% [/COLOR]Search letwatch.us','http://letwatch.us/?op=search&k=',3,'http://letwatch.us/images/logo.png')
            addDir('[COLOR green]100% [/COLOR]Search Vodlocker','http://vodlocker.com/?op=search&k=',5,'http://vodlocker.com/images/logo.png')
            addDir('[COLOR green]100% [/COLOR]Search cloudy.ec','http://www.cloudy.ec/search?search=',6,'http://www.cloudy.ec/img/logo.png')
            addDir('[COLOR green]100% [/COLOR]Search Bing Videos','http://www.msn.com/en-us/video/searchresults?q=',37,'http://microsoft-news.com/wp-content/uploads/2014/09/Bing-logo-1.jpg')
            addDir('[COLOR green]100% [/COLOR]Search PASTEBIN','https://www.googleapis.com/customsearch/v1element?key=AIzaSyCVAXiUzRYsML1Pv6RwSG1gunmMikTzQqY&rsz=filtered_cse&num=20&hl=en&prettyPrint=false&source=gcsc&gss=.com&sig=56f70d816baa48bdfe9284ebc883ad41&cx=013305635491195529773:0ufpuq-fpt0&sort=date&q=',503,'http://pastebin.com/i/fb2.jpg')
            addDir('[COLOR red]Search Only [/COLOR]Search ALL My Videos .Net','https://www.googleapis.com/customsearch/v1element?key=AIzaSyCVAXiUzRYsML1Pv6RwSG1gunmMikTzQqY&rsz=small&num=20&hl=en&prettyPrint=false&source=gcsc&gss=.com&sig=56f70d816baa48bdfe9284ebc883ad41&cx=partner-pub-2526982841387487:3428957054&googlehost=www.google.com&gs_l=partner.12...0.0.1.20932.0.0.0.0.0.0.0.0..0.0.gsnos%2Cn%3D13...0.0jj1..1ac..25.partner..0.0.0.&callback=google.search.Search.apiary18154&q=',5055,'http://allmyvideos.net/images/amvlogo-200-min.png')
            addDir('[COLOR green]100% [/COLOR]Search MoviShare.NET','https://www.googleapis.com/customsearch/v1element?key=AIzaSyCVAXiUzRYsML1Pv6RwSG1gunmMikTzQqY&rsz=small&num=20&hl=en&prettyPrint=false&source=gcsc&gss=.com&sig=56f70d816baa48bdfe9284ebc883ad41&cx=partner-pub-2526982841387487:4545021852&googlehost=www.google.com&oq=hell&gs_l=partner.3...1800.2471.0.2719.0.0.0.0.0.0.0.0..0.0.gsnos%2Cn%3D13...0.672j160640j4..1ac.1.25.partner..0.0.0.&callback=google.search.Search.apiary16046&q=',5055,'http://allmyvideos.net/images/amvlogo-200-min.png')
            addDir('[COLOR red]Search Only [/COLOR]Search 180 Upload','https://www.googleapis.com/customsearch/v1element?key=AIzaSyCVAXiUzRYsML1Pv6RwSG1gunmMikTzQqY&rsz=small&num=20&hl=en&prettyPrint=false&source=gcsc&gss=.com&sig=56f70d816baa48bdfe9284ebc883ad41&cx=partner-pub-2526982841387487:5103425050&googlehost=www.google.com&gs_l=partner.3...4025.4624.0.4785.0.0.0.0.0.0.0.0..0.0.gsnos%2Cn%3D13...0.599j105313j5..1ac.1.25.partner..0.0.0.&callback=google.search.Search.apiary12175&q=',5055,'http://allmyvideos.net/images/amvlogo-200-min.png')
            addDir('[COLOR green]100% [/COLOR]Search TV Online Streams','http://www.tvonlinestreams.com/?s=',102,'')
            addDir('[COLOR green]100% [/COLOR]Search Filmover','http://iptv.filmover.com/?s=',203,'')
            addDir('[COLOR red]Search Only [/COLOR]Search XVIDSTAGE','https://www.googleapis.com/customsearch/v1element?key=AIzaSyCVAXiUzRYsML1Pv6RwSG1gunmMikTzQqY&rsz=small&num=20&hl=en&prettyPrint=false&source=gcsc&gss=.com&sig=56f70d816baa48bdfe9284ebc883ad41&cx=partner-pub-2526982841387487:3986618654&googlehost=www.google.com&gs_l=partner.3...1135.1806.0.1935.0.0.0.0.0.0.0.0..0.0.gsnos%2Cn%3D13...0.656j110976j5..1ac.1.25.partner..0.0.0.&callback=google.search.Search.apiary13567&q=',5055,'')
            addDir('[COLOR green]100% [/COLOR]Search Gorillavid','https://www.googleapis.com/customsearch/v1element?key=AIzaSyCVAXiUzRYsML1Pv6RwSG1gunmMikTzQqY&rsz=small&num=20&hl=en&prettyPrint=false&source=gcsc&gss=.com&sig=56f70d816baa48bdfe9284ebc883ad41&cx=partner-pub-2526982841387487:7638089059&&googlehost=www.google.com&gs_l=partner.3...1478.2143.0.2302.0.0.0.0.0.0.0.0..0.0.gsnos%2Cn%3D13...0.656j112896j5..1ac.1.25.partner..0.0.0.&callback=google.search.Search.apiary10799&q=',5055,'')
            addDir('[COLOR green]100% [/COLOR]Search Filhoot','https://www.googleapis.com/customsearch/v1element?key=AIzaSyCVAXiUzRYsML1Pv6RwSG1gunmMikTzQqY&rsz=small&num=20&hl=en&prettyPrint=false&source=gcsc&gss=.com&sig=56f70d816baa48bdfe9284ebc883ad41&cx=partner-pub-2526982841387487:7777689852&googlehost=www.google.com&gs_l=partner.12...0.0.1.82212.0.0.0.0.0.0.0.0..0.0.gsnos%2Cn%3D13...0.0jj1..1ac..25.partner..0.0.0.&callback=google.search.Search.apiary14624&q=',5055,'')
            addDir('[COLOR green]100% [/COLOR]Search FlashX','https://www.googleapis.com/customsearch/v1element?key=AIzaSyCVAXiUzRYsML1Pv6RwSG1gunmMikTzQqY&rsz=small&num=20&hl=en&prettyPrint=false&source=gcsc&gss=.com&sig=56f70d816baa48bdfe9284ebc883ad41&cx=partner-pub-2526982841387487:4684622655&googlehost=www.google.com&gs_l=partner.3...2228.2922.0.3067.0.0.0.0.0.0.0.0..0.0.gsnos%2Cn%3D13...0.696j125120j5..1ac.1.25.partner..0.0.0.&callback=google.search.Search.apiary2894&q=',5055,'')
            addDir('[COLOR green]100% [/COLOR]Search Filnuke','https://www.googleapis.com/customsearch/v1element?key=AIzaSyCVAXiUzRYsML1Pv6RwSG1gunmMikTzQqY&rsz=small&num=20&hl=en&prettyPrint=false&source=gcsc&gss=.com&sig=56f70d816baa48bdfe9284ebc883ad41&cx=partner-pub-2526982841387487:9254423052&googlehost=www.google.com&gs_l=partner.3...1165.1836.0.1957.0.0.0.0.0.0.0.0..0.0.gsnos%2Cn%3D13...0.648j105280j5..1ac.1.25.partner..0.0.0.&callback=google.search.Search.apiary18526&q=',5055,'')
            addDir('[COLOR green]100% [/COLOR]Search Beststreams','http://bestreams.net/?op=search&k=',5055,'')
            addDir('[COLOR red]Search Only [/COLOR]Search Nos Video','https://www.googleapis.com/customsearch/v1element?key=AIzaSyCVAXiUzRYsML1Pv6RwSG1gunmMikTzQqY&rsz=small&num=20&hl=en&prettyPrint=false&source=gcsc&gss=.com&sig=56f70d816baa48bdfe9284ebc883ad41&cx=partner-pub-2526982841387487:7498488250&googlehost=www.google.com&o&gs_l=partner.12...0.0.2.8454.0.0.0.0.0.0.0.0..0.0.gsnos%2Cn%3D13...0.0..1ac..25.partner..0.0.0.&callback=google.search.Search.apiary4775&nocache=1441486920204&q=',5055,'')
            addDir('[COLOR green]100% [/COLOR]Search nowvideo','https://www.googleapis.com/customsearch/v1element?key=AIzaSyCVAXiUzRYsML1Pv6RwSG1gunmMikTzQqY&rsz=small&num=20&hl=en&prettyPrint=false&source=gcsc&gss=.com&sig=56f70d816baa48bdfe9284ebc883ad41&cx=partner-pub-2526982841387487:8975221455&googlehost=www.google.com&gs_l=partner.3...1363.2322.0.3779.0.0.0.0.0.0.0.0..0.0.gsnos%2Cn%3D13...0.927j217665j5..1ac.1.25.partner..0.0.0.&callback=google.search.Search.apiary373&nocache=1441490987165&q=',5055,'')
            addDir('[COLOR green]100% [/COLOR]Search promtfile','https://www.googleapis.com/customsearch/v1element?key=AIzaSyCVAXiUzRYsML1Pv6RwSG1gunmMikTzQqY&rsz=small&num=20&hl=en&prettyPrint=false&source=gcsc&gss=.com&sig=56f70d816baa48bdfe9284ebc883ad41&cx=partner-pub-2526982841387487:2928687859&googlehost=www.google.com&gs_l=partner.3...4542.5525.0.5654.0.0.0.0.0.0.0.0..0.0.gsnos%2Cn%3D13...0.951j258993j5..1ac.1.25.partner..0.0.0.&callback=google.search.Search.apiary10461&nocache=1441490844196&q=',5055,'')
            addDir('[COLOR green]100% [/COLOR]Search sharedsix','https://www.googleapis.com/customsearch/v1element?key=AIzaSyCVAXiUzRYsML1Pv6RwSG1gunmMikTzQqY&rsz=small&num=20&hl=en&prettyPrint=false&source=gcsc&gss=.com&sig=56f70d816baa48bdfe9284ebc883ad41&cx=partner-pub-2526982841387487:5882154254&googlehost=www.google.com&gs_l=partner.3...1403.2138.0.2268.0.0.0.0.0.0.0.0..0.0.gsnos%2Cn%3D13...0.736j142848j5..1ac.1.25.partner..0.0.0.&callback=google.search.Search.apiary16986&nocache=1441490770544&q=',5055,'')
            addDir('[COLOR red]Search Only [/COLOR]Search thevideo','https://www.googleapis.com/customsearch/v1element?key=AIzaSyCVAXiUzRYsML1Pv6RwSG1gunmMikTzQqY&rsz=small&num=20&hl=en&prettyPrint=false&source=gcsc&gss=.com&sig=56f70d816baa48bdfe9284ebc883ad41&cx=partner-pub-2526982841387487:1312353853&gs_l=partner.3...1557.1557.0.1925.0.0.0.0.0.0.0.0..0.0.gsnos%2Cn%3D13...0.0jj1..1ac.1.25.partner..0.0.0.&callback=google.search.Search.apiary11714&nocache=1441490528350&q=',5055,'')
            addDir('[COLOR red]Search Only [/COLOR]Search weehd',' https://www.googleapis.com/customsearch/v1element?key=AIzaSyCVAXiUzRYsML1Pv6RwSG1gunmMikTzQqY&rsz=small&num=20&hl=en&prettyPrint=false&source=gcsc&gss=.com&sig=56f70d816baa48bdfe9284ebc883ad41&cx=partner-pub-2526982841387487:7280387058&googlehost=www.google.com&gs_l=partner.3...1022.1821.0.3431.0.0.0.0.0.0.0.0..0.0.gsnos%2Cn%3D13...0.775j191121j5..1ac.1.25.partner..0.0.0.&callback=google.search.Search.apiary4756&nocache=1441489115347&q=',5055,'')
            addDir('[COLOR green]100% [/COLOR]Search vidbull',' https://www.googleapis.com/customsearch/v1element?key=AIzaSyCVAXiUzRYsML1Pv6RwSG1gunmMikTzQqY&rsz=small&num=20&hl=en&prettyPrint=false&source=gcsc&gss=.com&sig=56f70d816baa48bdfe9284ebc883ad41&cx=partner-pub-2526982841387487:3552639851&googlehost=www.google.com&gs_l=partner.3...1357.2204.0.2317.0.0.0.0.0.0.0.0..0.0.gsnos%2Cn%3D13...0.824j199968j5..1ac.1.25.partner..0.0.0.&callback=google.search.Search.apiary15372&nocache=1441489162158&q=',5055,'')
            addDir('[COLOR red]Search Only [/COLOR]Search videomega','https://www.googleapis.com/customsearch/v1element?key=AIzaSyCVAXiUzRYsML1Pv6RwSG1gunmMikTzQqY&rsz=small&num=20&hl=en&prettyPrint=false&source=gcsc&gss=.com&sig=56f70d816baa48bdfe9284ebc883ad41&cx=partner-pub-2526982841387487:9108890656&gs_l=partner.12...2781.2781.1.3942.0.0.0.0.0.0.0.0..0.0.gsnos%2Cn%3D13...0.0jj1..1ac.1.25.partner..0.0.0.&callback=google.search.Search.apiary7206&nocache=1441489072515&q=',5055,'')
            addDir('[COLOR green]100%[/COLOR]Search videoveed','https://www.googleapis.com/customsearch/v1element?key=AIzaSyCVAXiUzRYsML1Pv6RwSG1gunmMikTzQqY&rsz=small&num=20&hl=en&prettyPrint=false&source=gcsc&gss=.com&sig=56f70d816baa48bdfe9284ebc883ad41&cx=partner-pub-2526982841387487:2649486255&googlehost=www.google.com&gs_l=partner.3...1327.2063.0.2207.0.0.0.0.0.0.0.0..0.0.gsnos%2Cn%3D13...0.728j144576j5..1ac.1.25.partner..0.0.0.&callback=google.search.Search.apiary17700&nocache=1441488422216&q=',5055,'')
            addDir('[COLOR red]Search Only [/COLOR]Search vimeo',' https://www.googleapis.com/customsearch/v1element?key=AIzaSyCVAXiUzRYsML1Pv6RwSG1gunmMikTzQqY&rsz=small&num=20&hl=en&prettyPrint=false&source=gcsc&gss=.com&sig=56f70d816baa48bdfe9284ebc883ad41&cx=partner-pub-2526982841387487:4399489457&googlehost=www.google.com&gs_l=partner.3...1340.1963.0.2100.0.0.0.0.0.0.0.0..0.0.gsnos%2Cn%3D13...0.616j96704j5..1ac.1.25.partner..0.0.0.&callback=google.search.Search.apiary17326&nocache=1441488697093&q=',5055,'')
            addDir('[COLOR red]Search Only [/COLOR]Search vk','https://www.googleapis.com/customsearch/v1element?key=AIzaSyCVAXiUzRYsML1Pv6RwSG1gunmMikTzQqY&rsz=small&num=20&hl=en&prettyPrint=false&source=gcsc&gss=.com&sig=56f70d816baa48bdfe9284ebc883ad41&cx=partner-pub-2526982841387487:7352955859&googlehost=www.google.com&gs_l=partner.12...0.0.1.46617.0.0.0.0.0.0.0.0..0.0.gsnos%2Cn%3D13...0.0jj1..1ac..25.partner..0.0.0.&callback=google.search.Search.apiary87&nocache=1441488557076&q=',5055,'')
            addDir('[COLOR green]100% [/COLOR]Search youwatch','https://www.googleapis.com/customsearch/v1element?key=AIzaSyCVAXiUzRYsML1Pv6RwSG1gunmMikTzQqY&rsz=small&num=20&hl=en&prettyPrint=false&source=gcsc&gss=.com&sig=56f70d816baa48bdfe9284ebc883ad41&cx=partner-pub-2526982841387487:8416818254&googlehost=www.google.com&gs_l=partner.3...1197.2570.0.2749.0.0.0.0.0.0.0.0..0.0.gsnos%2Cn%3D13...0.1367j752721j5..1ac.1.25.partner..0.0.0.&callback=google.search.Search.apiary15167&nocache=1441488504168&q=',5055,'')
def torrentcat():
            addDir('[COLOR brown]100% [/COLOR]Torrent TV','http://torrent-tv.gr/sport.php',5678,'http://media.navi-x.org/images/logos/search.png')

def GSEARCH(name,url):
        if name == 'NEXT >>>':
            link = OPEN_URL(url)
            match=re.compile('titleNoFormatting":"(.+?)","unescapedUrl":"(.+?)"', re.DOTALL).findall(link)
            match2=re.compile('background-image:url\((.+?)\);"><span>(.+?)</span></a></TD>\n<TD valign=top>\n<div class="link"><a href="(.+?)">(.+?)</a></div>').findall(link)
            counts=re.compile('"resultCount":"(.+?)"').findall(link)
            nextpage=re.compile("<a href='(.+?)'>Next").findall(link)
            for name in counts:
                addDir2('FOUND %s MATCHS'%(counts),'count',4,'')
            for name,url in match:
                addDir2(name,'%s/'%url.replace('-640x360.html','').replace('embed-',''),4,'')
            for image,time,url,name in match2:
                addDir2('%s - %s'%(name,time),url,4,'%s'%(image))
            for url in nextpage:
                addDir('NEXT >>>',url.replace('&amp;','&'),5055,'')
        else:
            searchStr = ''
            keyboard = xbmc.Keyboard(searchStr, 'Search')
            keyboard.doModal()
            searchStr=keyboard.getText()
            link = OPEN_URL('%s%s'%(url,searchStr))
            counts=re.compile('"resultCount":"(.+?)"').findall(link)
            match=re.compile('titleNoFormatting":"(.+?)","unescapedUrl":"(.+?)"', re.DOTALL).findall(link)
            match2=re.compile('background-image:url\((.+?)\);"><span>(.+?)</span></a></TD>\n<TD valign=top>\n<div class="link"><a href="(.+?)">(.+?)</a></div>').findall(link)
            nextpage=re.compile("<a href='(.+?)'>Next").findall(link)
            for name in counts:
                addDir2('[COLOR yellow]FOUND %s MATCHS[/COLOR]'%(name),'count',4,'')
            for name,url in match:
                addDir2(name,'%s/'%url.replace('-640x360.html','').replace('embed-',''),4,'')
            for image,time,url,name in match2:
                addDir2('%s - %s'%(name,time),url,4,'%s'%(image))
            for url in nextpage:
                addDir('NEXT >>>',url.replace('&amp;','&'),5055,'')
def CRAVING(url):
            link = OPEN_URL(url)
            match=re.compile('<li><a href="(.+?)">(.+?)</a>', re.DOTALL).findall(link)
            match2=re.compile('<li>(.+?)<a href="(.+?)">(.+?)</a></li>').findall(link)
            match3=re.compile('<b>(.+?)</b></span><b id=\'ko\' data-iframe=\'<iframe src="(.+?)"').findall(link)
            for url,name in match:
                addDir(name,url,5679,'')
            addDir('[COLOR yellow]----------------- EPISODES BELLOW----------------------------[/COLOR]','hhh',5679,'')
            for number,url,name in match2:
                addDir('%s - %s'%(number,name),'%s'%url,5679,'')
            for name,url in match3:
                addDir2(name,url,4,'')
def skysate(url):
            addDir('[COLOR gold]CLICK HERE TO SORT OUT DEAD LINKS[/COLOR]',url,1456,'')
            link = OPEN_URL(url)
            match=re.compile('<div class=\'item-title\'><a href=\'(.+?)\'>(.+?)<', re.DOTALL).findall(link)
            match2=re.compile('#EXTINF:.+?,(.+?)<.+?http(.+?)<', re.DOTALL).findall(link)
            for url,name in match:
                addDir('%s'%(name),'%s'%url,182,'')
            for name,url in match2:
                addDir('%s'%(name),'http%s'%url,10,'')
def contact():
    dialog = xbmcgui.Dialog()
    ret = dialog.select('Were Do You Want It Sent', ['Request A Website', 'Request A Section', 'Everything Else'])
    if ret == 1:
        dialog.input('Enter secret code', type=xbmcgui.INPUT_ALPHANUM)
    if ret == 2:
        dialog.input('Enter secret code', type=xbmcgui.INPUT_ALPHANUM)
    if ret == 3:
        dialog.input('Enter secret code', type=xbmcgui.INPUT_ALPHANUM)
def addons(url):
    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_TITLE)
    addDir2('[COLOR yellow]MEGA SEARCH BY PIPCAN[/COLOR]','',1000,'')
    addDir('solved.no-issue.ca','http://solved.no-issue.ca/',1656,'')
    addDir('xbmc.digiwizard.net','http://www.xbmc.digiwizard.net/repo/',1656,'')
    addDir('wtyczki.iptvlive.org','http://wtyczki.iptvlive.org',1656,'')
    addDir('Full Super Repo','http://ftp.acc.umu.se/mirror/addons.superrepo.org/',1656,'')
    addDir('Full Super Repo BACK UP','http://mirror.cinosure.com/superrepo/',1656,'')
    addDir('XBMC.ORG','http://ftp.acc.umu.se/mirror/xbmc.org/',1656,'')
    addDir('computertechs.org','http://computertechs.org/xbmc/',1656,'')
    addDir('The Little Black Box','http://cloud.thelittleblackbox.co.uk/repo/zips/',1656,'')
    addDir('xstream-addon.square7','http://xstream-addon.square7.ch/repo',1656,'')
    addDir('iptvip.info','http://iptvip.info/repo/',1656,'')
    addDir('kodi.media-guru.com.au','http://kodi.media-guru.com.au/',1656,'')
    addDir('kodi.shivuthegreat','http://kodi.shivuthegreat.com/Video/',1656,'')
    addDir('gerrymoth.co.uk/KODI','https://home.pilsfree.net/chudy/',1656,'')
    addDir('gerrymoth.co.uk','http://gerrymoth.co.uk/KODI/',1656,'')
    addDir('srp.nu','http://srp.nu/',1656,'')
    addDir('xfinity.xunitytalk.com','http://xfinity.xunitytalk.com',1656,'')
    addDir('srp.nu','http://srp.nu',1656,'')
    addDir('i.totalxbmc.tv/COLOR]','http://i.totalxbmc.tv',1656,'')
    addDir('solved.no-issue.ca','http://solved.no-issue.ca',1656,'')
    addDir('xbmc.aminhacasadigital.com','http://xbmc.aminhacasadigital.com',1656,'')
    addDir('install.kaosbox.tv','http://install.kaosbox.tv',1656,'')
    addDir('kodi.metalkettle.co','http://kodi.metalkettle.co',1656,'')
    addDir('jas0npc.pcriot.com','http://jas0npc.pcriot.com',1656,'')
    addDir('halow.x10.bz','http://halow.x10.bz',1656,'')
    addDir('www.kodicustombuilds.com/wizard','http://www.kodicustombuilds.com/wizard/',1656,'')
    addDir('entertainmentrepo.x10.bz','http://entertainmentrepo.x10.bz',1656,'')
    addDir('theyidsrepo.x10host.com','http://theyidsrepo.x10host.com',1656,'')
    addDir('tecbox.tv/repo/install','http://tecbox.tv/repo/install/',1656,'')
    addDir('shadowcrew.info/shadows','http://shadowcrew.info/shadows/',1656,'')
    addDir('chrisbkodi.uk/kodi','http://chrisbkodi.uk/kodi/',1656,'')
    addDir('muckys.kodimediaportal.ml','http://muckys.kodimediaportal.ml',1656,'')
    addDir('iwillfolo.com/iwf','http://iwillfolo.com/iwf/',1656,'')
    addDir('add.taffymc.com','http://add.taffymc.com',1656,'')
    addDir('upgrades.montrealandroidtv.com','http://upgrades.montrealandroidtv.com',1656,'')
    addDir('transform.mega-tron.tv','http://transform.mega-tron.tv',1656,'')
    addDir('dan-elmore.co.uk/kodi','http://dan-elmore.co.uk/kodi/',1656,'')
    addDir('Http//install.tvaddons.nl','http://Http//install.tvaddons.nl/',1656,'')
    addDir('renegades.x10host.com/addons','http://renegades.x10host.com/addons/',1656,'')
    addDir('repository.bbtsip.tv/repo','http://repository.bbtsip.tv/repo/',1656,'')
    addDir('tugafree.hostei.com','http://tugafree.hostei.com',1656,'')
    addDir('prozone.getxbmc.com','http://prozone.getxbmc.com',1656,'')
    addDir('njmweb.we.bs/NJMC','http://njmweb.we.bs/NJMC/',1656,'')
    addDir('lihattv.com/install','http://lihattv.com/install/',1656,'')
    addDir('zeusrepo.com/zeus','http://zeusrepo.com/zeus/',1656,'')
    addDir('www.vectordroid.com/repo','http://www.vectordroid.com/repo/',1656,'')
    addDir('diavolettotv-repo.16mb.com','http://diavolettotv-repo.16mb.com',1656,'')
    addDir('cwal.me/xbmc/addons','http://cwal.me/xbmc/addons/',1656,'')
    addDir('mrtvbox.net/support','http://mrtvbox.net/support/',1656,'')
    addDir('thaisatellite.tv/repo','http://thaisatellite.tv/repo/',1656,'')
    addDir('www.xbmcmods.com','http://www.xbmcmods.com/',1656,'')
    addDir('droidtv4free.partypixxphotobooth.com','http://droidtv4free.partypixxphotobooth.com/',1656,'')
    addDir('cesego.com','http://cesego.com',1656,'')
    addDir('www.xbmc.digiwizard.net/repo','http://www.xbmc.digiwizard.net/repo/',1656,'')
    addDir('cynagen.com/xbmcapp/Addons/','http://cynagen.com/xbmcapp/Addons/',1656,'')
    addDir('dmdsoftware.net/repository.ddurdle','http://dmdsoftware.net/repository.ddurdle/',1656,'')
    addDir('www.we-fix-it.ca/xbmc/','http://www.we-fix-it.ca/xbmc/',1656,'')
    addDir('jetstreambox.com/repo','http://jetstreambox.com/repo/',1656,'')
    addDir('wanttowatchtv.com/addons','http://wanttowatchtv.com/addons/',1656,'')
    addDir('viewstationusa.org/vs/XbmcRepos','http://viewstationusa.org/vs/XbmcRepos/',1656,'')
    addDir('xbmc.kestouf.com/~XBMC/addons/Files','http://xbmc.kestouf.com/~XBMC/addons/Files/',1656,'')
    addDir('xbmc-czech.sourceforge.net/addons','http://xbmc-czech.sourceforge.net/addons/',1656,'')
    addDir('147.194.93.20:8080/xbmc','http://147.194.93.20:8080/xbmc/',1656,'')
    addDir('web.ist.utl.pt/~ist157804/xbmc','http://web.ist.utl.pt/~ist157804/xbmc/',1656,'')
    addDir('xbmc.channaa.com','http://xbmc.channaa.com/',1656,'')
    addDir('xbmcil.com/addons','http://xbmcil.com/addons/',1656,'')
    addDir('wtyczki.iptvlive.org','http://wtyczki.iptvlive.org/',1656,'')
    addDir('www.bruggers.net/repo','http://www.bruggers.net/repo/',1656,'')
    addDir('digsim.homelinux.org/xbmc/code','http://digsim.homelinux.org/xbmc/code/',1656,'')
    addDir('web-develop.ca/kodi/20150328-repositories','http://web-develop.ca/kodi/20150328-repositories/',1656,'')
    addDir('xstream-addon.square7.ch/repo','http://xstream-addon.square7.ch/repo/',1656,'')
    addDir('xbmc.samyantoun.com/addons','http://xbmc.samyantoun.com/addons/',1656,'')
    addDir('iptvip.info/repo/','http://iptvip.info/repo/',1656,'')
    addDir('www.alelec.net/kodi','http://www.alelec.net/kodi/',1656,'')
    addDir('d.openboxfan.com/xbmc','http://d.openboxfan.com/xbmc/',1656,'')
    addDir('koditr.org/kurulum','http://koditr.org/kurulum/',1656,'')
    addDir('[COLOR http://android.bulfon.com/MiBoxMini/Media/Kodi','http://android.bulfon.com/MiBoxMini/Media/Kodi/',1656,'')
    addDir('home.pilsfree.net/chudy/','https://home.pilsfree.net/chudy/',1656,'')
    addDir('kodi.shivuthegreat.com/Video','http://kodi.shivuthegreat.com/Video/',1656,'')
    addDir('kodi.media-guru.com.au','http://kodi.media-guru.com.au/',1656,'')
    addDir('kodi.neptune-one.net','http://kodi.neptune-one.net/',1656,'')
    addDir('cwal.me','http://cwal.me/xbmc/addons/',1656,'')
    addDir('viewstationusa.org/vs/XbmcRepos/','http://viewstationusa.org/vs/XbmcRepos/',1656,'')
    addDir('dextertv.site40.net','http://dextertv.site40.net',1656,'')
    addDir('web-develop.ca/kodi','http://web-develop.ca/kodi',1656,'')
    addDir('web-develop.ca/kodi/20150328-repositories','http://web-develop.ca/kodi/20150328-repositories',1656,'')
    addDir('web-develop.ca/kodi/20150403-repositories','http://web-develop.ca/kodi/20150403-repositories',1656,'')
    addDir('web-develop.ca/kodi/20150911-repos','http://web-develop.ca/kodi/20150911-repos',1656,'')
    addDir('kangotek.com/repo','http://kangotek.com/repo',1656,'')
    addDir('','',1656,'')
    addDir('','',1656,'')
def SPORTS(url):
        xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_TITLE)
        link = OPEN_URL(url)
        match=re.compile('display-name lang="en">(.+?)</display-name>').findall(link)
        for name in match:
            addDir('%s'%(name),url,4561,'http://www.astro.com.my/whats-on/logoimages/ChannelLogo/Pos/%s_100.png')
def SPORTS2(url,name):
        link = OPEN_URL(url)
        match=re.compile('<programme start="\d\d\d\d\d\d\d\d(\d\d)(\d\d)\d\d \+\d\d\d\d" stop="\d\d\d\d\d\d\d\d\d\d\d\d\d\d \+\d\d\d\d" channel="%s">.+?<title lang="en">(.+?)<'%(name), re.DOTALL).findall(link)
        for start,finish,title in match:
            addDir('[%s:%s] - %s'%(start,finish,title),'http://tecbox.tv/repo/teciptvguide/sports.xml',4561,'http://www.astro.com.my/whats-on/logoimages/ChannelLogo/Pos/%s_100.png')

def addoncats():
    addDir2('[COLOR yellow]MEGA SEARCH BY PIPCAN[/COLOR]','',1000,'')
def addonsdownloadpage(url):
    link = OPEN_URL(url)
    url2 = url
    match=re.compile('<[aA] href="(.+?)\/">(.+?)\/</[aA]>').findall(link)
    match2=re.compile('<[aA] href="(.+?)\.(.+?)">(.+?)</[aA]>').findall(link)
    for url,name in match:
        addDir('../%s'%name.replace(' ',''),'%s/%s'%(url2,url),1656,'')
    for url,ext,name in match2:
        str1 = ext
        find_this = "zip"
        if find_this in str1:
            addDir2('[COLOR yellow][DOWNLOAD][/COLOR] %s'%name.replace('../>','').replace(' ','').replace('%20',''),'%s/%s'%(url2,name.replace(' ','').replace('%20','').replace('.zip.zip','.zip')),1654,'')
        elif "m3u" in str1:
            addDir('[COLOR green][OPEN][/COLOR] %s'%name.replace('../>','').replace(' ','').replace('%20',''),'%s/%s'%(url2,name.replace(' ','').replace('%20','').replace('.zip.zip','.zip')),1458,'')
def DOWNLOADIMAGE(url,name):
    HOME = xbmc.translatePath('special://home/addons/%s'%AddonID)
    dialog = xbmcgui.Dialog()
    ret = dialog.select('What To Do', ['View Image', 'Download Image', 'Cancel'])
    if (ret == 0):
    	xbmc.executebuiltin("ShowPicture(%s)"%url)
        return True
    if (ret == 1):
        dialog = xbmcgui.Dialog()
        if dialog.yesno("DOWNLOADING IMAGE", 'Do you Wish To Download This Icon','', "",'No','Yes'):
            dp = xbmcgui.DialogProgress()
            dp.create('Downloading')
            dp.update(20)
            dialog = xbmcgui.Dialog()
            dp = xbmcgui.DialogProgress()
            dp.create('Downloading Icon')
            dp.update(60)
            url = ("%s"%(url))
            localfile = os.path.join(addonDir,"resources/logos/%s.png"%name)
            urllib.urlretrieve(url,localfile,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
            dp.update(70,'Updating Addons')
            dp.update(100)
            dp.close()
            dialog.ok("Finished Downloading", "All Done!")
        else:
            return   
#    if (ret == 2):
#        play=xbmc.Player(GetPlayerCore())
#        play.play('plugin://plugin.video.f4mTester/?url=%s&mode=play'%(url).replace(".m3u8",".f4m"))
    if (ret == 2):
        return True 
         

def MAILRU(url):
            link = OPEN_URL(url)
            match=re.compile('tId="(.+?)"><a href="#">(.+?)\n', re.DOTALL).findall(link)
            for url,name in match:
                addDir2(name,'plugin://program.plexus/?url=acestream://%s&mode=1&name=acestream+title'%url,9,'')
def CATMOVIES():
            addDir2('[COLOR yellow]MEGA SEARCH BY PIPCAN[/COLOR]','',1000,'')
            searchStr = ''
            addDir('Search Navix','http://www.navixtreme.com/playlist/search/video/',735,'http://media.navi-x.org/images/logos/search.png')
            addDir('Search letwatch.us','http://letwatch.us/?op=search&k=',3,'http://letwatch.us/images/logo.png')
            addDir('Search Vodlocker','http://vodlocker.com/?op=search&k=',5,'http://vodlocker.com/images/logo.png')
            addDir('Search cloudy.ec','http://www.cloudy.ec/search?search=',6,'http://www.cloudy.ec/img/logo.png')
            addDir('Dedibox','http://sd-41445.dedibox.fr/',8,'ww')
            addDir('Craving TV','http://series-cravings.me/tv-show-1',5679,'ww')
            addDir('Craving Movie','http://series-cravings.me/tv-show-1',5679,'ww')
            addDir('Filmgozar','http://dl.filmgozar.com/',8,'ww')
            addDir('Filmgozar','http://dl.tehmovies.com/94',8,'ww')
            addDir('LOADS OF FILMS','http://46.105.122.150/',8,'ww')
            addDir('Moviefarsi','http://dl5.moviefarsi.org/',8,'ww')
            addDir('Free Upload .IR ','http://dl8.freeupload.ir/',8,'ww')
            addDir('NFilm','http://dl.nfilm.org/DL/',8,'ww')
            addDir('Canflix','http://cdn.alpha.canflix.net',8,'ww')
            addDir('Tehmovies','http://dl.tehmovies.com/',8,'ww')
            addDir('MVSnap','http://mvsnap.com',299,'ww')
            addDir('Yukinoshita','http://yukinoshita.eu/ddl/',12,'ww')
            addDir('Seed Cows','http://seed.cows.io/',8,'ww')
            addDir('Hastidownload','http://dl.hastidownload.net/ali/film/',8,'ww')
            addDir('Kino Kong','http://kinokong.net',18,'http://smarttvnews.ru/wp-content/uploads/2015/05/32731097.png')
            addDir('HDFullTV','http://hdfull.tv',656,'')
            addDir('MOVIE25','http://movie25.ag',9780,'')
def CATMUSIC():
            addDir2('[COLOR yellow]MEGA SEARCH BY PIPCAN[/COLOR]','',1000,'')
            addDir('ARTISTS','http://e-mp3bul.com/albumler/2/yabanci-mp3-indir.html',5000,'https://lh5.ggpht.com/is1Mt-5l5uoysOrEZ9MhCn8JAe5_QokIcLdxI_6k-105AB9WTeycHDHbLiX37EYcXg=w300')
            addDir('ALBUMS','http://e-mp3bul.com/album/142/2015.html',5000,'https://lh5.ggpht.com/is1Mt-5l5uoysOrEZ9MhCn8JAe5_QokIcLdxI_6k-105AB9WTeycHDHbLiX37EYcXg=w300')
            addDir('[COLOR red][BROKEN] Search FreeMp3.SE[/COLOR]','http://freemp3.se/?query=',5023,'https://lh5.ggpht.com/is1Mt-5l5uoysOrEZ9MhCn8JAe5_QokIcLdxI_6k-105AB9WTeycHDHbLiX37EYcXg=w300')
            addDir('http://muscut.ru/','http://muscut.ru/search/',190,'https://lh5.ggpht.com/is1Mt-5l5uoysOrEZ9MhCn8JAe5_QokIcLdxI_6k-105AB9WTeycHDHbLiX37EYcXg=w300')
def CATANIME():
            addDir2('[COLOR yellow]MEGA SEARCH BY PIPCAN[/COLOR]','',1000,'')
            addDir('Toonova Cartoon','http://www.toonova.com/cartoon',8000,'http://www.toonova.com/images/site/front/logo.png')
            addDir('Animetoon.eu Cartoon','http://www.animetoon.eu/cartoon',8000,'http://www.animetoon.eu/images/site/front/logo.png')
            addDir('Animetoon.eu Movies','http://www.animetoon.eu/movies',8000,'http://www.animetoon.eu/images/site/front/logo.png')
            addDir('Animewow','http://www.animewow.eu/anime',8000,'http://www.animewow.eu/images/site/front/logo.png')
            addDir('Animakai Anime','http://www.animakai.tv/animes/1/',13,'http://www.animakai.tv/sys_misc/images/logo.png')
            addDir('Animetoon Dubbed Anime','http://www.animetoon.eu/dubbed-anime',8000,'http://www.animetoon.eu/images/site/front/logo.png')
            addDir('videozoo Movies','http://www.videozoo.me/category/anime-movies',8000,'http://www.videozoo.me/wp-content/themes/anime/images/header.jpg')
            addDir('videozoo Animne','http://www.videozoo.me/new-anime-list',8000,'http://www.videozoo.me/wp-content/themes/anime/images/header.jpg')
            addDir('watchcartoonweb','http://watchcartoonweb.com/',9000,'http://watchcartoonweb.com/themes/default/img/icon/logo.png')
def CATVIDEOS():
            addDir2('[COLOR yellow]MEGA SEARCH BY PIPCAN[/COLOR]','',1000,'')
            addDir('Search Bing Videos','http://www.msn.com/en-us/video/searchresults?q=',37,'http://microsoft-news.com/wp-content/uploads/2014/09/Bing-logo-1.jpg')
            addDir('Failarmy','http://www.failarmy.com',4444,'http://www.failarmy.com/2.0.39/media/img/site-logo-sm.png')
            addDir('Worldstar','http://www.worldstarhiphop.com/videos/trending.php?v=now',4557,'http://www.failarmy.com/2.0.39/media/img/site-logo-sm.png')
def CATDOCS():
            addDir2('[COLOR yellow]MEGA SEARCH BY PIPCAN[/COLOR]','',1000,'')
            addDir('Top Documentary Films','http://www.topdocumentaryfilms.com/watch-online/',4448,'')
def CATIPTV():
            addDir2('[COLOR yellow]MEGA SEARCH BY PIPCAN[/COLOR]','',1000,'')
            searchStr = ''
            addDir('Search Navix','http://www.navixtreme.com/playlist/search/video/',735,'http://media.navi-x.org/images/logos/search.png')
            addDir('Search PASTEBIN','https://www.googleapis.com/customsearch/v1element?key=AIzaSyCVAXiUzRYsML1Pv6RwSG1gunmMikTzQqY&rsz=filtered_cse&num=20&hl=en&prettyPrint=false&source=gcsc&gss=.com&sig=56f70d816baa48bdfe9284ebc883ad41&cx=013305635491195529773:0ufpuq-fpt0&sort=date&q=',503,'http://pastebin.com/i/fb2.jpg')
            addDir('[COLOR red][BROKEN] [/COLOR]http://80.80.160.168/live/','http://80.80.160.168/live',8,'ww')
            addDir('TV Online Streams','http://tvonlinestreams.com',100,'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTdHvBF68jexfm7JTjh692IRi4xC5EbtIy5fDsMcE3ItOqMhXpN')
            addDir('kodi.altervista','http://kodi.altervista.org/category/iptv-playlist/',8008,'http://media.navi-x.org/images/logos/search.png')
            addDir('IPTV Filmover','http://iptv.filmover.com',200,'http://website.informer.com/thumbnails/280x202/i/iptv.filmover.com.png')
            addDir('FreeTux TV','http://database.freetuxtv.net',300,'http://lh5.googleusercontent.com/-3BqBJNvGN-E/TqQWikkIrfI/AAAAAAAAAnk/nGx_J8pK1mU/s1600/freetuxtv.png')
            addDir('Hack-Sat','http://hack-sat.com/iptv.php',4285,'http://lh5.googleusercontent.com/-3BqBJNvGN-E/TqQWikkIrfI/AAAAAAAAAnk/nGx_J8pK1mU/s1600/freetuxtv.png')
            addDir('VLC Database','http://database.eu.pn/index.php/database/exportvlc',4285,'http://lh5.googleusercontent.com/-3BqBJNvGN-E/TqQWikkIrfI/AAAAAAAAAnk/nGx_J8pK1mU/s1600/freetuxtv.png')
            addDir('I-PTV BLOGSPOT','http://i-ptv.blogspot.co.uk',401,'http://4.bp.blogspot.com/-nHAYhJE46Vg/VG27mtXmXYI/AAAAAAAAA4Q/-_QhnzBJ8M4/s1600/logo2%2B-%2B500.png')
            addDir('I-PTV BLOGSPOT RUSSIA','http://i-ptv.blogspot.co.uk/p/russia-big.html',401,'http://4.bp.blogspot.com/-nHAYhJE46Vg/VG27mtXmXYI/AAAAAAAAA4Q/-_QhnzBJ8M4/s1600/logo2%2B-%2B500.png')
            addDir('Pastebin m3u','https://www.googleapis.com/customsearch/v1element?key=AIzaSyCVAXiUzRYsML1Pv6RwSG1gunmMikTzQqY&rsz=filtered_cse&num=20&hl=en&prettyPrint=false&source=gcsc&gss=.com&sig=56f70d816baa48bdfe9284ebc883ad41&cx=013305635491195529773:0ufpuq-fpt0&q=m3u&sort=date',501,'http://pastebin.com/i/fb2.jpg')
            addDir('Pastebin M3U8','https://www.googleapis.com/customsearch/v1element?key=AIzaSyCVAXiUzRYsML1Pv6RwSG1gunmMikTzQqY&rsz=filtered_cse&num=20&hl=en&prettyPrint=false&source=gcsc&gss=.com&sig=56f70d816baa48bdfe9284ebc883ad41&cx=013305635491195529773:0ufpuq-fpt0&q=m3u8&sort=date',501,'http://pastebin.com/i/fb2.jpg')
            addDir('TV Degunino','http://tv.degunino.net/m3u/',8,'')
            addDir('tunisia-dreambox','http://www.tunisia-dreambox.info/e2-addons-manager/Tunisiasat-plugins/softupdates/TSmedia/',8,'')
            addDir('iptvm3u','http://www.iptvm3u.com/search?updated-max=2016-03-03T15%3A14%3A00-08%3A00&max-results=7000',600,'http://3.bp.blogspot.com/-mMVnbnRsISw/U7c8sb8Z2uI/AAAAAAAAAL8/_6Vfvpcfa7c/s1600/freeiptv.png')
            addDir('VLC','http://www.vlchistory.eu.pn',701,'http://www.vlchistory.eu.pn/images/vlcstreamhistory.jpg')
            addDir('LANMEAPP','http://langamepp.com/playlist/pipcan/Snooker85',504,'http://langamepp.com/iptv/img/logo.png')
            addDir('Iptvlinks','http://www.iptvlinks.com/feeds/posts/summary?alt=json-in-script&callback=pageNavi&max-results=200',2000,'http://4.bp.blogspot.com/-D4Nbf7BM52c/VIzTSja7qdI/AAAAAAAACe4/u7PSn24mxK8/s1600/iptvlinkslogo.png')
            addDir('Free-links-iptv.blogspot','https://www.blogger.com/feeds/7582140021242686461/posts/summary?alt=json-in-script&start-index=1&max-results=10',2000,'')
            addDir('Navi-X','http://www.navixtreme.com/wiilist/',730,'')
            addDir('HDFULLHD EU','http://hdfullhd.eu/iptv_groups.txt',181,'')
            addDir('SKYSKATE','http://www.skysate.net',182,'')
            addDir('IPTVPLAYLIST.com','http://iptvplaylists.com/',183,'')
            addDir('IPTVM3U.BLOGSPOT','http://iptvm3u8.blogspot.co.uk/',184,'')
            addDir('IPTVSPORTT','http://www.iptvsportt.com',186,'')
            addDir('IPTV.Online-TV','http://iptv.online-tv.ws/',187,'')
            addDir('RUSSIAN PEERS TV','http://api.peers.tv/iptv/2/playlist.m3u',188,'')
            addDir('GLAZTV','http://www.glaz.tv/online-tv/',189,'')
            addDir('FILMON','file:///%s/VLC.m3u'%addonDir,194,'')
            addDir('select-pedia','http://select-pedia.com/tutos/tag/playlist/',4289,'')
            addDir('xbmchelper.squarespace.com','http://xbmchelper.squarespace.com/iptv/',4290,'')
            addDir('http://iptv-xbmc.blogspot.co.uk/','http://iptv-xbmc.blogspot.co.uk/',4555,'')
            addDir('http://shadowcrew.info/adryan/stalker001.m3u','http://shadowcrew.info/adryan/stalker001.m3u',4556,'')
def sportiptv(url):
        addDir('[COLOR gold]CLICK HERE TO SORT OUT DEAD LINKS[/COLOR]',url,1456,'')
        r = requests.get(url)
        match=re.compile("<h2 class='post-home-title post-main-home-title'>\n<a href='(.+?)' title='(.+?)'>").findall(r.text)
        match2=re.compile("#EXTINF:.+?,(.+?)<br />\n(.+?)<br />").findall(r.text)
        for url,name in match:
            addDir('[COLOR yellow]%s[/COLOR]'%name,url,186,'')
        for name,url in match2:
                    addDir2('[COLOR yellow]%s[/COLOR]'%name,url,10,'')
def xbmclog(url):
        addDir('[COLOR gold]CLICK HERE TO SORT OUT DEAD LINKS[/COLOR]',url,1456,'')
        r = requests.get(url)
        match=re.compile("<h3 class='post-title entry-title' itemprop='name'>\n<a href='(.+?)'>(.+?)</a>", re.DOTALL).findall(r.text)
        match2=re.compile('#EXTINF:.+?,(.+?)[\n](.+?)[<\n]', re.DOTALL).findall(r.text)
        for url,name in match:
            addDir(name,url,4555,'')
        for name,url in match2:
            addDir2(name,url,10,'')
def PEERSTV(url):
        addDir('[COLOR gold]CLICK HERE TO SORT OUT DEAD LINKS[/COLOR]',url,1456,'')
        r = requests.get(url)
        match=re.compile('EXTINF:.+?,(.+?)\nhttp(.+?)\n', re.DOTALL).findall(r.content)
        for name,url in match:
            addDir2(name,'http%s'%url,9,'')
def tew(url):
        addDir2('[COLOR red]ERASE ENTIRE LIST[/COLOR]',url,1459,'')
        addDir('[COLOR gold]CLICK HERE TO SORT OUT DEAD LINKS[/COLOR]',url,1456,'')
        link = OPEN_URL(url)
        match=re.compile('EXTINF:.+?,(.+?)[<\n].+?http(.+?)[<\n]', re.DOTALL).findall(link)
        for name,url in match:
            addDir2(name,'http%s'%url,9,'')
def muscut(url):
            searchStr = ''
            keyboard = xbmc.Keyboard(searchStr, 'Search')
            keyboard.doModal()
            searchStr=keyboard.getText()
            r = requests.get('%s%s'%(url,searchStr))
            match=re.compile('<h2 class="search-title" >(.+?)</h2>.+?onclick="data_update\(\'(.+?)\'.+?open_download\(\'(.+?)\'', re.DOTALL).findall(r.content)
            for url,image,down in match:
                addDir2(url,down,10,image)
def xbmchelper(url):
    addDir('[COLOR gold]CLICK HERE TO SORT OUT DEAD LINKS[/COLOR]',url,1456,'')
    r = requests.get(url)
    match=re.compile('\n(.+?)<a href="http://m3u\.tv/(.+?)">').findall(r.content)
    match2=re.compile('#EXTINF:.+?,(.+?)\n(.+?)\n').findall(r.content)
    for name,url in match:
        addDir(name,url,4290,'')
    for name,url in match2:
        addDir2(name,url,10,'')
def glaztv(url):
        addDir('[COLOR gold]CLICK HERE TO SORT OUT DEAD LINKS[/COLOR]',url,1456,'')
        r = requests.get(url)
        match=re.compile('<a href="(.+?)"><img width="60" height="60" src="(.+?)" alt="(.+?)"').findall(r.content)
        match2=re.compile('file=(.+?)&').findall(r.content)
        match3=re.compile('class="pageactive">(.+?)</span><a href="(.+?)">').findall(r.content)
        for url,img,name in match:
            addDir(name,'http://www.glaz.tv%s'%url,189,'http://www.glaz.tv%s'%img)
        for url in match2:
            addDir2(url,url,10,'http://www.glaz.tv%s'%url)
        for name,url in match3:
            addDir('Currrnt Page %s Go To Next >>>>'%name,'http://www.glaz.tv%s'%url,189,'http://www.glaz.tv%s'%url)
def iptvonline(url):
        addDir('[COLOR gold]CLICK HERE TO SORT OUT DEAD LINKS[/COLOR]',url,1456,'')
        r = requests.get(url)
        match=re.compile('<span class="thumbnail"><a href="(.+?)"><img width="100" height="100" src="(.+?)"').findall(r.text)
        match2=re.compile("#EXTINF:.+?,(.+?)<br/>\n(.+?)<br/>").findall(r.text)
        match3=re.compile('<link rel="next" href="(.+?)"/>').findall(r.text)
        for url in match3:
            addDir('[COLOR yellow]NEXT >>>>>[/COLOR]',url,187,'')
        for url,name in match:
            addDir('[COLOR yellow]%s[/COLOR]'%name,url,187,name)
        for name,url in match2:
            addDir2(name,url,9,'')
def TVLOGOS(url):
        link = OPEN_URL(url)	
        match=re.compile('<img src="/views/default/images/flags/(.+?)" alt="(.+?)" width="48" height="48" /><a href="(.+?)"').findall(link)
        match2=re.compile('<img src="(.+?)" alt="(.+?)"').findall(link)
        for image,name,url in match:
            addDir('%s'%(name),'http://www.tv-logo.com%s'%url,5463,'http://www.tv-logo.com/views/default/images/flags/%s'%image)
        for image,name in match2:
            addDir3('%s'%(name),'http://www.tv-logo.com%s'%image,4916,'http://www.tv-logo.com%s'%image)
def NAVIX(url):
        addDir('[COLOR gold]CLICK HERE TO SORT OUT DEAD LINKS[/COLOR]',url,1456,'')
        addDir('[COLOR yellow]SEARCH[/COLOR]','http://www.navixtreme.com/playlist/search/video/',735,'http://media.navi-x.org/images/logos/search.png')
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
def FULLHDTV(url):
        link = OPEN_URL(url)
        match=re.compile('<li><a href="http://hdfull.tv/tags-peliculas/(.+?)">(.+?)</a></li>').findall(link)
        match2=re.compile('<a href="(.+?)".+?<img class="img-preview spec-border"  src="(.+?)" alt="(.+?)"', re.DOTALL).findall(link)
        match3=re.compile('<b class="provider" style="background-image: url\((.+?)\)">(.+?)</b>.+?</b>(.+?)\n.+?&nbsp;<a href="(.+?)"', re.DOTALL).findall(link)
        match4=re.compile('<iframe src="http://(.+?)/(.+?)" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" width="920" height="360" allowfullscreen="true">', re.DOTALL).findall(link)
        for url,name in match:
            addDir('%s'%(name),'http://hdfull.tv/tags-peliculas/%s'%url,656,'')
        for name,url in match4:
            addDir2('%s'%(name),'http://s/%s'%(name,url),6,'')
        for image,name in match2:
            addDir('%s'%(name),'http://hdfull.tv/movies/%s'%name.replace('',''),656,image)
        for image,server,quality,url in match3:
            addDir2('%s [COLOR yellow]%s[/COLOR]'%(url,quality),url,4,image)
def HACKSAT(url):
        addDir('[COLOR gold]CLICK HERE TO SORT OUT DEAD LINKS[/COLOR]',url,1456,'')
        addDir('[COLOR yellow]Go To Page 2[/COLOR]','http://hack-sat.com/iptv-1.html',4285,'')
        link = OPEN_URL(url)
        match=re.compile('#EXTINF:.+?,(.+?)\n(.+?)\n').findall(link)
        match3=re.compile('<option value="(.+?)">(.+?)\((.+?)\)</option>').findall(link)
        for name,url in match:
            addDir2(name,url,9,'')
        for number,url,ammount in match3:
            addDir2('%s - %s  (%s)'%(number,url,ammount),'%s'%url,9,'')
def CCAMS(url):
        link = OPEN_URL(url)
        match=re.compile('[\n>]([CN])(.+?)[<\n]').findall(link)
        for norc,code in match:
            addDir2('%s%s'%(norc,code),'d',4287,'')
def CCAM(url):
        link = OPEN_URL(url)
        match=re.compile('\d\d\d\d\d\d;">(.+?)<').findall(link)
        for code in match:
            addDir2('%s'%(code),'d',4287,'')
def SHOWCCAMS(name):
    dialog = xbmcgui.Dialog()
    dialog.ok("Your CamLine", "%s"%name)
def FREEMP3SE(url):
        searchStr = ''
        keyboard = xbmc.Keyboard(searchStr, 'Search')
        keyboard.doModal()
        searchStr=keyboard.getText()
        link = OPEN_URL('%s%s'%(url,searchStr))
        match2=re.compile('data-title="(.+?)" data-url="(.+?)"', re.DOTALL).findall(link)
        match=re.compile('<a class="page-next" href="(.+?)">(.+?)<', re.DOTALL).findall(link)
        for name,url in match2:
            addDir2(name,url.replace(' ','%20'),9,'')
        for url2,name in match:
            addDir(name,url2,5024,'')
def LOGOPIDIA(url):
        if url == 'http://logos.wikia.com/wiki/Special:Search?fulltext=Search&search=':
            searchStr = ''
            keyboard = xbmc.Keyboard(searchStr, 'Search')
            keyboard.doModal()
            searchStr=keyboard.getText()
            link = OPEN_URL('%s%s'%(url,searchStr))
            match2=re.compile('<img src="(.+?)"', re.DOTALL).findall(link)
            match=re.compile('<a href="(.+?)" class="result-link" data-pos=".+?" >(.+?)</a>', re.DOTALL).findall(link)
            for url,name in match:
                addDir(name,url,9777,'')
            for url in match2:
                addDir(url,url,9777,url)
        else:
            link = OPEN_URL(url)
            match=re.compile('<a href="(.+?)" class="result-link" data-pos=".+?" >(.+?)</a>', re.DOTALL).findall(link)
            match2=re.compile('<img src="(.+?)"(.+?)', re.DOTALL).findall(link)
            for url,name in match:
                addDir(name,url,9777,'')
            for url,name in match2:
                addDir2(name,url,4916,url)
def FREEMP3SE2(url):
        link = OPEN_URL(url)
        match2=re.compile('data-title="(.+?)" data-url="(.+?)"', re.DOTALL).findall(link)
        match=re.compile('<a class="page-next" href="(.+?)">(.+?)<', re.DOTALL).findall(link)
        for name,url in match2:
            addDir2(name,url.replace(' ','%20'),9,'')
        for url2,name in match:
            addDir(name,url2,5024,'')
def RADIO(url):
        link = OPEN_URL(url)
        match=re.compile('<td><img width="8" height="8" alt="" src="b.gif" /> <a href="(.+?)">(.+?)</a></td></tr>').findall(link)
        match2=re.compile('<b>(.+?)</b>.+?<a href="(.+?)">(.+?)<', re.DOTALL).findall(link)
        for url,name in match:
            addDir(name,'http://listenlive.eu/%s'%url,8890,'')
        for name,url,qu in match2:
            addDir2('%s - %s'%(name,qu),url,9,'')
def NAVISEARCH(url):
        addDir('[COLOR gold]CLICK HERE TO SORT OUT DEAD LINKS[/COLOR]',url,1456,'')
        searchStr = ''
        keyboard = xbmc.Keyboard(searchStr, 'Search')
        keyboard.doModal()
        searchStr=keyboard.getText()
        link = OPEN_URL('%s%s'%(url,searchStr))
        match=re.compile('type=playlist\nname=(.+?)\nthumb=(.+?)\nURL=(.+?)\n').findall(link)
        match3=re.compile('name=>>>.+?URL=http:\/\/www\.navixtreme\.com\/wiilist\/(.+)', re.DOTALL).findall(link)
        match1=re.compile('type=video\nname=(.+?)\nthumb=(.+?)\nURL=(.+?)\n').findall(link)
        for name,thumb,url in match:
            addDir(name,url,730,thumb)
        for name,thumb,url in match1:
            addDir2('%s'%(name),'%s'%(url),9,thumb)
        for url in match3:
            addDir('NEXT >>>','http://www.navixtreme.com/wiilist/%s'%url,730,'')
def jokes2(name,url):
        showText(name,url)
def showText(heading, text):
    id = 10147
    xbmc.executebuiltin('ActivateWindow(%d)' % id)
    xbmc.sleep(100)
    win = xbmcgui.Window(id)
    retry = 50
    while (retry > 0):
        try:
            xbmc.sleep(10)
            retry -= 1
            win.getControl(1).setLabel(heading)
            win.getControl(5).setText(text.replace('<br>','\n').replace('  ',''))
            return
        except:
            pass
def DOC(url):
        link = OPEN_URL(url)
        match=re.compile('<a href="http://topdocumentaryfilms.com/category/(.+?)" title="Browse.+?">(.+?)</a>(.+?)</h2>').findall(link)
        match2=re.compile('<a href="(.+?)" title="(.+?)"><img width="95" height="125" src="(.+?)"').findall(link)
        match3=re.compile('embedUrl" content="(.+?)"').findall(link)
        match4=re.compile('<link rel="next" href="(.+?)" />"').findall(link)
        for url,name,count in match:
            addDir('%s - %s'%(name,count),'http://www.topdocumentaryfilms.com/category/%s'%url,4448,'')
        for url,name,image in match2:
            addDir2('%s'%(name),url,4448,image)
        for url in match4:
            addDir('[COLOR yellow]NEXT PAGE[/COLOR]',('%s')%url,4448,'')
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
    elif ADDON.getSetting(id='passfword') == '2':
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
        match=re.compile('background-image:url\((.+?)\);"><span>(.+?)</span></a></TD>\n<TD valign=top>\n<div class="link"><a href="(.+?)">(.+?)</a></div>').findall(link)
        for image,time,url,name in match:
            addDir2('%s - %s'%(name,time),url,4,'%s'%(image))
def canflix(url):
        link = OPEN_URL(url)
        match=re.compile('<td data-sort-value="(.+?)"><i class="fa fa-(.+?) fa-fw"></i>&nbsp;<a href="(.+?)">.+?\n.+?value=".+?">(.+?)<').findall(link)
        for name,type,url,size in match:
            addDir2('%s - %s'%(name,size),'%s'%url,4,'%s'%(type))
def HDFULLHD(url):
        addDir('[COLOR gold]CLICK HERE TO SORT OUT DEAD LINKS[/COLOR]',url,1456,'')
        link = OPEN_URL(url)
        match=re.compile('(.+?),(.+?)txt').findall(link)
        match2=re.compile('(.+?),(.+?)m3u8').findall(link)
        match3=re.compile('(.+?),(.+?)ts').findall(link)
        match4=re.compile('(.+?),(.+?)\/').findall(link)
        for name,url in match:
            addDir(name,'%stxt'%url,181,'')
        addDir2('------------ END --------------','f',9,'')
        for name,url in match2:
            addDir2(name,'%sm3u8'%url,9,'')
        for name,url in match3:
            addDir2(name,'%sts'%url,9,'')
        for name,url in match4:
            addDir2(name,'%sm3u8'%url,9,'')
        addDir2('------------ END --------------','f',9,'')
def MVSNAP(url):
        addDir('[COLOR green]SEARCH[/COLOR]','http://mvsnap.com/v1/api/search?query=',299,'ww')
        if url == 'http://mvsnap.com/v1/api/search?query=':
            searchStr = ''
            keyboard = xbmc.Keyboard(searchStr, 'Search')
            keyboard.doModal()
            searchStr=keyboard.getText()
            link = OPEN_URL('%s%s'%(url,searchStr.replace(' ','%20')))
            match=re.compile('"title":"(.+?)","type":"(.+?)","slug":"(.+?)","photo":"(.+?)"', re.DOTALL).findall(link)
            for name,type,url,image in match:
                addDir('%s'%(name),'http://mvsnap.com/%s/%s'%(type,url),299,image)
        else:
            link = OPEN_URL(url)
            match=re.compile('<div class="media-body">.+?<h3 class="media-title">.+?<a href="(.+?)">(.+?)</a>', re.DOTALL).findall(link)
            match2=re.compile('<option value="(.+?)">(.+?)</option>', re.DOTALL).findall(link)
            for url,name in match2:
                addDir2('%s'%(name),'%s'%url,9,'')
            addDir2('','g',9,'')
            addDir2('[COLOR yellow]You May Like[/COLOR]','g',9,'')
            for url,name in match:
                addDir('%s'%(name),'http://mvsnap.com/%s'%url,299,'')
def ALLUC(url):
        addDir('[COLOR green]SEARCH[/COLOR]','https://www.alluc.com/api/search/',2468,'ww')
        if url == 'https://www.alluc.com/api/search/':
            searchStr = ''
            keyboard = xbmc.Keyboard(searchStr, 'Search')
            keyboard.doModal()
            searchStr=keyboard.getText()
            link = OPEN_URL('%s/stream/?apikey=708e0b7bbc1e087e4f4a1daf925cfa22&%s&count=10'%(url,searchStr.replace(' ','+')))
            match=re.compile('"sourcetitle":"(.+?)".+?sourcename":"(.+?)".+?"sourceurl":"(.+?)".+?"description","value":".+?".+?name":"length","value":"(.+?)".+?"pic","value":"(.+?)"', re.DOTALL).findall(link)
            for name,url,host,length,image in match:
                addDir2('%s - %s - %s'%(name,length,host),'%s'%(url.replace('\/','/')),9,image.replace('\/','/'))
        else:
            link = OPEN_URL(url)
            match=re.compile('<div class="media-body">.+?<h3 class="media-title">.+?<a href="(.+?)">(.+?)</a>', re.DOTALL).findall(link)
            match2=re.compile('<option value="(.+?)">(.+?)</option>', re.DOTALL).findall(link)
            for url,name in match2:
                addDir2('%s'%(name),'%s'%url,9,'')
            addDir2('','g',9,'')
            addDir2('[COLOR yellow]You May Like[/COLOR]','g',9,'')
            for url,name in match:
                addDir('%s'%(name),'http://mvsnap.com/%s'%url,299,'')
def altervista(url):
        addDir('[COLOR gold]CLICK HERE TO SORT OUT DEAD LINKS[/COLOR]',url,1456,'')
        link = OPEN_URL(url)
        match=re.compile('<a href="(.+?)" title="Permalink to (.+?)" rel="bookmark">').findall(link)
        match2=re.compile('#EXTINF:.+?,(.+?)<br />\n(.+?)<br />').findall(link)
        match3=re.compile('#EXTINF:.+?,(.+?)<br />(.+?)<').findall(link)
        match4=re.compile('<p>(.+?)<br/>(.+?) </p>').findall(link)
        match5=re.compile('#EXTINF:.+?,(.+?)<br />\n(.+?)</p>').findall(link)
        match6=re.compile('a href="(.+?)" ><span class="meta-nav">&larr;</span>(.+?)</a>').findall(link)
        for url,name in match:
            addDir('%s'%name.replace('</span>','').replace('</b>',''),'%s'%url,8005,'')
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
def kodialtervista(url):
        addDir('[COLOR gold]CLICK HERE TO SORT OUT DEAD LINKS[/COLOR]',url,1456,'')
        link = OPEN_URL(url)
        match7=re.compile('<h2 class="post-title entry-title"><a href="(.+?)" rel="bookmark">(.+?)</a></h2>').findall(link)
        match=re.compile('<a href="(.+?)" title="(.+?)" rel="bookmark"><time class="(.+?)" datetime=".+?">(.+?)</time></a>').findall(link)
        match2=re.compile(':.+?,(.+?)<br />(.+?)<').findall(link)
        match3=re.compile('#EXTINF:.+?,(.+?)<br />(.+?)<').findall(link)
        match4=re.compile('<p>(.+?)<br/>(.+?) </p>').findall(link)
        match5=re.compile('#EXTINF:.+?,(.+?)<br />\n(.+?)</p>').findall(link)
        match6=re.compile('a href="(.+?)"><span class="meta-nav">&larr;</span>(.+?)</a>').findall(link)
        match9=re.compile('>(.+?)</span></b><br /><b style="background: transparent;border: 0px;margin: 0px;padding: 0px;vertical-align: baseline"><span style="background: transparent;border: 0px;color: red;margin: 0px;padding: 0px;vertical-align: baseline">(.+?)<').findall(link)
        match10=re.compile("<span class='page-numbers current'>(.+?)</span>\n.+?<a class='page-numbers' href='(.+?)'>(.+?)</a>", re.DOTALL).findall(link)
        for url,name in match7:
            addDir('%s'%(name.replace('</span>','').replace('</b>','')),'%s'%url,8008,'')
        for url,time,name,date in match:
            addDir('%s  - %s -  %s'%(name,date,time),'%s'%url,8008,'')
        for name,url in match2:
            addDir2('%s'%(name),'%s'%url,9,'')
        for name,url in match9:
            addDir2('%s'%(name),'%s'%url,9,'')
        for name,url in match3:
            addDir2('%s'%(name),'%s'%url,9,'')
        for name,url in match4:
            addDir2('%s'%(name),'%s'%url,9,'')
        for name,url in match5:
            addDir2('%s'%(name),'%s'%url,9,'')
        for url,name in match6:
            addDir('%s'%(name),'%s'%url,8008,'')
        for current,url,next in match10:
            addDir('%s GO TO PAGE %s  >>>>'%(current,next),url,8008,'')
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
def movie25(url):
        r = requests.get(url)
        match=re.compile('<div class="movie_pic"><a href="(.+?)" target="_self" title="(.+?)">\n<img src="(.+?)"').findall(r.text)
        match2=re.compile('(.+?)</li>\n<li id="playing_button"><a href="(.+?)"').findall(r.text)
        match3=re.compile('external.php?url=\'(.+?)\'').findall(r.text)
        for url,name,image in match:
            addDir(name,'http://movie25.ag/%s'%url,9780,image)
        for name,url in match2:
            addDir(name,'http://movie25.ag/%s'%url,9780,'')
        for url in match3:
            addDir(url,'http://movie25.ag/%s'%url,9780,'')

def LANGSAT(url):
        link = OPEN_URL(url)
        match=re.compile('font face="Arial" size=1><b><a href="\.\.\/tvcountry\/(.+?)_1\.html">(.+?)</a>').findall(link)
        match2=re.compile('<td align="center"><a href="(.+?)"><img src="\.\.\/(.+?)".+?href=".+?">(.+?)</a></font></td>',re.DOTALL).findall(link)
        match3=re.compile('<b>(.+?)</b></font><br><a href=".+?" target="lyngwin"><img src="\.\.\/(.+?)"').findall(link)
        for url,name in match:
            addDir(name,'http://www.lyngsat-logo.com/tvcountry/%s.html'%url,4915,'http://www.satlogo.com/hires/flag/%s.png'%url)
        for url,image,name in match2:
            addDir(name,'http://www.lyngsat-logo.com/tvcountry/%s'%url,4915,'http://www.satlogo.com/%s'%image)
        for name,image in match3:
            addDir2(name,'http://www.lyngsat-logo.com/%s'%image.replace('logo','hires').replace('/tv',''),4916,'http://www.satlogo.com/%s'%image)
def freetuxtv(url):
        link = OPEN_URL(url)
        match=re.compile('src="(.+?)" alt="" /><i>(.+?)</i>.+<a href="(.+?)">(.+?)<').findall(link)
        for flag,name,url,count in match:
            addDir('%s - %s'%(name,count),'http://database.freetuxtv.net%s'%url,301,'http://database.freetuxtv.net%s'%(flag))
def showpicture(url):
    	xbmc.executebuiltin("ShowPicture(%s)"%url)
        return True
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
        addDir('[COLOR gold]CLICK HERE TO SORT OUT DEAD LINKS[/COLOR]',url,1456,'')
        link = OPEN_URL(url)
        match=re.compile('<h5><span style=" color:#06C">(.+?)</span>').findall(link)
        match2=re.compile('<a href="http://www.vlchistory.eu.pn/index.php/vlchistory/show/\d\d\d\d/\d\d/(.+?)">').findall(link)
        for url in match:
            r = requests.head('http://'+link)
            addDir2('%s %s'%(url,r),'%s'%url,9,'')
        for url in match2:
            addDir('%s'%(url),'http://www.vlchistory.eu.pn/index.php/vlchistory/show/2015/09/%s'%url,701,'')
def iptvm3u(url):
        addDir('[COLOR gold]CLICK HERE TO SORT OUT DEAD LINKS[/COLOR]',url,1456,'')
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
        match=re.compile('href="(.+?)" target=_blank>(.+?)<').findall(link)
        match3=re.compile('(.+?)\n').findall(link)
        match2=re.compile('id="realGkfuuudownload"><a href="(.+?)"').findall(link)
        for url,name in match:
            addDir2(name,url,9,'')
        for url in match3:
            addDir2(url.replace('',''),'%s'%url,9,'')
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
        addDir('[COLOR gold]CLICK HERE TO SORT OUT DEAD LINKS[/COLOR]',url,1456,'')
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
        addDir('[COLOR gold]CLICK HERE TO SORT OUT DEAD LINKS[/COLOR]',url,1456,'')
        link = OPEN_URL(url)
        match=re.compile('#EXTINF:.+?,(.+?)\n(.+?)\n').findall(link)
        match2=re.compile('<a href="https://sites.google.com/site/iptvblogspot/config/pagetemplates/m3u/(.+?)"> Download (.+?)</a>').findall(link)
        for url,name in match2:
            addDir('[COLOR yellow]%s[/COLOR]'%name,'https://sites.google.com/site/iptvblogspot/config/pagetemplates/m3u/%s'%url,401,'')
        for name,url in match:
            addDir2(name,url,9,'')
def IPTVLINKS(url):
        addDir('[COLOR gold]CLICK HERE TO SORT OUT DEAD LINKS[/COLOR]',url,1456,'')
        link = OPEN_URL(url)
        match=re.compile('{"rel":"alternate","type":"text/html","href":"(.+?)","title":"(.+?)"}].+?".+?"url":"(.+?)"').findall(link)
        for url,name,image in match:
            addDir(name,'%s'%(url.replace('\/', '/')),2001,image.replace('\/','/'))
def IPTVLINKS2(url):
        addDir('[COLOR gold]CLICK HERE TO SORT OUT DEAD LINKS[/COLOR]',url,1456,'')
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
def FILMON(url):
        addDir('[COLOR gold]CLICK HERE TO SORT OUT DEAD LINKS[/COLOR]',url,1456,'')
        link = OPEN_URL(url)
        match=re.compile('<title>(.+?)</title>.+?\n<link>(.+?)</link>').findall(link)
        for name,url in match:
            addDir2(name,'%s'%(url),10,'')
def CCS(url):
        addDir('[COLOR gold]CLICK HERE TO SORT OUT DEAD LINKS[/COLOR]',url,1456,'')
        link = OPEN_URL(url)
        match=re.compile('#EXTINF:(.+?)<.+?http(.+?)<', re.DOTALL).findall(link)
        match2=re.compile('<a class="next page-numbers" href="http://select-pedia.com/tutos/tag/playlist/page/(.+?)/">Next').findall(link)
        for url in match2:
            addDir('NEXT >>>>','http://select-pedia.com/tutos/tag/playlist/page/%s'%url,4289,'')
        for name,url in match:
            addDir2(name,'http%s'%(url),10,'')

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
        addDir('[COLOR gold]CLICK HERE TO SORT OUT DEAD LINKS[/COLOR]',url,1456,'')
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
        addDir('[COLOR gold]CLICK HERE TO SORT OUT DEAD LINKS[/COLOR]',url,1456,'')
        addDir('SEARCH','http://www.tvonlinestreams.com/?s=',102,'')
        link = OPEN_URL(url)
        match=re.compile('<h2 class="entry-title"><a href="(.+?)" title=".+?" rel="bookmark">(.+?)</a></h2>').findall(link)
        match2=re.compile('href="(.+?)" class="page" title="(.+?)">').findall(link)
        for url,name in match:
            addDir(name,url,101,'')
        for url,name in match2:
            addDir('GO TO PAGE %s '%name,url,100,'')
def tvonlinestreams2(url):
        addDir('[COLOR gold]CLICK HERE TO SORT OUT DEAD LINKS[/COLOR]',url,1456,'')
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
        addDir('[COLOR gold]CLICK HERE TO SORT OUT DEAD LINKS[/COLOR]',url,1456,'')
        link = OPEN_URL(url)
        match=re.compile('#EXTINF:.+?,(.+?)<br />\n(.+?)<').findall(link)
        match3=re.compile('<br />#EXTINF:.+?,(.+?)<br />(.+?)<br />').findall(link)
        for name,url in match:
            addDir2('%s'%(name.replace(':','[COLOR yellow] - [/COLOR]')),url.replace(' ',''),9,'')
        for name,url in match3:
            addDir2('%s'%(name.replace(':','[COLOR yellow] - [/COLOR]')),url.replace(' ',''),9,'')
def tvonlinestreams3(url):
        addDir('[COLOR gold]CLICK HERE TO SORT OUT DEAD LINKS[/COLOR]',url,1456,'')
        addDir('[COLOR gold]CLICK HERE TO SORT OUT DEAD LINKS[/COLOR]',url,1456,'')
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
        addDir('[COLOR gold]CLICK HERE TO SORT OUT DEAD LINKS[/COLOR]',url,1456,'')
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
def Husham(url):
        addDir('[COLOR gold]CLICK HERE TO SORT OUT DEAD LINKS[/COLOR]',url,1456,'')
        link = OPEN_URL(url)
        match2=re.compile('<a href="(.+?)" title="(.+?)"').findall(link)
        match=re.compile('#EXTINF:.+?,(.+?)http(.+?)[#<"\s\n]', re.DOTALL).findall(link)
        for url,name in match2:
            addDir(name,'%s'%(url),183,'')
        for name,url in match:
            addDir2(name,'http%s'%(url),10,'')

def canflix(url):
        link = OPEN_URL(url)
        match=re.compile('<td data-sort-value="(.+?)"><i class="fa fa-(.+?) fa-fw"></i>&nbsp;<a href="(.+?)">.+?\n.+?value=".+?">(.+?)<').findall(link)
        for name,type,url2,size in match:
            if type == 'folder':
                addDir('[COLOR yellow][FOLDER][/COLOR] %s - %s'%(name,size),'%s%s'%(url,url2),12,'%s'%(type))
            else:
                addDir2('%s - %s'%(name,size),'%s%s'%(url,url2),9,'%s'%(type))
def iptvm3u8blogspot(url):
        link = OPEN_URL(url)
        match=re.compile('<h3 class=\'post-title entry-title\'>\n<a href=\'(.+?)\'>(.+?)</a>').findall(link)
        match2=re.compile('<a class=\'blog-pager-older-link\' href=\'(.+?)\'').findall(link)
        for url,name in match:
                addDir(name,url,185,'')
        for url in match2:
                addDir('NEXTT >>>>',url,184,'')
def iptvm3u8blogspot2(url):
        addDir('[COLOR gold]CLICK HERE TO SORT OUT DEAD LINKS[/COLOR]',url,1456,'')
        link = OPEN_URL(url)
        match=re.compile('#EXTINF:.+?,(.+?)\n(.+?)\n').findall(link)
        for name,url in match:
                addDir2(name,url,10,'')
def VIPER(url):
        link = OPEN_URL(url)
        match=re.compile('<h2 class="forumtitle"><a href="(.+?)">(.+?)</a></h2>').findall(link)
        match2=re.compile('<a class="title" href="(.+?)" id=".+?"').findall(link)
        match3=re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" border="0"').findall(link)
        for url,name in match:
                addDir(name,'http://vipergirls.to/%s'%url,9778,'')
        for url in match2:
                addDir(url,'http://vipergirls.to/%s'%url,9778,'')
        for url,image in match3:
                addDir(image,url,9779,image)
def VIPER2(url):
    payload = dict(imgContinue='')
    r = requests.post(url, data=payload)
    test = ["http"+url for url in re.findall(r'http(.+?)\'', r.content)]
    for url in test:
        addDir2(url,url,4914,url)
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
        match=re.compile('[<Alia>"] href="(.+?)">(.+?)[<>"]').findall(link)
        for url2,name in match:
            str1 = url2
            find_this = "/"
            if find_this in str1:
                addDir('[COLOR yellow][FOLDER][/COLOR] %s'%name,url+url2,8,'')
            else:
                addDir2(name,url+'/'+url2,10,'')

def CLOUD(url):
        searchStr = ''
        keyboard = xbmc.Keyboard(searchStr, 'Search')
        keyboard.doModal()
        searchStr=keyboard.getText()
        link = OPEN_URL('%s%s'%(url,searchStr))
        match=re.compile('<a title="(.+?)" href="\/v\/(.+?)".+?time">(.+?)<.+?src="(.+?)"', re.DOTALL).findall(link)
        for name,url,time,image in match:
            addDir2('%s - %s'%(name,time),'https://www.cloudy.ec/embed.php?id=%s'%(url),4,image)
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
    dp.update(35,'Trying To Play Directly')
    try: play.play(url)
    except: pass 
    dp.update(65,'Trying To Resollver')
    try: url=urlresolver.HostedMediaFile(url).resolve()
    except: pass
    dp.update(100,'You Video Is Ready')
    dp.close()
def PLAYVIDEO3(url):
    import urlresolver
    from urlresolver import common
    dp = xbmcgui.DialogProgress()
    dp.create('Featching Your Video','Opening Ready')
    play=xbmc.Player(GetPlayerCore())
    play.play(url)
def PLAYVIDEO4(url):
    play=xbmc.Player(GetPlayerCore())
    play.play(url)
def PLAYVIDEO5(url):
    r = requests.get(url)
    match=re.compile('<iframe src="(.+?)"').findall(r.content)
    for url in match:
        import urlresolver
        from urlresolver import common
        play=xbmc.Player(GetPlayerCore())
        dp = xbmcgui.DialogProgress()
        dp.create('Featching Your Video','TRYING TO RESOLVE')
        try: url=urlresolver.HostedMediaFile(url).resolve()
        except: pass
        dp.update(100,'You Video Is Ready')
        dp.close()
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
        return
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
        return
    dp.close()
def DOWNLOAD(url):
    url = '%s'%url 
    HOME = xbmc.translatePath('special://home/addons/')
    dialog = xbmcgui.Dialog()
    if dialog.yesno("DOWNLOADING ADDON", 'Do you Wish To Install Addon','', "",'Close','Yes'):
        dp = xbmcgui.DialogProgress()
        dp.create('UPDATING')
        dp.update(20)
        dialog = xbmcgui.Dialog()
        dp = xbmcgui.DialogProgress()
        dp.create('Downloading Zip')
        dp.update(60)
        import zipfile 
        url = ("%s"%(url))
        localfile = os.path.join(addonDir,"resources/addons.zip")
        urllib.urlretrieve(url,localfile,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
        zin = zipfile.ZipFile(localfile, 'r')
        zin.extractall(HOME)
        dp.update(70,'Updating Addons')
        xbmc.executebuiltin("UpdateLocalAddons")
        xbmc.executebuiltin("UpdateLocalAddons")
        dp.update(70,'Refreshing Repos')
        xbmc.executebuiltin("UpdateAddonRepos")
        xbmc.executebuiltin("UpdateAddonRepos")
        dp.update(100)
        dp.close()
        dialog.ok("Finished Installing", "Installation Is Complete")
        xbmc.executebuiltin("UpdateLocalAddons")
        xbmc.executebuiltin("UpdateAddonRepos")
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
def addDir3(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        menu=[]
        menu.append(('Refresh', 'Container.Refresh'))        
        menu.append(('[COLOR red]Download Image[/COLOR]','Container.Update(%s?mode=4916&name=%s&url=%s)'% (sys.argv[0],name,url)))
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return True
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
elif mode==8008:
        kodialtervista(url)
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
elif mode==731:
        joke()
elif mode==732:
        showtext(heading, text)
elif mode==733:
        jokes2(name,url)
elif mode==735:
        NAVISEARCH(url)
elif mode==345:
        SEARCHCAT(url)
elif mode==8890:
        RADIO(url)
elif mode==5023:
        FREEMP3SE(url)
elif mode==5024:
        FREEMP3SE2(url)
elif mode==5025:
        PLAYVIDEO4(url)
elif mode==5055:
        GSEARCH(name,url)
elif mode==656:
        FULLHDTV(url)
elif mode==299:
        MVSNAP(url)
elif mode==181:
        HDFULLHD(url)
elif mode==5678:
        MAILRU(url)
elif mode==5679:
        CRAVING(url)
elif mode==5680:
        contact()
elif mode==2468:
        ALLUC(url)
elif mode==1654:
        DOWNLOAD(url)
elif mode==1655:
        addons(url)
elif mode==1656:
        addonsdownloadpage(url)
elif mode==5464:
        TVLOGOS(url)
elif mode==4912:
        COUNTRYS()
elif mode==4913:
    MISC(url)
elif mode==4914:
        showpicture(url)
elif mode==4915:
        LANGSAT(url)
elif mode==4916:
        DOWNLOADIMAGE(url,name)
elif mode==4285:
        HACKSAT(url)
elif mode==4286:
        CCAMS(url)
elif mode==4289:
        CCS(url)
elif mode==4287:
        SHOWCCAMS(name)
elif mode==5691:
    TVGUIDEUS(name)
elif mode==5692:
    TVGUIDEUS2(url)
elif mode==4111:
          INDIA(url)
elif mode==4112:
          INDIA2(url)
elif mode==8855:
          Guidecat()
elif mode==977:
          torrent(url)
elif mode==955:
          torrent2(url)
elif mode==966:
          torrent3(name,image)
elif mode==1456:
          TESTLINKS(url)
elif mode==1458:
    tew(url)
elif mode==1457:
    dialog = xbmcgui.Dialog()
    fn = dialog.browse(1, 'XBMC', 'files', '', False, False, 'C:')
    url = 'file:///'+fn
    TESTLINKS2(url)
elif mode==4113:
          VIAT(url)
elif mode==4114:
          PG(url)
elif mode==4115:
          RO(url)
elif mode==4116:
          TESTING()
elif mode==4117:
          SHOOT(url)
elif mode==4118:
          SHOOTs(url)
elif mode==9777:
          LOGOPIDIA(url)
elif mode==182:
          skysate(url)
elif mode==183:
          Husham(url)
elif mode==184:
          iptvm3u8blogspot(url)
elif mode==185:
          iptvm3u8blogspot2(url)
elif mode==9778:
          VIPER(url)
elif mode==9779:
          VIPER2(url)
elif mode==9780:
          movie25(url)
elif mode==186:
          sportiptv(url)
elif mode==187:
          iptvonline(url)
elif mode==188:
          PEERSTV(url)
elif mode==189:
          glaztv(url)
elif mode==190:
          muscut(url)
elif mode==191:
          ie(url)
elif mode==192:
          ie2(url)
elif mode==194:
          FILMON(url)
elif mode==195:
          FILMON2()
elif mode==4289:
          CCAM(url)
elif mode==8899:
          torrentcat()
elif mode==198:
          trimtv(url)
elif mode==199:
          ipko(name,url)
elif mode==120:
          elcinema(url)
elif mode==205:
          hongkong(url)
elif mode==206:
          newz(url)
elif mode==1459:
          erase()
elif mode==9788:
          EROTIC(url)
elif mode==9789:
          EROTIC2(url)
elif mode==9711:
          megasearch(url)
elif mode==4290:
          xbmchelper(url)
elif mode==4292:
          hostselect2(url)
elif mode==4291:
          hostselect(url)
elif mode==4927:
          tvplayer(url)
elif mode==4928:
          genccam(url)
elif mode==4555:
          xbmclog(url)
elif mode==4556:
          shadow(url)
elif mode==4557:
          worldstar(url)
elif mode==4559:
          trailers(url)
elif mode==4560:
          SPORTS(url)
elif mode==4561:
          SPORTS2(url,name)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
