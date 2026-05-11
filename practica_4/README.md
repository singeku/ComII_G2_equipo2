# Práctica 4: La Modulación de M-PSK y Q-PSK

## 📖 Descripción del Proyecto
Este repositorio documenta el diseño, implementación y simulación de esquemas de modulación digital M-PSK y Q-PSK haciendo uso de Radio Definida por Software (SDR) en el entorno de GNU Radio. 

El objetivo principal de esta práctica es sintetizar estas señales operando estrictamente en el dominio de la **Envolvente Compleja** (banda base), lo que facilita el análisis de la Densidad Espectral de Potencia (PSD) y el mapeo de los símbolos en el plano complejo.

## 👥 Equipo de Trabajo
* **Juan David Camacho González** (Cód: 2210428) 
* **Valentina Arguellez Angulo** (Cód: 2215670) 
* **Jordy Pabón Carrillo** 

## 📁 ¿Qué encontrarás en esta rama?
La rama `practica_4` está dividida en las siguientes carpetas principales:

* **`/GNURadio/`**: Contiene los flujogramas (`.grc`) y los scripts generados en Python. Aquí encontrarás las implementaciones de:
  * El transmisor M-PSK (8-PSK) utilizando tanto el método de Oscilador Controlado por Voltaje (VCO) como el método de Tabla de Verdad.
  * El transmisor Q-PSK ($M=4$) parametrizado con una tasa de símbolos de 32 kBd.
  * Simulaciones del canal introduciendo Ruido Gaussiano Blanco Aditivo (AWGN).
* **`/Informe/`**: Contiene el código fuente en LaTeX (`.tex`) y las imágenes utilizadas para generar el documento final.
  * **`main.pdf`**: El informe final consolidado con el análisis matemático, comparativas de ancho de banda y conclusiones.

## 🚀 Cómo ejecutar las simulaciones
Para visualizar y ejecutar los flujogramas desarrollados en esta práctica:

1. Asegúrate de tener instalado **GNU Radio** en un entorno Linux (Ubuntu recomendado).
2. Clona el repositorio y ubícate en la rama correspondiente:
   `git checkout practica_4`
3. Abre GNU Radio Companion y carga los archivos `.grc` ubicados en la carpeta `/GNURadio/`.
4. Al ejecutar cada flujograma, se desplegará una interfaz gráfica (QT GUI) que permite observar:
   * La señal en el dominio del tiempo.
   * La Densidad Espectral de Potencia (PSD) y la ubicación de los cruces por cero.
   * El diagrama de constelación, donde se evidencia la dispersión de los símbolos al interactuar con el ruido AWGN.

## 🎯 Resultados Destacados
* **Ancho de Banda:** Se corroboró experimentalmente que, al trabajar en Envolvente Compleja, el ancho de banda del lóbulo principal está dictado exclusivamente por la tasa de símbolos ($R_s$).
* **VCO vs. Tabla de Verdad:** Se demostró que ambos métodos de modulación son equivalentes y producen la misma señal en banda base.
* **Constelaciones Inéditas (Punto 8):** Se incluye un análisis sobre geometrías no convencionales (diseñadas por cada integrante) y su vulnerabilidad frente al ruido del canal en comparación con esquemas circulares estándar.
