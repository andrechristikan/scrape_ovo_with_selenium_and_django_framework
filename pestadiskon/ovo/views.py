from django.http import HttpResponse
from selenium import webdriver
import time
import datetime
import json

# Create your views here.

def writeToJsonFile(data):
    filename = "ovoData.json"

    with open(filename,'w') as fp:
        json.dump(data,fp)



def index(request):
    context = {
        'title':'ovo',
        'description':'Promotion ovo'
    }

    chromedriver = '/Users/andrechristikan/Documents/workspace/python/pestadiskon/static/drivers/chromedriver'
    browser = webdriver.Chrome(chromedriver)
    url = 'https://www.ovo.id/deals'
    browser.get(url)

    time.sleep(3)

    condition = True

    while condition:
        try:
            button = browser.find_elements_by_xpath("/html/body/div/section[3]/div[2]/div/a")[0]
            button.click()
            time.sleep(3)
        except :
            condition = False
            break

    data = browser.find_elements_by_xpath('//*[@id="new"]/article')
    datas = []

    browser2 = webdriver.Chrome(chromedriver)

    for dat in data:

        link = dat.find_element_by_tag_name('a').get_attribute('href')

        browser2.get(link)
        time.sleep(3)

        try:
            print(browser2.find_element_by_class_name('ovo-merchant-content-wrapper').find_element_by_class_name('ovo-deals-merchant-details').find_element_by_tag_name('p').text)

            datas.append(
                {
                    'discountid':'',
                    'short_description':browser2.find_element_by_class_name('ovo-merchant-content-wrapper').find_element_by_tag_name('h3').text,
                    'shop_name':browser2.find_element_by_class_name('ovo-merchant-content-wrapper').find_element_by_class_name('ovo-deals-merchant-text').text,
                    'provider':'ovo',
                    'discount_detail':browser2.find_element_by_class_name('ovo-merchant-content-wrapper').find_element_by_class_name('ovo-deals-merchant-details').find_element_by_tag_name('p').text,
                    'image_url':browser2.find_element_by_class_name('ovo-merchant-image-wrapper').find_element_by_tag_name('img').get_attribute('src'),
                    'discount_start_date':'',
                    'discount_end_date':browser2.find_element_by_class_name('ovo-merchant-content-wrapper').find_element_by_tag_name('h6').text.replace('Berlaku Hingga ',''),
                    'created_at':datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }
            )
        except :
            print(browser2.find_element_by_class_name('ovo-merchant-content-wrapper').find_element_by_class_name('ovo-deals-merchant-details').find_element_by_tag_name('div').text)

            datas.append(
                {
                    'discountid':'',
                    'short_description':browser2.find_element_by_class_name('ovo-merchant-content-wrapper').find_element_by_tag_name('h3').text,
                    'shop_name':browser2.find_element_by_class_name('ovo-merchant-content-wrapper').find_element_by_class_name('ovo-deals-merchant-text').text,
                    'provider':'ovo',
                    'discount_detail':browser2.find_element_by_class_name('ovo-merchant-content-wrapper').find_element_by_class_name('ovo-deals-merchant-details').text,
                    'image_url':browser2.find_element_by_class_name('ovo-merchant-image-wrapper').find_element_by_tag_name('img').get_attribute('src'),
                    'discount_start_date':'',
                    'discount_end_date':browser2.find_element_by_class_name('ovo-merchant-content-wrapper').find_element_by_tag_name('h6').text.replace('Berlaku Hingga ',''),
                    'created_at':datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }
            )


    writeToJsonFile(datas)
    return HttpResponse('success')

    # return render(request,'ovo/index.html',context)
