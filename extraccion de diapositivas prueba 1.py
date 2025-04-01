#PRIMERA PRUEBA
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from fpdf import FPDF

# 🔹 Configurar Selenium con tu perfil de Chrome
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\Angel Temporal\\AppData\\Local\\Google\\Chrome\\User Data")  # Ruta de tu perfil
options.add_argument("profile-directory=Default")  # Usa el perfil principal

# 🔹 Iniciar Chrome con el perfil cargado
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 🔹 Ir a la URL
driver.get("https://www.steamvirtual.com/mod/scorm/player.php")

# 🔹 Esperar manualmente a que inicies sesión
input("⚠️ **INICIA SESIÓN MANUALMENTE EN EL NAVEGADOR ABIERTO.**\nPresiona Enter en esta consola cuando hayas terminado...")

# 🔹 Maximizar la ventana
driver.maximize_window()

# 🔹 Selector del botón "Siguiente"
next_button_selector = "button.component_base.next"

screenshot_paths = []

try:
    for i in range(50):  # Máximo 50 diapositivas
        # Capturar screenshot
        screenshot_name = f"slide_{i}.png"
        driver.save_screenshot(screenshot_name)
        screenshot_paths.append(screenshot_name)
        print(f"Diapositiva {i+1} capturada ✅")

        # Avanzar a la siguiente diapositiva
        next_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, next_button_selector))
        )
        next_button.click()
        time.sleep(2)  # Más tiempo para carga dinámica

except Exception as e:
    print(f"Fin de las diapositivas o error: {str(e)}")

finally:
    # Preguntar si cerrar el navegador
    cerrar = input("¿Cerrar el navegador? (s/n): ").lower()
    if cerrar == "s":
        driver.quit()

# 🔹 Generar PDF
if screenshot_paths:
    pdf = FPDF()
    for image in screenshot_paths:
        pdf.add_page()
        pdf.image(image, x=0, y=0, w=210, h=297)  # Ajusta si la proporción es diferente
    pdf.output("presentacion_nueva.pdf")
    print("¡PDF generado: presentacion_nueva.pdf! 🚀")

    # 🔹 Limpiar imágenes temporales
    for image in screenshot_paths:
        os.remove(image)
else:
    print("Error: No se capturaron diapositivas ⚠️")