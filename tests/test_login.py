def test_login_validation(login_in_driver):
    driver = login_in_driver
    driver.save_screenshot("evidencias/login_ok.png")
    assert "/inventory.html" in driver.current_url, "Error: No se redirigió al inventario"