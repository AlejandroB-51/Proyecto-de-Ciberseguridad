Fecha de Inicio: 18 de Septiembre 2026
Herramientas Utilizadas: Dirbister y Navegador Web
1.- Resumen de la Actividad:
Durante la prueba de la aplicación web simulada: Fakebank , se pudo identificar una falla de seguridad dentro de la estructura de archivos del servidor. El sitio no contaba con alguna restricción de acceso adecuada ni con la ocultación de rutas administrativas sensibles.

2.- Reconocimiento y Explotación:
1.- Descubrimiento de Directorios: Utilice la herramienta Dirbuster para poder realizar un ataque de fuerza bruta sobre la estructura de directorios del sitio web.
2.- Hallazgo: Tras el ataque utilizando Dirbister pude identificar una URL oculta: http://fakebank.thm/bank-transfer .
3.- Explotación: Después de ingresar a la ruta oculta, la interfaz me permite ejecutar una transferencia de dinero no autorizada entre cuentas sin necesidad alguna de una autenticación previa o permisos de administrador.

3.- Impacto y Riesgo:
Riesgo: Muy Alto
Argumento: Un atacante puede localizar fácilmente la URL oculta y realizar transferencias no autorizadas.

4.-Mitigación y Solución
Control de Acceso: Se recomienda implementar implementación y autorización estrictas del lado del servidor para cada panel para asegurar que solo usuarios autenticados con el rol de administrador puedan acceder.
Deshabilitar la Navegación de Directorios: Esto garantizaría que el servidor web no exponga listados de archivos.

