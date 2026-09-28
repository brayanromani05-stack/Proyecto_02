if nombre_Usuario in usuarios:
    
        if usuarios[nombre_Usuario]["contraseña"]==contraseña:
           tipo_de_Usuario = usuarios[nombre_Usuario]["tipo"]
           if tipo_de_Usuario == "estudiante":
               abrirMenuEstudiante()
               windows.withdraw()
           elif tipo_de_Usuario == "profesor":
               abrirMenuProfesor()
               windows.withdraw()

           widget_Usuario.delete(0,END)
           widget_Contraseña.delete(0,END)
        else:
           messagebox.showerror(
               "Error",
               "La contraseña es incorrecta" 
           )
    else:
        messagebox.showerror(
            "Error", "Usuario no encontrado"
        )
cursor.execute("SELECT * FROM Usuarios;")
Usuarios = cursor.fetchall()
for usuario in Usuarios:
    print(usuario)
print ("Conexión exitosa")
cursor = conexion.cursor()
cursor.execute("SELECT * FROM Usuarios;")
Usuarios = cursor.fetchall()
for usuario in Usuarios:
    print(usuario)
print ("Conexión exitosa")