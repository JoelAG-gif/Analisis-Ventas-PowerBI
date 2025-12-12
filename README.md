# 🛒 Dashboard de Análisis de Ventas - Gran Distribución (Retail)

Este proyecto consiste en un tablero interactivo de Power BI diseñado para realizar un análisis detallado del rendimiento comercial, la rentabilidad y el cumplimiento presupuestario de las ventas en una cadena de tiendas de distribución.

## 📊 Galería del Reporte

### 1. Vista General y Comparativa entre Tiendas (2012)
![Vista General](ventas%20x%20tienda.png)
* **Filtros Activos:** Análisis comparativo centrado en la Tienda Alicante 01 y la Tienda La Coruña.
* **KPIs Agregados:** La venta acumulada (YTD) total de las tiendas filtradas es de 75.21 mil, con un déficit presupuestario del -14.53% (12.79 mil).
* **Evolución YTD:** La gráfica de área (derecha) muestra la tendencia de Venta (verde oscuro) siempre por debajo del Presupuesto (verde claro) a lo largo de 2012.

### 2. Rendimiento por Subfamilia y Rentabilidad (Tienda Alicante 01, 2012)
![Rendimiento Subfamilia](tienda%20x%20subfamilia.png)
Este segmento se enfoca en la distribución de la venta y el margen de beneficio por categoría de producto, siendo el punto de enfoque la Tienda Alicante 01.
* **Venta por Volumen (Importe Venta):** Las subfamilias que generan mayor volumen de ingresos son Alimentación (97 mil), Refrescos y Bebidas (58 mil) y Golosinas y Chocolates (57 mil).
* **Rentabilidad (Beneficio %):** Las categorías más rentables son Refrescos y Bebidas (44.22%) y Juegos y Complementos (41.84%).
* **Punto Crítico:** La subfamilia Prensa y Revistas no solo es de bajo volumen, sino que genera una pérdida significativa de -9.68% en el beneficio.

### 3. Detalle Mensual y Desempeño Presupuestario (Tienda Alicante 01, 2012)
![Detalle Mensual](detalle%20mensual.png)
| Indicador | Valor Total (2012) | Observaciones Clave |
| :--- | :--- | :--- |
| **Venta Anual** | 223.29 mil | La venta total del año está registrada. |
| **Beneficio Anual** | 7.14 mil (18.22 %) | El margen de beneficio anual promedio es positivo. |
| **Desfase Presupuestario** | -73.82 % | La tienda no cumplió su meta presupuestaria, indicando que las ventas reales fueron sustancialmente menores a las planificadas. Este déficit se mantuvo constante mes a mes. |
| **Detalle YTD** | Acumulado mes a mes | Los campos YTD (Year To Date) muestran el acumulado de Venta y Presupuesto, alcanzando el total al finalizar Diciembre. |



---

## 🛠️ Herramientas y Metodología Utilizada

* **Power BI Desktop:** Modelado de datos y diseño de visualizaciones interactivas.
* **DAX:** Implementación de medidas para cálculos de diferencias porcentuales ($\text{DifPresup}\%$), beneficio ($\text{Beneficio}\%$) y acumulados anuales ($\text{YTD}$).
* **ETL (Power Query):** Proceso de limpieza, transformación y carga de datos desde las fuentes operacionales.

---
*Desarrollado por [Tu Nombre]*
