import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# 1. Configuración
NUM_REGISTROS = 5000
FECHA_INICIO = datetime(2023, 1, 1)
FECHA_FIN = datetime(2024, 12, 31)

# 2. Listas de Datos Maestros
productos = [
    {"id": "PROD001", "nombre": "Laptop Gamer X1", "categoria": "Laptops", "precio": 1200, "costo": 800},
    {"id": "PROD002", "nombre": "Laptop Ultrabook Air", "categoria": "Laptops", "precio": 950, "costo": 600},
    {"id": "PROD003", "nombre": "Monitor 4K 27p", "categoria": "Monitores", "precio": 350, "costo": 200},
    {"id": "PROD004", "nombre": "Monitor Curvo 32p", "categoria": "Monitores", "precio": 450, "costo": 280},
    {"id": "PROD005", "nombre": "Mouse Inalámbrico Pro", "categoria": "Periféricos", "precio": 45, "costo": 20},
    {"id": "PROD006", "nombre": "Teclado Mecánico RGB", "categoria": "Periféricos", "precio": 85, "costo": 40},
    {"id": "PROD007", "nombre": "Auriculares Noise Cancel", "categoria": "Audio", "precio": 120, "costo": 70},
    {"id": "PROD008", "nombre": "Disco SSD 1TB", "categoria": "Almacenamiento", "precio": 90, "costo": 50},
]

paises = ["Perú", "Colombia", "México", "Chile", "Argentina"]
canales = ["Tienda Física", "Online", "Distribuidor"]

# 3. Generación de Datos
data = []

dias_totales = (FECHA_FIN - FECHA_INICIO).days

for i in range(NUM_REGISTROS):
    fecha = FECHA_INICIO + timedelta(days=random.randint(0, dias_totales))
    prod = random.choice(productos)
    pais = random.choice(paises)
    canal = random.choice(canales)
    cantidad = random.randint(1, 5)
    
    # Lógica de descuento: más descuento si compra más
    descuento_pct = 0.0
    if cantidad >= 3:
        descuento_pct = 0.10  # 10% descuento
    
    precio_venta = prod["precio"]
    venta_total = precio_venta * cantidad * (1 - descuento_pct)
    costo_total = prod["costo"] * cantidad
    utilidad = venta_total - costo_total
    
    data.append({
        "ID_Venta": f"V-{10000+i}",
        "Fecha": fecha.strftime("%Y-%m-%d"),
        "ID_Producto": prod["id"],
        "Producto": prod["nombre"],
        "Categoria": prod["categoria"],
        "Pais": pais,
        "Canal": canal,
        "Cantidad": cantidad,
        "Precio_Unitario": precio_venta,
        "Descuento_Pct": descuento_pct,
        "Venta_Total": round(venta_total, 2),
        "Costo_Total": costo_total,
        "Utilidad": round(utilidad, 2)
    })

# 4. Exportar a CSV
df = pd.DataFrame(data)
df.to_csv("Ventas_TechZone.csv", index=False, encoding='utf-8-sig')
print("¡Archivo 'Ventas_TechZone.csv' generado con éxito!")