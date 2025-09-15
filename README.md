# Telco Konrad API Management

Este proyecto es una simulación de un API Management para Telco Konrad, diseñado con Flask. La estructura modular del proyecto permite un fácil mantenimiento y escalabilidad.

## Estructura del Proyecto

```
telco-konrad-api-management
├── app
│   ├── __init__.py
│   ├── api
│   │   ├── __init__.py
│   │   ├── endpoints.py
│   ├── models
│   │   ├── __init__.py
│   │   └── models.py
│   ├── services
│   │   ├── __init__.py
│   │   └── service_logic.py
│   ├── utils
│   │   ├── __init__.py
│   │   └── helpers.py
│   └── config.py
├── tests
│   ├── __init__.py
│   ├── test_endpoints.py
│   └── test_services.py
├── requirements.txt
├── run.py
└── README.md
```

## Instalación

1. Clona el repositorio:
   ```
   git clone <URL_DEL_REPOSITORIO>
   cd telco-konrad-api-management
   ```

2. Crea un entorno virtual:
   ```
   python -m venv venv
   ```

3. Activa el entorno virtual:
   - En Windows:
     ```
     venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

## Uso

Para ejecutar la aplicación, utiliza el siguiente comando:

```
python run.py
```

La API estará disponible en `http://localhost:5000`.

## Pruebas

Las pruebas unitarias se encuentran en el directorio `tests`. Para ejecutarlas, asegúrate de estar en el entorno virtual y ejecuta:

```
pytest
```

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT.