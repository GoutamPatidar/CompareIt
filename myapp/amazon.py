

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from bs4 import BeautifulSoup

def link_generator(name):
    product_req = name
    new_pro_req = product_req.replace(" ", "+")

    url = 'https://www.amazon.in/s?k=' + new_pro_req + '&crid=2ZL677QUVV68Q&sprefix=' + new_pro_req + '%2Caps%2C246&ref=nb_sb_ss_ts-doa-p_1_4'
    print(url)
   


    # Set up Microsoft Edge WebDriver
    edge_options = Options()
    edge_options.use_chromium = True
    edge_options.add_argument('--headless') #for not opening the the browswer pop up
   
    driver = webdriver.Edge(service=Service('E:/Main_project/compareit/env/Scripts/edgedriver_win64/msedgedriver.exe'), options=edge_options) # Replace 'path_to_edgedriver' with the actual path to the downloaded Edge WebDriver executable
    driver.get(url)# Use the WebDriver to navigate to the URL

    driver.implicitly_wait(10)# Wait for the page to load (you can use explicit waits here if needed)
    page_source = driver.page_source# Get the page source after the JavaScript has executed
   
    req_content = BeautifulSoup(page_source, 'html.parser') # Parse the page source with BeautifulSoup
    # print(req_content)
  
    img=[]  
    name=[]
    links=[]
    price=[]
    rating=[]
    del_li=[]

    # Find links using BeautifulSoup
    data_cont_img_imp = req_content.find_all('div', {'class': 's-product-image-container aok-relative s-text-center s-image-overlay-grey puis-image-overlay-grey s-padding-left-small s-padding-right-small puis-spacing-small s-height-equalized puis puis-v2q9dos4w4qqgu20zj8pkw7yd24'})
    data_cont_data_imp=req_content.find_all('div',{'class':'a-section a-spacing-small puis-padding-left-small puis-padding-right-small'})
    data_cont_img_imp_try = req_content.find_all('div', {'class': 's-product-image-container aok-relative s-text-center s-image-overlay-grey puis-image-overlay-grey s-padding-left-small s-padding-right-small puis-spacing-small s-height-equalized puis puis-v2q9dos4w4qqgu20zj8pkw7yd24'})

    # print(data_cont_img_imp)
    # print("               //////////////////////////////////////////////////\n////////////////////////\n")
    # print(data_cont_data_imp)

    if data_cont_img_imp and data_cont_data_imp:#used for horizontal page
        print("Trying to access the data [Block 1] into given page......................................")

        for item in data_cont_data_imp:  # Use 'item' as the loop variable for data extraction
            href_link=""
            rest_link = item.find('a', {'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
            if rest_link is not None and 'href' in rest_link.attrs:
                href_link = 'https://www.amazon.in/' + rest_link['href']
                links.append(href_link)

            name_list = item.find('span', attrs={'class': 'a-size-base-plus a-color-base a-text-normal'})
            price_list = item.find('span', attrs={'class': 'a-offscreen'}) 
            rating_list = item.find('span', attrs={'class': 'a-icon-alt'})  

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
            img_list = item.find('img', {'class': 's-image'})
            if img_list is not None and 'src' in img_list.attrs:
                href_img = img_list['src']
                if href_img is not None:
                    img.append(href_img)

    elif data_cont_img_imp_try:

        data_cont_img_imp = req_content.find_all('div', {'class': 's-product-image-container aok-relative s-text-center s-image-overlay-grey puis-image-overlay-grey s-padding-left-small s-padding-right-small puis-spacing-small s-height-equalized puis puis-vnjufzhntlqm11zjo2xc51q7r1'})
        data_cont_data_imp=req_content.find_all('div',{'a-section a-spacing-small puis-padding-left-micro puis-padding-right-micro'})


        print("Trying to access the data [Block 2] into given page......................................")

        for item in data_cont_data_imp:  # Use 'item' as the loop variable for data extraction
            href_link=""
            rest_link = item.find('a', {'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
            if rest_link is not None and 'href' in rest_link.attrs:
                href_link = 'https://www.amazon.in/' + rest_link['href']
                links.append(href_link)
            campanyname=item.find('span', attrs={'class': 'a-size-base-plus a-color-base'})
            name_list = item.find('span', attrs={'class': 'a-size-base-plus a-color-base a-text-normal'})
            price_list = item.find('span', attrs={'class': 'a-price-whole'}) 
            rating_list = item.find('span', attrs={'class': 'a-icon-alt'})  

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
            img_list = item.find('img', {'class': 's-image'})
            if img_list is not None and 'src' in img_list.attrs:
                href_img = img_list['src']
                if href_img is not None:
                    img.append(href_img)





    else :#use for vertical page
        data_cont_img_imp = req_content.find_all('div', {'class': 'puisg-col puisg-col-4-of-12 puisg-col-4-of-16 puisg-col-4-of-20 puisg-col-4-of-24 puis-list-col-left'})
        data_cont_data_imp=req_content.find_all('div',{'puisg-col puisg-col-4-of-12 puisg-col-8-of-16 puisg-col-12-of-20 puisg-col-12-of-24 puis-list-col-right'})

        if data_cont_img_imp and data_cont_data_imp:
            print("Trying to access the data [Block 3] into given page......................................")

            for item in data_cont_data_imp:   # Use 'item' as the loop variable for data extraction
                href_link=""
                rest_link = item.find('a', {'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
                if rest_link is not None and 'href' in rest_link.attrs:
                    href_link = 'https://www.amazon.in/' + rest_link['href']
                    links.append(href_link)

                name_list = item.find('span', attrs={'class': 'a-size-medium a-color-base a-text-normal'}) # Use 'item.find' here
                price_list = item.find('span', attrs={'class': 'a-offscreen'})  # Use 'item.find' here
                rating_list = item.find('span', attrs={'class': 'a-icon-alt'})  # Use 'item.find' here

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
                img_list = item.find('img', {'class': 's-image'})
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
