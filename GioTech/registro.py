import pandas as pd

columns = ['correo', 'contraseña'] + [f'pregunta{i+1}' for i in range(24)]
df = pd.DataFrame(columns=columns)

def agregar_usuario(correo, contraseña):
    global df
    new_data = {**{'correo': correo, 'contraseña': contraseña}, **{f'pregunta{i+1}': None for i in range(24)}}
    df = df.append(new_data, ignore_index=True)

def actualizar_respuesta(correo, pregunta_num, respuesta):
    global df
    df.loc[df['correo'] == correo, f'pregunta{pregunta_num}'] = respuesta

def guardar_dataframe():
    df.to_csv('datos_usuarios.csv', index=False)

def cargar_dataframe():
    global df
    try:
        df = pd.read_csv('datos_usuarios.csv')
    except FileNotFoundError:
        df = pd.DataFrame(columns=columns)


cargar_dataframe()


if df.empty or 'usuario@example.com' not in df['correo'].values:
    agregar_usuario('usuario@example.com', 'contraseña123')

actualizar_respuesta('usuario@example.com', 1, 'Respuesta a la pregunta 1')
guardar_dataframe()

