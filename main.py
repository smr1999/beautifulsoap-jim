from bs4 import BeautifulSoup


if __name__ == '__main__':
    with open('index.html',mode='r') as html_file:
        content = html_file.read()
        
        soup = BeautifulSoup(content,'lxml')
        #print(soup.prettify())
        
        # tags = soup.find('h5') # Just find first h5 tag
        # print(tags)

        courses_html_tags = soup.find_all('h5')
        # print(courses_html_tags)
        
        for course in courses_html_tags:
            print(course.text)
        
