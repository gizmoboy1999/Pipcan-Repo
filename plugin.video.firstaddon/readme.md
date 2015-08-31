OK LETS READ A PAGE

So you get used to it we will start small, so pick your page you want to read. im going to pick the kodi fourms.

http://forum.kodi.tv/forumdisplay.php?fid=26 

Once on the page right click and view source now this may look hard but this is the code of the website HTML normaly.
click ctrl F and type in the text you are trying to find mine is your first add-on it should now hight light the txt
now the left and right there will be code you want to select the whole line now copy it 

<a href="showthread.php?tid=209948" class=" subject_new" id="tid_209948">Your First Add-On: Hello World!</a></strong> 

now regex has special code to indicate that this is the text you want and to ignore the rest the code is 

EXAMPLES OF REGEX CODE

Read This  --->   (.+?)
Ignore This --->  .+?
read this numbers ---> (\d\d) the \d stands for number so for each \d is one number so (\d\d) would read 2 numbers
a new line ----> \n
before this ---> \b

so look at the code you have copyed

<a href="showthread.php?tid=209948" class=" subject_new" id="tid_209948">Your First Add-On: Hello World!</a></strong>

Now you need to grab the txt that will change but still match what you are trying to grab so

<a href="showthread.php?tid=209948" class=" subject_new" id="tid_209948">Your First Add-On: Hello World!</a></strong>
                            ^^^^^^                  ^^^          ^^^^^^  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  where you see ^ is text that will change on each post so we will start with the name of the post 
  
  "Your First Add-On Hello World"
  
  now like in the regex examples we want to read this so what we do is remove the text "Your First Add-On Hello World"
  and put (.+?) the tell regex that we want this code now you code should look like
  
  <a href="showthread.php?tid=209948" class=" subject_new" id="tid_209948">(.+?)</a></strong>
  
  now the code will fetch the name but as you will see this will only fetch one item becouse 
  
  showthread.php?tid=209948      tid_209948       subject_new
  
  these 3 items can change on each post so to do this i want to add
  
  .+?
  
  this tell regex to ignore this text so lets change it 
    
  FROM  <a href="showthread.php?tid=209948" class=" subject_new" id="tid_209948">(.+?)</a></strong>
  TO    <a href="showthread.php?tid=.+?" class=".+?" id="tid_.+?">(.+?)</a></strong>
  
  Now the reason why i have kept the text showthread.php?tid= is becouse i dont want it to read every link just the posts
  Now you see where it says PUT REGEX CODE you want to copy
  
  <a href="showthread.php?tid=.+?" class=".+?" id="tid_.+?">(.+?)</a></strong>
  
  and paste it in there now we need to tell kodi that we have one item and that we want it to be the name so to do this
  look bellow see where it says GIVE IT A NAME change the text channelid to name all this is a defining the read text nw that   we have given it a name we also need to say add a director each time you read the name so bellow that you should see
  
  addDir('','',10,'')
  
  let me break it down for you 
  
addDir('1','2',3,'4')

1. THE NAME 
2. THE URL
3. THE MODE
4. THE ICON

So with kodi you want to remember this bit of code

%s

This meens put it here basically but how does kodi know what to put there this is dont by adding 

%(name)
  ^--- Put The name Of The Fuction Defined Earlier here    

So now it meens put the text 

<a href="showthread.php?tid=.+?" class=".+?" id="tid_.+?">(.+?)</a></strong>
                                                            ^------- FROM HERE
AND

            addDir('','',10,'')
   PUT IT HERE ----^

but make sure that the %(name)is after the comma so it should look like 
addDir('%s'%(name),'',10,'')

the %s will now put the name there now you can experiment just say you want som text befor the name you can do

addDir('ANY TXT HERE %s OR HERE'%(name),'',,'')

now if you plan on having nothing either side you can do this

addDir(name,'',10,'')

all i have done is removed the '' and put name this tells kodi like the other examples to put the name here now there are
other cool exanples you can use to play with the text these are

CHANGE THE COLOR ----> [COLOR yellow]TXT HERE[/COLOR] SO IN YOUR CODE ----> addDir('[COLOR yellow]%s[/COLOR]'%(name),'',10,'')
BOLD TEXT -----> [COLOR yellow]TXT HERE[/COLOR]

NOW PUT THAT IN WERE IT SAYS REGEXCODE BELOW THAT
BIT SAYS GIVE IT A NAME SO CHANGE channelid TO name NOW AFTER THAT LOOK AT THE addDir NOW THE FIRST ITEM IS THE
NAME SO if you want the name to appper here you could remove to ' ' and just put name or you could put %s in the middle
