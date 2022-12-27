class Locators:
    # Login page url
    login_page_url = 'https://opensource-demo.orangehrmlive.com/'

    # Login credentials
    username = 'Admin'
    password = 'admin123'

    # Login page objects
    username_textbox = 'username'
    password_textbox = 'password'
    login_button = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    drop_down_menu = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/i'

    # Home page objects
    user_menu_link = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p'
    logout_link = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a'

    # Logout page objects
    logout_link_text = 'Logout'
