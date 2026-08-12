# Gastos Personales

## Descripción del Proyecto

Gastos Personales es un componente desarrollado en Python para registrar y analizar gastos personales.

El sistema permite:

- Registrar gastos con fecha, monto, categoría y descripción.
- Validar los datos ingresados.
- Calcular el total de una lista de gastos.
- Calcular el promedio de una lista de gastos.

## Objetivo

Desarrollar un componente funcional en Python aplicando buenas prácticas de programación, pruebas automatizadas, revisión de calidad y seguridad, documentación técnica y control de versiones colaborativo mediante GitHub.

## Funcionalidades

- **Registro de gastos:** fecha, monto, categoría y descripción.
- **Validaciones:**
  - El monto debe ser mayor que cero.
  - La categoría debe pertenecer a las categorías permitidas.
- **Cálculos:**
  - Total de una lista de gastos.
  - Promedio de una lista de gastos.
- **Pruebas automatizadas:** realizadas con pytest.

### Categorías permitidas

- Alimentación
- Ayuda familiar
- Educación
- Entretenimiento
- IESS
- Otros
- Salud
- Servicios
- Transporte
- Vivienda

## Tecnologías utilizadas

- Python 3.8 o superior
- pytest
- GitHub Copilot
- Visual Studio Code
- SonarQube for IDE
- Git
- GitHub

## Estructura del proyecto

```text
gastos-personales/
├── gastos.py
├── test_gastos.py
└── README.md
Descripción de los archivos
Archivo	Descripción
gastos.py	Contiene las funciones principales del componente.
test_gastos.py	Contiene las pruebas automatizadas.
README.md	Contiene la documentación técnica del proyecto.
Instalación
Se requiere tener Python 3.8 o superior instalado.
Para instalar pytest:
py -m pip install pytest
Ejecución de las pruebas
Desde la carpeta del proyecto ejecutar:
py -m pytest
Las pruebas verifican:
•	Registro correcto de gastos. 
•	Validación de montos. 
•	Validación de categorías. 
•	Cálculo del total. 
•	Cálculo del promedio. 
•	Flujo completo de registro y cálculo de gastos. 
Uso de GitHub Copilot
GitHub Copilot se utilizó como asistente durante el desarrollo del componente.
Se utilizó para:
•	Generar código mediante comentarios y completions inline. 
•	Revisar el código generado. 
•	Identificar oportunidades de refactorización. 
•	Mejorar la organización y documentación del código. 
•	Revisar la redacción de la documentación técnica. 
Las sugerencias de Copilot fueron revisadas antes de aplicarlas al proyecto.
Calidad y seguridad
El código fue analizado mediante la extensión SonarQube for IDE en Visual Studio Code.
El análisis no presentó hallazgos de severidad alta pendientes de resolver.
Control de versiones y Pull Request
El proyecto fue gestionado mediante Git y GitHub utilizando una rama de trabajo para el desarrollo.
Los cambios fueron organizados mediante commits y posteriormente se creó un Pull Request hacia la rama principal para revisar e integrar la solución final.
Conclusiones
El desarrollo del componente permitió aplicar GitHub Copilot como asistente durante diferentes etapas del desarrollo, desde la generación inicial del código mediante comentarios hasta la revisión y refactorización del componente.
Las pruebas automatizadas con pytest permitieron comprobar el funcionamiento de las principales funcionalidades y verificar que los cambios realizados no afectaran el comportamiento esperado.
El análisis mediante SonarQube for IDE permitió revisar la calidad y seguridad del código. Finalmente, el uso de Git, GitHub, ramas y Pull Requests permitió aplicar un flujo organizado para gestionar y entregar la solución final.
Autor
Norma Benalcázar
Licencia
Proyecto académico desarrollado como parte del curso GitHub Copilot para Desarrollo y Aseguramiento de la Calidad.

