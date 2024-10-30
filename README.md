# ¿What it is?
This is an skeleton example to start Python projects that use POO programming and StreamLit. StreamLit is a Graphical User Interface
This example includes:
* Folders as modules to structure the project
* An example for an unitary test
* A requirements.txt file to install the required libraries

# ¿How to use it?
* Install the **virtual environment** [VirtualEnvs](https://docs.python-guide.org/dev/virtualenvs/#lower-level-virtualenv)
* Activate the virtual environment
  > `` Windows \venv\Scripts\activate``
  > `` MAC/Linux source \venv\Scripts\activate``
* Install missing libraries  `` pip install -r requirements.txt ``
* Run Streamlit example app 
  > ``streamlit run main.py``


## Useful links
* Streamlit --> https://streamlit.io
* P8P coding standard --->https://peps.python.org/pep-0008/

## Estructura basica

├── src/                     # Directorio principal del código fuente  
│   ├── model               # Contiene la lógica principal
    │   ├── ui_components.py     # Componentes de interfaz de usuario reutilizables y configuraciones de estilo
    │   ├── leaderboard.py       # Funciones relacionadas con la gestión de la tabla de líderes
    │   └── utils.py             # Funciones de utilidad general como cargar imágenes y otros
├── pages/                    # Directorio para las páginas de la aplicación
│   ├── habito.py               # Página de inicio y configuración del juego
│   ├── reportes.py               # Página donde se juega efectivamente
│   └── leaderboard.py        # Página para mostrar la tabla de líderes
├── static/
│   ├── images/              # Directorio para imágenes estáticas utilizadas en la interfaz
│   └── styles/              # Hojas de estilo y otros recursos de estilo si se requieren
│
├── main.py                   # Archivo principal que ejecuta la aplicación Streamlit
