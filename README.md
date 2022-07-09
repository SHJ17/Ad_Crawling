# Ad_Crawling
My first crawling code (and this is the one survived from numerous errors)

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
