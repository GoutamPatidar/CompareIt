

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from bs4 import BeautifulSoup

def link_generator(name):
    product_req = name
    new_pro_req = product_req.replace(" ", "%20")

    url = 'https://www.flipkart.com/search?q=' + new_pro_req + '&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off'
    print(url)
   


    # Set up Microsoft Edge WebDriver
    edge_options = Options()
    edge_options.use_chromium = True
    edge_options.add_argument('--headless') #for not opening the the browswer pop up
   
    driver = webdriver.Edge(service=Service('C:/Users/PATIDAR_G_/edgedriver_win64'), options=edge_options) # Replace 'path_to_edgedriver' with the actual path to the downloaded Edge WebDriver executable
    driver.get(url)# Use the WebDriver to navigate to the URL

    driver.implicitly_wait(20)# Wait for the page to load (you can use explicit waits here if needed)
    page_source = driver.page_source# Get the page source after the JavaScript has executed
   
    req_content = BeautifulSoup(page_source, 'html.parser') # Parse the page source with BeautifulSoup
  
    img=[]  
    name=[]
    links=[]
    price=[]
    rating=[]
    del_li=[]

    # Find links using BeautifulSoup
    data_cont_img_imp = req_content.find_all('a', {'class': '_2rpwqI'})
    data_cont_data_imp=req_content.find_all('div',{'_4ddWXP'})
    data_cont_img_imp_try = req_content.find_all('div', {'class': '_1xHGtK _373qXS'})
  
    if data_cont_img_imp and data_cont_data_imp:#used for horizontal page
        print("Trying to access the data [Block 1] into given page......................................")

        for item in data_cont_data_imp:  # Use 'item' as the loop variable for data extraction
            href_link=""

            rest_link = item.find('a', {'class': 's1Q9rs'})
            if rest_link is not None and 'href' in rest_link.attrs:
                href_link = 'https://www.flipkart.com/' + rest_link['href']
                links.append(href_link)

            name_list = item.find('a', attrs={'class': 's1Q9rs'})
            price_list = item.find('div', attrs={'class': '_30jeq3'}) 
            rating_list = item.find('div', attrs={'class': '_3LWZlK'})  

            if price_list is None or name_list is None:
                del_li.append(href_link)  # This is used to check if there any link with do not have price and name so we can delete it later
                continue
            
            
            name.append(name_list.text.strip())
            rating.append(rating_list.text.strip() if rating_list is not None else "")
            price_temp = price_list.text.strip()
            price_temp = price_temp.replace('₹', '')
            price_temp = price_temp.replace(',', '')
            price.append(float(price_temp))


        for item in data_cont_img_imp:  # Use 'item' as the loop variable  for img extraction
            img_list = item.find('img', {'class': '_396cs4'})
            if img_list is not None and 'src' in img_list.attrs:
                href_img = img_list['src']
                if href_img is not None:
                    img.append(href_img)


    elif data_cont_img_imp_try:
        
        data_cont_img_imp = req_content.find_all('div', {'class': '_3ywSr_'})
        data_cont_data_imp=req_content.find_all('div',{'_1xHGtK _373qXS'})


        print("Trying to access the data [Block 2] into given page......................................")

        for item in data_cont_data_imp:  # Use 'item' as the loop variable for data extraction
            href_link=""

            rest_link = item.find('a', {'class': 'IRpwTa'})
            if rest_link is not None and 'href' in rest_link.attrs:
                href_link = 'https://www.flipkart.com/' + rest_link['href']
                links.append(href_link)

            campanyname=item.find('div', attrs={'class': '_2WkVRV'})
            name_list = item.find('a', attrs={'class': 'IRpwTa'})
            price_list = item.find('div', attrs={'class': '_30jeq3'}) 
            rating_list = item.find('div', attrs={'class': '_3LWZlK'})  

            if price_list is None or name_list is None:
                del_li.append(href_link)  # This is used to check if there any link with do not have price and name so we can delete it later
                continue
            
            
            name.append(campanyname.text.strip() + name_list.text.strip())
            rating.append(rating_list.text.strip() if rating_list is not None else "")
            price_temp = price_list.text.strip()
            price_temp = price_temp.replace('₹', '')
            price_temp = price_temp.replace(',', '')
            price.append(float(price_temp))


        for item in data_cont_img_imp:  # Use 'item' as the loop variable  for img extraction
            img_list = item.find('img', {'class': '_2r_T1I'})
            if img_list is not None and 'src' in img_list.attrs:
                href_img = img_list['src']
                if href_img is not None:
                    img.append(href_img)


    else:#use for vertical page
        data_cont_img_imp = req_content.find_all('div', {'class': '_2QcLo-'})
        data_cont_data_imp=req_content.find_all('div',{'_2kHMtA'})

        if data_cont_img_imp and data_cont_data_imp:
            print("Trying to access the data [Block 3] into given page......................................")

            for item in data_cont_data_imp:   # Use 'item' as the loop variable for data extraction
                href_link=""
    
                rest_link = item.find('a', {'class': '_1fQZEK'})
                if rest_link is not None and 'href' in rest_link.attrs:
                    href_link = 'https://www.flipkart.com/' + rest_link['href']
                    links.append(href_link)

                name_list = item.find('div', attrs={'class': '_4rR01T'}) # Use 'item.find' here
                price_list = item.find('div', attrs={'class': '_30jeq3 _1_WHN1'})  # Use 'item.find' here
                rating_list = item.find('div', attrs={'class': '_3LWZlK'})  # Use 'item.find' here

                if price_list is None or name_list is None:
                    del_li.append(href_link)  # This is used to check if there any link with do not have price and name so we can delete it later
                    continue
                # print(name_list)
                # print(name_list.text.strip())
                name.append(name_list.text.strip())

                rating.append(rating_list.text.strip() if rating_list is not None else "")
                price_temp = price_list.text.strip()
                price_temp = price_temp.replace('₹', '')
                price_temp = price_temp.replace(',', '')
                price.append(float(price_temp))


            for item in data_cont_img_imp:  # Use 'item' as the loop variable  for img extraction
                img_list = item.find('img', {'class': '_396cs4'})
                if img_list is not None and 'src' in img_list.attrs:
                    href_img = img_list['src']
                    if href_img is not None:
                        img.append(href_img)

        else:
            print("HTML PARSING ERROR.....................................................")

    # Close the WebDriver
    driver.quit()

    print("Scraping done successfully. Found  ", len(links),"links ", len(price)," Names ", len(name)," Prices ",len(rating)," rating ",len(img), "Images")
    
    for i in del_li:  # removing unncesssary links
        try:
            links.remove(i)
        except:
            print("Item is not found in deleteing list",i)

    combined_array = []
    for index, (element1, element2, element3, element4, element5) in enumerate(zip( img, name, rating, price, links)):
        combined_array.append((index, element1, element2, element3, element4, element5))


    print("Lists of itms is sending .......................................................")
    sorted_price_list = sorted(combined_array, key=lambda x: x[4])
    # for i in sorted_price_list:
    #     print(i)

    return sorted_price_list

# Call the function and pass the product name as an argument
# product_name = input("Enter product name: ")

# print(link_generator(product_name))

def main(name):
    return link_generator(name)
