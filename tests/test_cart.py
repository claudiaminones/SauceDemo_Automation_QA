from selenium.webdriver.common.by import By

def test_add_to_cart(login_in_driver):
    driver = login_in_driver
    # Elegimos el primer producto
    driver.find_elements(By.CLASS_NAME, "btn_inventory")[0].click()
    # Foto de la acción
    driver.save_screenshot("evidencias/agregando_al_carrito.png")
    
    # Validamos contador
    contador = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert contador == "1", "Error: El contador no marca 1"
    
    # Ir al carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.save_screenshot("evidencias/carrito_final.png")