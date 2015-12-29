Implement the function escape_html(s), which replaces all instances of:
> with &gt;
< with &lt;
" with &quot;
& with &amp;
and returns the escaped string
Note that your browser will probably automatically render your escaped text as the corresponding symbols, 
but the grading script will still correctly evaluate it.

#1
def escape_html(s):
    for (i,o) in (('&','&amp;'),
                    ('>','&gt;'),
                    ('<','&lt;'),
                    ('"','&quot;')):
        s = s.replace(i,o)
    return s


#2
import cgi
def escape_html(s):
    return cgi.escape(s, quote = True)

print escape_html('"hello, & = &amp;"') #&quot;hello, &amp; = &amp;amp;&quot;
print escape_html('<') #&lt;
print escape_html('"') #&quot;
print escape_html("&") #&amp;
print escape_html("test") #test
