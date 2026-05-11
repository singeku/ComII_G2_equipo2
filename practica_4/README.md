# Práctica 4: La Modulación de M-PSK y Q-PSK

## 📖 Descripción del Proyecto
[cite_start]Este repositorio documenta el diseño, implementación y simulación de esquemas de modulación digital M-PSK y Q-PSK haciendo uso de Radio Definida por Software (SDR) en el entorno de GNU Radio. 

[cite_start]El objetivo principal de esta práctica es sintetizar estas señales operando estrictamente en el dominio de la **Envolvente Compleja** (banda base), lo que facilita el análisis de la Densidad Espectral de Potencia (PSD) y el mapeo de los símbolos en el plano complejo[cite: 138].

## 👥 Equipo de Trabajo
* [cite_start]**Juan David Camacho González** (Cód: 2210428) [cite: 123]
* [cite_start]**Valentina Arguellez Angulo** (Cód: 2215670) [cite: 123]
* [cite_start]**Jordy Pabón Carrillo** [cite: 123]

## 📁 ¿Qué encontrarás en esta rama?
La rama `practica_4` está dividida en las siguientes carpetas principales:

* **`/GNURadio/`**: Contiene los flujogramas (`.grc`) y los scripts generados en Python. Aquí encontrarás las implementaciones de:
  * [cite_start]El transmisor M-PSK (8-PSK) utilizando tanto el método de Oscilador Controlado por Voltaje (VCO) como el método de Tabla de Verdad[cite: 143, 144].
  * [cite_start]El transmisor Q-PSK ($M=4$) parametrizado con una tasa de símbolos de 32 kBd[cite: 178, 181].
  * [cite_start]Simulaciones del canal introduciendo Ruido Gaussiano Blanco Aditivo (AWGN)[cite: 191].
* **`/Informe/`**: Contiene el código fuente en LaTeX (`.tex`) y las imágenes utilizadas para generar el documento final.
  * [cite_start]**`main.pdf`**: El informe final consolidado con el análisis matemático, comparativas de ancho de banda y conclusiones[cite: 140, 141].

## 🚀 Cómo ejecutar las simulaciones
Para visualizar y ejecutar los flujogramas desarrollados en esta práctica:

1. [cite_start]Asegúrate de tener instalado **GNU Radio** en un entorno Linux (Ubuntu recomendado)[cite: 84, 86].
2. Clona el repositorio y ubícate en la rama correspondiente:
   `git checkout practica_4`
3. Abre GNU Radio Companion y carga los archivos `.grc` ubicados en la carpeta `/GNURadio/`.
4. Al ejecutar cada flujograma, se desplegará una interfaz gráfica (QT GUI) que permite observar:
   * [cite_start]La señal en el dominio del tiempo[cite: 225].
   * [cite_start]La Densidad Espectral de Potencia (PSD) y la ubicación de los cruces por cero[cite: 204].
   * [cite_start]El diagrama de constelación, donde se evidencia la dispersión de los símbolos al interactuar con el ruido AWGN[cite: 196].

## 🎯 Resultados Destacados
* [cite_start]**Ancho de Banda:** Se corroboró experimentalmente que, al trabajar en Envolvente Compleja, el ancho de banda del lóbulo principal está dictado exclusivamente por la tasa de símbolos ($R_s$)[cite: 290].
* [cite_start]**VCO vs. Tabla de Verdad:** Se demostró que ambos métodos de modulación son equivalentes y producen la misma señal en banda base[cite: 197].
* [cite_start]**Constelaciones Inéditas (Punto 8):** Se incluye un análisis sobre geometrías no convencionales (diseñadas por cada integrante) y su vulnerabilidad frente al ruido del canal en comparación con esquemas circulares estándar[cite: 268, 281].
