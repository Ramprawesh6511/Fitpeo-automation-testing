import traceback
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Invoking browser
driver = webdriver.Chrome()
#Navigate to the Fitpeo Homepage
driver.get("https://www.fitpeo.com/")
driver.maximize_window()
time.sleep(5)

# Navigate to the Revenue Calculator page
driver.implicitly_wait(5)
revenue_calculator = driver.find_element(By.XPATH, "//div[contains(text(),'Revenue Calculator')]")
revenue_calculator.click()
time.sleep(5)
try:
    # Scroll Down to the Slider Section
    slider = driver.find_element(By.XPATH,"//span[contains(@class, 'MuiSlider-thumbSizeMedium')]")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", slider)
    time.sleep(5)

    # Adjust the Slider
    actions = ActionChains(driver)
    actions.click_and_hold(slider).pause(1).move_by_offset(94,0).release().perform()
    time.sleep(5)

    # Update the Text Field An validate :
    element_to_click = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,"//div[@class='MuiInputBase-root MuiOutlinedInput-root MuiInputBase-colorPrimary MuiInputBase-formControl MuiInputBase-sizeSmall css-129j43u']"))
    )
    actions = ActionChains(driver)
    actions.move_to_element(element_to_click).click().perform()
    #update text
    actions.click(element_to_click).key_down(Keys.CONTROL).send_keys("560").key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE).perform()
    actions.send_keys("560").perform()
    time.sleep(2)
    actions.click_and_hold(slider).pause(1).move_by_offset(39,0).release().perform()
    time.sleep(5)

    # VERIFY the revenue page:
    WebDriverWait(driver, 10).until(
        EC.url_contains("https://www.fitpeo.com/revenue-calculator")
    )
    print("revenue page loaded")

    #Select CPT Codes:
    element1 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.MuiBox-root.css-3f59le > div.MuiBox-root.css-rfiegf > div.MuiBox-root.css-1p19z09 > div:nth-child(1) > label > span.MuiButtonBase-root.MuiCheckbox-root.MuiCheckbox-colorPrimary.MuiCheckbox-sizeMedium.PrivateSwitchBase-root.MuiCheckbox-root.MuiCheckbox-colorPrimary.MuiCheckbox-sizeMedium.MuiCheckbox-root.MuiCheckbox-colorPrimary.MuiCheckbox-sizeMedium.css-1sp9p8c > svg"))
    )
    # Scroll down further:
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element1)
    print("Element scrolled into view")
    actions.move_to_element(element1).click().perform()

    element2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.MuiBox-root.css-3f59le > div.MuiBox-root.css-rfiegf > div.MuiBox-root.css-1p19z09 > div:nth-child(2) > label > span.MuiButtonBase-root.MuiCheckbox-root.MuiCheckbox-colorPrimary.MuiCheckbox-sizeMedium.PrivateSwitchBase-root.MuiCheckbox-root.MuiCheckbox-colorPrimary.MuiCheckbox-sizeMedium.MuiCheckbox-root.MuiCheckbox-colorPrimary.MuiCheckbox-sizeMedium.css-1sp9p8c > svg"))
    )
    actions.move_to_element(element2).click().perform()
    time.sleep(5)

    element3 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.MuiBox-root.css-3f59le > div.MuiBox-root.css-rfiegf > div.MuiBox-root.css-1p19z09 > div:nth-child(3) > label > span.MuiButtonBase-root.MuiCheckbox-root.MuiCheckbox-colorPrimary.MuiCheckbox-sizeMedium.PrivateSwitchBase-root.MuiCheckbox-root.MuiCheckbox-colorPrimary.MuiCheckbox-sizeMedium.MuiCheckbox-root.MuiCheckbox-colorPrimary.MuiCheckbox-sizeMedium.css-1sp9p8c > svg"))
    )
    actions.move_to_element(element3).click().perform()
    time.sleep(5)

    element4 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.MuiBox-root.css-3f59le > div.MuiBox-root.css-rfiegf > div.MuiBox-root.css-1p19z09 > div:nth-child(8) > label > span.MuiButtonBase-root.MuiCheckbox-root.MuiCheckbox-colorPrimary.MuiCheckbox-sizeMedium.PrivateSwitchBase-root.MuiCheckbox-root.MuiCheckbox-colorPrimary.MuiCheckbox-sizeMedium.MuiCheckbox-root.MuiCheckbox-colorPrimary.MuiCheckbox-sizeMedium.css-1sp9p8c > svg"))
    )
    # Scroll down
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element4)
    actions.move_to_element(element4).click().perform()
    time.sleep(5)

    # Validate Total Recurring Reimbursement: Header text
    header_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.MuiBox-root.css-3f59le > div.MuiBox-root.css-rfiegf > header > div > p:nth-child(4) > p"))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", header_element)
    actions.move_to_element(header_element).perform()

    # Extract the header text
    header_text = header_element.text
    print(f"Header Text: {header_text}")

    # Validate the header text
    expected_value = "$110160"
    if expected_value in header_text:
        print("Validation passed: Header displays the correct value.")
    else:
        print(f"Validation failed: Expected value '{expected_value}' not found in '{header_text}'.")


except Exception as e:
    print(f"An error occurred: {e}")
    traceback.print_exc()
finally:
    driver.quit()
