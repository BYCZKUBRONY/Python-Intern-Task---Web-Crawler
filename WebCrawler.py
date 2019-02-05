import urllib.request
import sys


class WebCrawler:
    # Constructor WebCrawler class. WebCrawler has 5 fields:
    # 'domain' field is set in constructor and not change value during script work.
    # 'site_dictionary' field contain all the accessible pages within that domain in 'domain' field.
    # 'visited_site_list' field contain all pages that script visited already.
    #  This field prevents Infinite loop(visit the same pages again).
    #  'set_site' field contain all the accessible pages located in URL( 'site_map' method( argument site)).
    #  ' set_site' is cleaned every time when 'site_map' is call.
    #  'site_title' field contain HTML `<title>` tag located in URL( 'site_map' method( argument site)).
    def __init__(self, domain):
        self.domain = domain
        self.site_dictionary = {}
        self.visited_site_list = []
        self.set_site = set()
        self.site_title = ""

    # This method print a mapping of that 'domain' (field 'self.site_dictionary')
    def print_dictionary(self):
        print(self.site_dictionary)

    # This method take argument site(it is a site URL).
    # This method take title of this site URL, put the name to the self.site_title and
    #  search in site URL, a site that have 'self.domain' in his URL
    # (eg. if in www.abc.org/abcd site URL is www.abc.org/zxc site URL) this www.abc.org/zxc site will be added to the
    # set_site set field. In the end of this method self.site_dictionary will be update
    #  on found site title and set_site.
    def site_map(self, site):
        self.site_title = ""
        self.set_site = set()
        self.visited_site_list.append(site)
        try:
            # In this place script open url(site)
            with urllib.request.urlopen(site) as response:
                # In this place script read lines from response variable and put to the html list.
                html = response.readlines()
                html_as_string = []
                for line in html:
                    # Here script decode the html.
                    html_as_string.append(line.decode("utf-8"))
                # This for section script search a title of self.site.
                for element in html_as_string:
                    if element.__contains__('<title>'):
                        elements_after_split_element_variable = element.split('>')
                        array_with_elements_after_split_elements_after_split_element_variable = \
                            elements_after_split_element_variable[1].split('<')
                        self.site_title = array_with_elements_after_split_elements_after_split_element_variable[0]
                        break
                # This for section search url sites link,check that this url sites link contain self.domain,
                # on the beginning of this url site link.
                # If yes, check that this url site link not exist in self.set_site
                #  If not add this url site link to the self.set_site set.
                for element in html_as_string:
                    if element.__contains__('href="') and element.__contains__(self.domain):
                        strings_in_html_pass_if_conditions_splitted = element.split('href="')
                        for element_in_string_in_html_pass_if_conditions_splitted_variable \
                                in strings_in_html_pass_if_conditions_splitted:
                            if element_in_string_in_html_pass_if_conditions_splitted_variable.startswith(self.domain):
                                variable_need_to_find_pages_startswith_self_domain = \
                                    element_in_string_in_html_pass_if_conditions_splitted_variable.split('"')
                                set_site_not_contain_this_site = True
                                for element_in_self_set_site in self.set_site:
                                    if element_in_self_set_site\
                                            == variable_need_to_find_pages_startswith_self_domain[0]:
                                        set_site_not_contain_this_site = False
                                        break
                                if set_site_not_contain_this_site:
                                    self.set_site.add(variable_need_to_find_pages_startswith_self_domain[0])
                                continue
                # Script added new element to the self.site_dictionary.
                self.site_dictionary[site] = {self.site_title: self.set_site}
                response.close()

                # In this if section if self.set_site have a element( url site link),
                # and this url site link was not visited yet, script call self.site_map(element) method
                #  with this url site link like a argument of this method.
                # This is recursion way to solve this exercise.
                if len(self.set_site) > 0:
                    for url_site_link in self.set_site:
                        if self.visited_site_list.__contains__(url_site_link):
                            continue
                        self.site_map(url_site_link)
        except UnicodeDecodeError:
            sys.stderr.write("'utf-8' codec can't decode byte")


webcrawler = WebCrawler(sys.argv[1])
webcrawler.site_map(webcrawler.domain)
webcrawler.print_dictionary()
