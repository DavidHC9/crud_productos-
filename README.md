# 📚 Sistema de Gestión de Notas Académicas

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![SQLite](https://img.shields.io/badge/SQLite-3.0+-orange.svg)
![HTML5](https://img.shields.io/badge/HTML5-E34F26.svg)
![CSS3](https://img.shields.io/badge/CSS3-1572B6.svg)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-yellow.svg)

## 🎯 Objetivo del Proyecto

Sistema web completo para la **gestión integral de notas académicas** que permite a educadores registrar, consultar, editar y eliminar calificaciones de estudiantes de manera eficiente. La aplicación implementa operaciones CRUD completas con una interfaz moderna y intuitiva, utilizando diseño neumórfico para una experiencia visual atractiva.

### Funcionalidades Principales:
- ✅ **Registro de notas** con validación de datos
- ✅ **Consulta dinámica** de calificaciones almacenadas
- ✅ **Edición en tiempo real** de registros existentes
- ✅ **Eliminación segura** con confirmación de usuario
- ✅ **Interfaz responsive** adaptable a dispositivos móviles
- ✅ **Base de datos persistente** con SQLite

---

## 🛠️ Tecnologías Utilizadas

### Backend
- **Python 3.8+** - Lenguaje de programación principal
- **Flask 2.0+** - Framework web minimalista y potente
- **SQLite3** - Base de datos embebida para persistencia

### Frontend
- **HTML5** - Estructura semántica de la aplicación
- **CSS3** - Diseño neumórfico moderno y responsive
- **JavaScript ES6+** - Interactividad y comunicación asíncrona
- **Fetch API** - Comunicación cliente-servidor

### Herramientas de Desarrollo
- **Git** - Control de versiones
- **GitHub** - Repositorio remoto y colaboración
- **VSCode** - Editor de código recomendado

---

## 🚀 Instrucciones de Instalación y Ejecución

### Prerrequisitos
Asegúrate de tener instalado:
- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git

### 1️⃣ Clonar el Repositorio
```bash
git clone https://github.com/DavidHC9/crud_productos-.git
cd crud_productos-
```

### 2️⃣ Crear Entorno Virtual (Recomendado)
```bash
# En Windows
python -m venv venv
venv\Scripts\activate

# En macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Instalar Dependencias
```bash
pip install flask
```

### 4️⃣ Ejecutar la Aplicación
```bash
python backend.py
```

### 5️⃣ Acceder a la Aplicación
Abre tu navegador web y navega a:
```
http://localhost:5000
```

### 🔧 Comandos Adicionales

**Detener la aplicación:**
- Presiona `Ctrl + C` en la terminal

**Desactivar entorno virtual:**
```bash
deactivate
```

**Reiniciar base de datos:**
- Elimina el archivo `productos.db` y reinicia la aplicación

---

## 📱 Resultado de la Aplicación

### Vista Principal
![Interfaz Principal](https://via.placeholder.com/800x600/e0f0ff/2a6bbf?text=Sistema+de+Notas+Acad%C3%A9micas)

*Captura de pantalla mostrando la interfaz principal con formulario de registro y tabla de notas*

### Funcionalidades en Acción
![Demo de Funcionalidades](https://via.placeholder.com/800x400/d0e8ff/245a8d?text=CRUD+Operations+Demo)

*GIF demostrativo de las operaciones CRUD: crear, leer, actualizar y eliminar notas*

### Diseño Neumórfico
- **Estilo visual moderno** con efectos de profundidad
- **Colores suaves** en tonalidades azules (#e0f0ff, #c2d6e8)
- **Botones interactivos** con efectos hover
- **Formularios intuitivos** con validación en tiempo real

---

## 📁 Estructura del Proyecto

```
crud_productos-/
│
├── backend.py              # Servidor Flask y API REST
├── productos.db            # Base de datos SQLite (se crea automáticamente)
├── static/
│   ├── style.css          # Estilos neumórficos y responsive
│   └── script.js          # Lógica frontend y comunicación AJAX
├── templates/
│   └── index.html         # Estructura HTML principal
├── README.md              # Este archivo
└── requirements.txt       # Dependencias del proyecto
```

---

## 🔄 API Endpoints

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/` | Página principal |
| `GET` | `/productos` | Listar todas las notas |
| `POST` | `/productos` | Crear nueva nota |
| `GET` | `/productos/<id>` | Obtener nota específica |
| `PUT` | `/productos/<id>` | Actualizar nota existente |
| `DELETE` | `/productos/<id>` | Eliminar nota |

---

## 🧪 Ejemplos de Uso

### Agregar Nueva Nota
```javascript
// Ejemplo de estructura JSON para nueva nota
{
  "nombre": "Juan Pérez",
  "Nota": 8.5,
  "Materia": "Ingeniería de Software"
}
```

### Respuesta del Servidor
```javascript
{
  "mensaje": "Nota guardado correctamente"
}
```

---

## 🤝 Contribución

Las contribuciones son bienvenidas. Para contribuir:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📋 Roadmap

### Versión 2.0 (Próximamente)
- [ ] Autenticación de usuarios
- [ ] Reportes en PDF
- [ ] Gráficos estadísticos
- [ ] Exportación a Excel
- [ ] API REST documentada con Swagger
- [ ] Despliegue en la nube

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

---

## 👥 Créditos y Autores

### Desarrolladores Principales

**David Herrera Carvajal**
- 📧 Email académico: david.herrera@universidad.edu.co
- 🎓 Estudiante de Ingeniería Informatica 
- 💼 Especialización: Desarrollo Backend y Bases de Datos

**Tomás Montoya Bolívar**
- 📧 Email académico: tomas.montoya@universidad.edu.co  
- 🎓 Estudiante de Ingeniería Informatica 
- 💼 Especialización: Desarrollo Frontend y UX/UI

**Juan Manuel Peláez Tamayo**
- 📧 Email académico: juan.pelaez@universidad.edu.co
- 🎓 Estudiante de Ingeniería Informatica 
- 💼 Especialización: Arquitectura de Software y Testing

### Información Académica
- **Institución:** [Tu Universidad]
- **Facultad:** Ingeniería de Sistemas
- **Curso:** Ingeniería de Software
- **Profesor:** [Nombre del Profesor]
- **Semestre:** 2025-1

---

## 📞 Soporte y Contacto

¿Tienes preguntas o necesitas ayuda? Contáctanos:

- 📧 **Email del equipo:** equipo.notas@universidad.edu.co
- 🐛 **Reportar bugs:** [Issues de GitHub](https://github.com/DavidHC9/crud_productos-/issues)
- 💡 **Sugerencias:** [Discussions](https://github.com/DavidHC9/crud_productos-/discussions)

---

## 🏆 Reconocimientos

Agradecimientos especiales a:
- **Comunidad Flask** por la excelente documentación
- **MDN Web Docs** por las referencias de JavaScript
- **Profesores** del curso de Ingeniería de Software
- **Compañeros de clase** por sus valiosos comentarios

---

<div align="center">

### ⭐ Si este proyecto te fue útil, ¡dale una estrella en GitHub! ⭐

**Desarrollado con ❤️ por estudiantes de Ingeniería de Software**

![GitHub stars](https://img.shields.io/github/stars/DavidHC9/crud_productos-?style=social)
![GitHub forks](https://img.shields.io/github/forks/DavidHC9/crud_productos-?style=social)

</div>
