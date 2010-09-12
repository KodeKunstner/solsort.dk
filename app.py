import content

google_analytics="""<script type="text/javascript">var _gaq=[['_setAccount', 'UA-8354880-3'],['_trackPageview']];</script><script type="text/javascript" src="http://www.google-analytics.com/ga.js"></script>"""

def header(title):
    return 'Content-Type: application/xhtml+xml; charset=UTF-8\n\n' \
        + '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">' \
        + '<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">' \
        + '<head>' \
        + '<title>' + title + '</title>' \
        + '<link rel="icon" href="/favicon.ico" />' \
        + '<link rel="stylesheet" type="text/css" href="static/style.css" />' \
        + '<meta http-equiv="content-type" content="application/xhtml+xml; charset=UTF-8" />' \
        + google_analytics \
        + "</head><body>" 

def readStaticFile(fname):
    return  os.path.join(os.path.dirname(__file__), "static", fname)

def simplebody():
    return '<div><img class="portrait" src="static/rasmuserik.jpg" alt="portrait" /></div>' \
        + content.address \
        + '<div class="small">' \
        + content.keywords \
        + '</div>'

def footer():
    return '</body></html>'

print header("solsort.dk") + simplebody() + footer()

