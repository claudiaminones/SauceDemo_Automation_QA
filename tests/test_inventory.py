from selenium.webdriver.common.by import By

def test_inventory_items(login_in_driver):
    driver = login_in_driver
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    driver.save_screenshot("evidencias/inventario_lista.png")
    assert len(productos) > 0, "Error: La lista de productos está vacía"