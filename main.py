import pyodbc
from tkinter import *
from tkinter import messagebox

conexion = pyodbc.connect(
    "DRIVER={ODBC DRIVER 18 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=SistemaeducativoPY;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

usuarios = {
    "admin": { 
        "contraseña": "1234",
        "tipo": "estudiante"
    },
    "Brayan2006": {
        "contraseña": "BrayanRomani1",
        "tipo": "profesor"
    },
    "Amiroma2000": "42315996"
}

def abrirMenuProfesor():
      ventana_Profesor = Toplevel(windows)
      ventana_Profesor.title("Menú Principal Profesor")
      ancho_pantalla = ventana_Profesor.winfo_screenmmwidth()
      largo_pantalla = ventana_Profesor.winfo_screenmmheight()
      g = (ancho_pantalla - 120) // 2
      h = (largo_pantalla - 150) // 2
      ventana_Profesor.geometry(f"1280x720+{g}+{h}")

      tituloProfesor = Label(
        ventana_Profesor, 
        text="MENÚ PRINCIPAL",
        font=("Arial", 20, "bold")
      )
      tituloProfesor.pack(pady=30)

      cuadro_contenido_Profesor = Frame(
            ventana_Profesor,
            bd=2,
            relief="groove"
        )
      cuadro_contenido_Profesor.pack(
            side=RIGHT,
            fill=BOTH,
            expand=True,
            padx=10,
            pady=10
        )
      def mostrar_contenido_Profesor(titulo_texto, texto):
            for widget in cuadro_contenido_Profesor.winfo_children():
                widget.destroy()
            Label(
                cuadro_contenido_Profesor,
                text=titulo_texto,
                font=("Arial", 18, "bold")
            ).pack(pady=20)
            Label(
                cuadro_contenido_Profesor,
                text=texto,
                font=("Arial", 12)
            ).pack(pady=10)
    
      def mostrar_perfil_Profesor():
        cursor = conexion.cursor()
        cursor.execute(
            """SELECT nombres, apellidos, correo, telefono
            FROM Perfiles
            WHERE id_usuario = ?""",
            (id_usuario_actual,)
            )
        perfil = cursor.fetchone()
    
        if perfil is not None:
            mensaje = (
                f"Nombres: {perfil[0]}\n"
                f"Apellidos: {perfil[1]}\n"
                f"Correo: {perfil[2]}\n"
                f"Teléfono: {perfil[3]}"
            )
            mostrar_contenido_Profesor("Mi perfil", mensaje)
        else:
            mostrar_contenido_Profesor(
                "Mi perfil",
                 "No se encontró información del perfil."
             )
      boton_inicio_Profesor = Button(
        ventana_Profesor,
        text="Inicio",
        width=20)
      boton_inicio_Profesor.pack(anchor="w", padx=50, pady=20)

      boton_cursos_Profesor = Button(
        ventana_Profesor,
        text="Cursos",
        width=20)
      boton_cursos_Profesor.pack(anchor="w", padx=50, pady=20)

      boton_notas_Profesor = Button(
        ventana_Profesor,
        text="Notas",
        width=20)
      boton_notas_Profesor.pack(anchor="w", padx=50, pady=20)

      boton_asistencia_Profesor = Button(
        ventana_Profesor,
        text="Asistencia",
        width=20)
      boton_asistencia_Profesor.pack(anchor="w", padx=50, pady=20)

      boton_perfil_Profesor = Button(
        ventana_Profesor,
        text="Perfil",
       width=20,
       command=mostrar_perfil_Profesor
       )
      boton_perfil_Profesor.pack(anchor="w", padx=50, pady=20)

      boton_salir_Profesor = Button(
        ventana_Profesor,
        text="Salir",
        width=20,
        command=clickSalir
      )
      boton_salir_Profesor.pack(anchor="w", padx=50, pady=50)

def abrirMenuEstudiante():
    vetana_Estudiante = Toplevel(windows)
    vetana_Estudiante.title("Menú Principal Estudiante")
    
    ancho_pantallaP = vetana_Estudiante.winfo_screenmmwidth()
    largo_pantallaP = vetana_Estudiante.winfo_screenmmheight()
    e = (ancho_pantallaP - 120) // 2
    f = (largo_pantallaP - 150) // 2
    vetana_Estudiante.geometry(f"1280x720+{e}+{f}")

    titulo = Label(
        vetana_Estudiante,
        text="MENÚ PRINCIPAL",
        font=("Arial", 20, "bold")
    )
    titulo.pack(pady=30)

    cuadro_contenido_Estudiante = Frame(
        vetana_Estudiante,
        bd=2,
        relief="groove"
    )
    cuadro_contenido_Estudiante.pack(
        side=RIGHT,
        fill=BOTH,
        expand=True,
        padx=10,
        pady=10
    )

    def mostrar_contenido_estudiante(titulo_texto, texto):
        for widget in cuadro_contenido_Estudiante.winfo_children():
            widget.destroy()
        Label(
            cuadro_contenido_Estudiante,
            text=titulo_texto,
            font=("Arial", 18, "bold")
        ).pack(pady=20)
        Label(
            cuadro_contenido_Estudiante,
            text=texto,
            font=("Arial", 12)
        ).pack(pady=10)

    def mostrar_perfil():
        cursor = conexion.cursor()
        cursor.execute(
            """SELECT nombres, apellidos, correo, telefono
            FROM Perfiles
            WHERE id_usuario = ?""",
            (id_usuario_actual,)
        )
        perfil = cursor.fetchone()

        if perfil is not None:
            mensaje = (
                f"Nombres: {perfil[0]}\n"
                f"Apellidos: {perfil[1]}\n"
                f"Correo: {perfil[2]}\n"
                f"Teléfono: {perfil[3]}"
            )
            mostrar_contenido_estudiante("Mi perfil", mensaje)
        else:
            mostrar_contenido_estudiante(
                "Mi perfil",
                "No se encontró información del perfil."
            )

    boton_inicio_Estudiante = Button(
        vetana_Estudiante,
        text="Inicio",
        width=20,
        command=lambda: mostrar_contenido_estudiante(
            "Inicio",
            "Bienvenido al sistema del estudiante."
        )
    )
    boton_inicio_Estudiante.pack(anchor="w", padx=50, pady=20)

    boton_cursos_Estudiante = Button(
        vetana_Estudiante,
        text="Cursos",
        width=20,
        command=lambda: mostrar_contenido_estudiante(
            "Cursos",
            "Aquí podrás encontrar los cursos y actividades dejadas en clase"
        )
    )
    boton_cursos_Estudiante.pack(anchor="w", padx=50, pady=20)

    boton_notas_Estudiante = Button(
        vetana_Estudiante,
        text="Notas",
        width=20,
        command=lambda: mostrar_contenido_estudiante(
            "Notas",
            "Aquí podrás encontrar las notas correspondientes a los cursos."
        )
    )
    boton_notas_Estudiante.pack(anchor="w", padx=50, pady=20)

    boton_asistencia_Estudiante = Button(
        vetana_Estudiante,
        text="Asistencia",
        width=20,
        command=lambda: mostrar_contenido_estudiante(
            "Asistencia al estudiante",
            "Aquí podrás encontrar la ayuda necesaria"
        )
    )
    boton_asistencia_Estudiante.pack(anchor="w", padx=50, pady=20)

    boton_perfil_Estudiante = Button(
        vetana_Estudiante,
        text="Perfil",
        width=20,
        command=mostrar_perfil
    )
    boton_perfil_Estudiante.pack(anchor="w", padx=50, pady=20)

    boton_salir_Estudiante = Button(
        vetana_Estudiante,
        text="Salir",
        width=20,
        command=clickSalir
    )
    boton_salir_Estudiante.pack(anchor="w", padx=50, pady=50)

def clickSalir():
    windows.destroy()

windows = Tk()
windows.title("Inicio de Sesión")

ancho_pantalla = windows.winfo_screenwidth()
largo_pantalla = windows.winfo_screenmmheight()
a = (ancho_pantalla - 600) // 2
b = (largo_pantalla - 0) // 2
windows.geometry(f"600x450+{a}+{b}")

icono = PhotoImage(file="unsch.png")
windows.iconphoto(True, icono)
windows.config(background="#E9E8E8")

titulo = Label(
    windows, 
    text="INICIAR SESIÓN",
    font=("Arial", 20, "bold")
)
titulo.pack(pady=20)

sub_titulo = Label(
    windows,
    text="Ingresa tu usuario y contraseña",
    font=("Arial", 11)
)
sub_titulo.pack(pady=5)

label_Usuario = Label(
    windows,
    text="Usuario:",
    font=("Arial", 11, "bold")
)
label_Usuario.pack(anchor="w", padx=195, pady=5)

widget_Usuario = Entry(
    windows, 
    font=("Arial", 10),
    width=30
)
widget_Usuario.pack(pady=5)

label_Contraseña = Label(
    windows,
    text="Contraseña:",
    font=("Arial", 11, "bold")
)
label_Contraseña.pack(anchor="w", padx=195, pady=5)

widget_Contraseña = Entry(
    windows,
    font=("Arial", 10),
    show="*",
    width=30
)
widget_Contraseña.pack(pady=5)

id_usuario_actual = None

def clickEntrar():
    global id_usuario_actual

    nombre_Usuario = widget_Usuario.get()
    contraseña = widget_Contraseña.get()
    
    cursor = conexion.cursor()
    cursor.execute(
        """SELECT id_usuario, tipo
        FROM Usuarios
        WHERE usuario = ? AND contraseña = ?
        """,
        (nombre_Usuario, contraseña)
    )
    resultado = cursor.fetchone()

    if resultado:
        id_usuario_actual = resultado[0]
        tipo_usuario = resultado[1]

        if tipo_usuario == "estudiante":
            abrirMenuEstudiante()
        elif tipo_usuario == "profesor":
            abrirMenuProfesor()

        windows.withdraw()
    else:
        messagebox.showerror(
            "Error",
            "Usuario o Contraseña incorrectos"
        )

boton1 = Button(
    windows,
    text="ENTRAR",
    command=clickEntrar,
    font=("Arial", 10),
    width=20
)
boton2 = Button(
    windows,
    text="SALIR",
    command=clickSalir,
    font=("Arial", 10),
    width=20
)
boton1.pack(pady=15)
boton2.pack(pady=5)

windows.mainloop()