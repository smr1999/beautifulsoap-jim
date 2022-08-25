from bs4 import BeautifulSoup


if __name__ == '__main__':
    with open('index.html',mode='r') as html_file:
        content = html_file.read()
        
        soup = BeautifulSoup(content,'lxml')
        
        course_cards = soup.find_all('div',class_='card')


        for course in course_cards:
            # print(course.prettify())
            # print(course.h5)
            course_name = course.h5.text
            course_price = course.a.text.split()[-1]
            print(course_name,':',course_price)
        

