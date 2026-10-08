  Fecha de inicio: 08 de octubre 2026 
  Herramientas utilizadas: Navegador Web y Security Analyst Dashboard
  
  1.- Resumen: El objetivo de este laboratorio fue analizar un evento de tráfico sospechoso mediante el panel de control de un analista SOC. Se identificó una dirección IP maliciosa ejecutando un ataque de reconocimiento/fuerza bruta sobre la infraestructura y se aplicaron acciones inmediatas de contención.

2. Reconocimiento e Identificación
  2.- Reconocimiento e Identificación: 
    1.- IP Sospechosa: Con el uso del panel de control logramos identificar cual es la IP correspondiente a la actividad sospechosa (32.122.195.63)
    2.- Identificación de Ataque: Gracias a que el panel de control registra todos los movimientos, con eso descubrimos que el atacante esta tratando de encontrar la URL: https://fakebank.com/admin. Esto es conocido como Enumeración de Directorios o Ataque de Fuerza Bruta Sobre paneles de Administración
    3.- Detención del Ataque: Para detener el ataque primero lo contenemos, lo que hacemos es desde el panel "Implement Security Actions" para colocar la IP del atacante y bloquearlo, esto es una medida temporal ya que el atacante puede cambiar de IP mediante VPN o Proxy, aun así se realiza para detener el ataque de forma momentanea y poder solucionarlo
  
  3.- Formas de Mitigación: El panel de seguridad nos da diversas opciones sobre como podemos detener el ataque
    1.- Bloqueo de IP: Utilizado en este laboratorio mediante el panel "Implement Security Actions" pude bloquear la IP del atacante, la cual es una buena opción inmediata
    2.- Limitación de Velocidad: Esto limitaria el número de conexiones posibles por usuario
    3.- Actualización de las Reglas de Seguridad: Reforzaria los controles de acceso a las páginas sensibles que el atacante ha logrado sortear 
