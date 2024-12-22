from selenium import webdriver
from selenium.webdriver.common.by import By
from time import time


def apply_buy_policy(driver: webdriver.Firefox):
    # check all available upgrades
    available_upgrades = driver.find_elements(By.CSS_SELECTOR, value="#store b")
    available_upgrades_names = [item.text for item in available_upgrades]

    current_money = driver.find_element(By.ID, value="money").text
    current_money = int(current_money.strip().replace(",", ""))

    # buy the most expensive upgrade
    for i in range(len(available_upgrades_names) - 2, -1, -1):
        upgrade_cost = available_upgrades_names[i].split("-")[1]
        upgrade_cost = int(upgrade_cost.strip().replace(",", ""))

        if current_money >= upgrade_cost:
            available_upgrades[i].click()
            current_money = driver.find_element(By.ID, value="money").text
            current_money = int(current_money.strip().replace(",", ""))


def main():
    firefox_options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=firefox_options)

    driver.get("http://orteil.dashnet.org/experiments/cookie/")

    # setting time limits
    end_time = time() + 300       # five minutes from now
    buy_time = time() + 5       # buy something every five minutes

    # getting the cookie
    cookie = driver.find_element(By.ID, value="cookie")

    # bot loop
    gaming = True
    while gaming:
        if time() > end_time:
            # get final cookies per click (cpc)
            print(f'final {driver.find_element(By.ID, value="cps").text}')
            driver.quit()
            break

        if time() > buy_time:
            apply_buy_policy(driver)
            buy_time = time() + 5

        cookie.click()


if __name__ == "__main__":
    main()
