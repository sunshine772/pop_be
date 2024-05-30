<body>
    <h1>BACKEND</h1>
    <p>Este es un proyecto de FastAPI.</p>
    <h2>Cómo montar y ejecutar el proyecto FastAPI:</h2>
    <ol>
        <li><strong>Clonar el repositorio:</strong>
            <pre><code>git clone https://github.com/sunshine772/pop_be.git</code></pre>
        </li>
        <!-- <li><strong>Crear y activar un entorno virtual:</strong>
            <pre>
                <code>cd pop_be<br>python -m venv env<br>source env/bin/activate   # En Linux/MacOS<br>env\Scripts\activate      # En Windows
                </code>
            </pre>
        </li> -->
        <li><strong>Instalar las dependencias del proyecto:</strong>
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li><strong>Ejecutar la aplicación:</strong>
            <pre><code>uvicorn api.v1.main:app --reload</code></pre>
            <p>Este comando ejecutará la aplicación FastAPI y proporcionará un servidor de desarrollo que se recargará automáticamente cuando realices cambios en el código.</p>
        </li>
        <li><strong>Acceder a la documentación de la API:</strong>
            <p>Abre un navegador web y visita la URL: <code>http://localhost:8000</code></p>
        </li>
    </ol>
</body>
