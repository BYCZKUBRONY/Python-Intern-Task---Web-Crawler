
# Python-Intern-Task---Web-Crawler
This is a python script. To run this script:

a)using PyCharm and other python IDE, add URL site  eg 'http://python.org' to the field Parameters in file Running configurations, click apply and ok.Now You can run the script. 

 b) using windows command line, go to folder with script, press shift key and use right mouse button click open command window here. write python or python3 'name of script' 'URL site' click enter. 
I write a class WebCrawler to solve this exercise:
Constructor WebCrawler class. WebCrawler has 5 fields:
'domain' field is set in constructor and not change value during script work.
'site_dictionary' field contain all the accessible pages within that domain in 'domain' field.
'visited_site_list' field contain all pages that script visited already.
 This field prevents Infinite loop(visit the same pages again).
'set_site' field contain all the accessible pages located in URL( 'site_map' method( argument site)).                                     ' set_site' is cleaned every time when 'site_map' is call.
'site_title' field contain HTML `<title>` tag located in URL( 'site_map' method( argument site)).
 def __init__(self, domain):
 self.domain = domain
 self.site_dictionary = {}
 self.visited_site_list = []
 self.set_site = set()
 self.site_title = ""
 This method print a mapping of that 'domain' field.
 def print_dictionary(self):
 This method take argument site(it is a site URL).
 This method use recursion to solve this exercise. 
 This method take title of this site URL, put the name to the self.site_title and
 search in site URL, a site that have 'self.domain' in his URL
 (eg. if in www.abc.org/abcd site URL is www.abc.org/zxc site URL) this www.abc.org/zxc site will be added to the
  set_site set field. In the end of this method self.site_dictionary will be update
  on found site title and set_site.
  def site_map(self, site):
