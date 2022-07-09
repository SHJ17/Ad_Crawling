# Ad_Crawling
My first crawling code (and this is the one survived from numerous errors)
# Prerequisites
You should donwload the right version of chromedriver. You can easily do this following a few steps...

Open Chrome -> Settings -> About Chrome

Now you'll see the version of your Chrome. Then you should download the right driver from
https://chromedriver.chromium.org/downloads

# How to modify the code according to websites
First, open the website you want to crawl the images in it.

Then open DevTools. Now find the specific "class" that those images have in common...

In the code I used

    class_='row w_banner'
    
You should find the appropriate one(but it is so easy in most cases, don't worry)

#
For the part         

    filename, headers = opener.retrieve(i, str(n)+'.jpg')

You can change the name of the file to your preference.
