<body>
    <h1>pop</h1>
    <p>FastAPI.</p>
    <h2>Cómo montar y ejecutar el proyecto FastAPI:</h2>
    <ol>
        <li><strong>Clonar el repositorio:</strong>
            <pre><code>git clone <URL_del_repositorio></code></pre>
        </li>
        <li><strong>Instalar las dependencias del proyecto:</strong>
            <pre>
                <code>cd pop pip install -r requirements.txt</code>
            </pre>
        </li>
        <li><strong>Ejecutar la aplicación:</strong>
            <pre><code>uvicorn api.v1.main:app --reload</code></pre>
            <p>Este comando ejecutará la aplicación FastAPI y proporcionará un servidor de desarrollo que se recargará automáticamente cuando realices cambios en el código.</p>
        </li>
        <li><strong>Acceder a la documentación de la API:</strong>
            <p>Abre un navegador web y visita la URL: <code>http://localhost:8000/</code></p>
        </li>
    </ol>
</body>
</html>
