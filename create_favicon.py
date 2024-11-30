from PIL import Image

# Открываем исходное изображение
img = Image.open('/home/ivan/Desktop/gub_lic_site2/static/images/logo.jpg')

# Конвертируем в RGB режим
img_rgb = img.convert('RGB')

# Изменяем размер до 32x32 пикселя
img_resized = img_rgb.resize((32, 32), Image.LANCZOS)

# Сохраняем как favicon
img_resized.save('/home/ivan/Desktop/gub_lic_site2/static/favicon.ico', format='ICO')
