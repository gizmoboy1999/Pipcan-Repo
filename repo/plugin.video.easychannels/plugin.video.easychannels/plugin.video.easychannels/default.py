import xbmcgui,xbmcplugin
# CREATED BY PIPCAN
# WEB:PIPCAN.INFO 
# SKYPE:PIPCAN2015

# STREAM 1 NAME
name1='  stream1  '
# STREAM 1 URL
link1='http://astvstream3.tulix.tv/gtvtv/gtvtv/playlist.m3u8'

# STREAM 2 NAME
name2='  stream2  '
# STREAM 2 URL
link2='http://astvstream3.tulix.tv/gtvtv/gtvtv/playlist.m3u8'

# STREAM 3 NAME
name3='  stream3  '
# STREAM 3 URL
link3='http://astvstream3.tulix.tv/gtvtv/gtvtv/playlist.m3u8'

# STREAM 4 NAME
name4='  stream4  '
# STREAM 4 URL
link4='http://astvstream3.tulix.tv/gtvtv/gtvtv/playlist.m3u8'

# STREAM 5 NAME
name5='  stream5  '
# STREAM 5 URL
link5='http://astvstream3.tulix.tv/gtvtv/gtvtv/playlist.m3u8'

# STREAM 6 NAME
name6='  stream6  '
# STREAM 6 URL
link6='http://astvstream3.tulix.tv/gtvtv/gtvtv/playlist.m3u8'

# STREAM 7 NAME
name7='  stream7  '
# STREAM 7 URL
link7='http://astvstream3.tulix.tv/gtvtv/gtvtv/playlist.m3u8'

# STREAM 8 NAME
name8='  stream8  '
# STREAM 8 URL
link8='http://astvstream3.tulix.tv/gtvtv/gtvtv/playlist.m3u8'




plugin_handle = int(sys.argv[1])
# ADDON NAME
_id = 'plugin.video.easychannels'
# ICONS DIR
_icondir = "special://home/addons/" + _id + "/icons/"

def add_video_item(url, infolabels, img=''):
    listitem = xbmcgui.ListItem(infolabels['title'], iconImage=img, thumbnailImage=img)
    listitem.setInfo('video', infolabels)
    listitem.setProperty('IsPlayable', 'true')
    xbmcplugin.addDirectoryItem(plugin_handle, url, listitem, isFolder=False)

# TO  ADD STREAM UNCOMMENT LINE                              V----ICONS
add_video_item('%s'% (link1),{ 'title': '%s'% (name1)}, '%s/1.jpg'% _icondir)
add_video_item('%s'% (link2),{ 'title': '%s'% (name2)}, '%s/2.jpg'% _icondir)
add_video_item('%s'% (link3),{ 'title': '%s'% (name3)}, '%s/3.jpg'% _icondir)
#add_video_item('%s'% (link4),{ 'title': '%s'% (name4)}, '%s/4.jpg'% _icondir)
#add_video_item('%s'% (link5),{ 'title': '%s'% (name5)}, '%s/5.jpg'% _icondir)
#add_video_item('%s'% (link6),{ 'title': '%s'% (name6)}, '%s/6.jpg'% _icondir)
#add_video_item('%s'% (link7),{ 'title': '%s'% (name7)}, '%s/7.jpg'% _icondir)
#add_video_item('%s'% (link8),{ 'title': '%s'% (name8)}, '%s/8.jpg'% _icondir)


xbmcplugin.endOfDirectory(plugin_handle)
xbmc.executebuiltin("Container.SetViewMode(500)")

