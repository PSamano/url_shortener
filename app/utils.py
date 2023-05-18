import random
import string

# Función para generar un shortcode de longitud específica
def generate_shortcode(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
