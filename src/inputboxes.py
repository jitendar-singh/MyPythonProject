
from drivers import *

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html")

'''
    1- How to find how many input boxes present in web page
    2- How to provide value into textbox
    3- How to get status of textbox
'''
inputboxes = driver.find_elements(By.CLASS_NAME, 'text_field')
print(len(inputboxes))


driver.find_element(By.ID, 'RESULT_TextField-1').send_keys("Jitendar")
driver.find_element_by_id('RESULT_TextField-2').send_keys("Singh")




