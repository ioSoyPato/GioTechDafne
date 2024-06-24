from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
import pandas as pd
import aiofiles
import csv

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def greet(request: Request):
    return templates.TemplateResponse("index2.html", {"request": request})

@app.get("/login")
async def greet(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/login")
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    try:
        with open("data.csv", mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[1] == username and row[2] == password:
                    credencials = pd.DataFrame({"username":[username], "password":[password]})
                    credencials.to_csv("credencials.csv")                   
                    return templates.TemplateResponse("index2.html", {"request": request})
            return templates.TemplateResponse("login.html", {"request": request, "error": "Credenciales incorrectas"})
    except FileNotFoundError:
        return templates.TemplateResponse("login.html", {"request": request, "error": "Error en el sistema, intente más tarde."})


@app.get("/register")
async def greet(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.post("/register")
async def register(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    confirm_password: str = Form(...)
):
    if password != confirm_password:
        return templates.TemplateResponse("register.html", {"request": request, "error": "Las contraseñas no coinciden."})
    
    save_path = "data.csv"
    with open(save_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])
    
    return templates.TemplateResponse("register.html", {"request": request, "message": "Usuario registrado con éxito"})

# guardar respuestas

df = pd.read_csv("data.csv",index_col=0)
credencials = pd.read_csv("credencials.csv")
Global_user = credencials["username"][0]

# Formulario 
@app.post("/section1")
async def sec1(request: Request, nombre: str = Form(...), apellidop: str = Form(...),apellidom:str  = Form(...), calle:str = Form(...), numero:str = Form(...), colonia:str = Form(...), poblacion:str = Form(...), municipio:str = Form(...), estado:str = Form(...), codigo:int = Form(...), telefonocasa:int = Form(...), celular1:int = Form(...), email1:str = Form(...)):
    global Global_user
    print(nombre)
    print(apellidop)
    print(apellidom)
    print(calle)
    print(numero)
    print(colonia)
    print(poblacion)
    print(municipio)
    print(estado)
    print(codigo)
    print(telefonocasa)
    print(celular1)
    print(email1)

    df.loc[df["correo"] == Global_user, "pregunta1"] = "True"
    df.to_csv("data.csv")
    return "si funcionó"


@app.post("/section2_4")
async def sec2(request: Request, 
               tiene_beca: str = Form(...), 
               tipobeca: str = Form(None), 
               economica: str = Form(None), 
               institucion: str = Form(None), 
               dependencia: str = Form(...), 
               tutores3: str = Form(None), 
               vive_con: str = Form(...), 
               otroparentesco: str = Form(None)):
    
    print(f"Tiene beca: {tiene_beca}")
    print(f"Tipo de beca: {tipobeca}")
    print(f"Económica: {economica}")
    print(f"Institución: {institucion}")
    print(f"Dependencia: {dependencia}")
    print(f"Tutores detalle: {tutores3}")
    print(f"Vive con: {vive_con}")
    print(f"Otro parentesco: {otroparentesco}")
    
    return "si funcionó2"

@app.post("/section5_7")
async def form_receive(
    request: Request,
    trabaja_actualmente: str = Form(...),
    nombreempresa: str = Form(None),
    puesto: str = Form(None),
    tiempolaborando: str = Form(None),
    domicilio6: str = Form(None),
    telefono6: int = Form(None),
    viven_padres: str = Form(...),
    edadpadre: int = Form(None),
    edadmadre: int = Form(None)):
   
    print(f"Trabaja: {trabaja_actualmente}")
    print(f"Empresa: {nombreempresa}")
    print(f"Puesto: {puesto}")
    print(f"Tiempo Laborando: {tiempolaborando}")
    print(f"Domicilio: {domicilio6}")
    print(f"Teléfono: {telefono6}")
    print(f"Viven Padres: {viven_padres}")
    print(f"Edad Padre: {edadpadre}")
    print(f"Edad Madre: {edadmadre}")
     
    return "si funcionó3"

@app.post("/section8_10")
async def process_form(
    request: Request,
    viven_juntos: str = Form(...),
    estado_civil_padre: str = Form(...),
    estado_civil_madre: str = Form(...),
    padre_educacion: str = Form(...),  
    madre_educacion: str = Form(...),  
    padre_nombre: str = Form(...),  
    padre_lugar_trabajo: str = Form(...),
    padre_cargo: str = Form(...),
    padre_tiempo_laborando: str = Form(...),
    padre_domicilio: str = Form(...),
    padre_telefono: str = Form(...),
    madre_nombre: str = Form(...),  
    madre_lugar_trabajo: str = Form(...),
    madre_cargo: str = Form(...),
    madre_tiempo_laborando: str = Form(...),
    madre_domicilio: str = Form(...),
    madre_telefono: str = Form(...)):
    
    print(f"Viven juntos: {viven_juntos}")
    print(f"Estado civil del padre: {estado_civil_padre}")
    print(f"Estado civil de la madre: {estado_civil_madre}")
    print(f"Educación del padre: {padre_educacion}")
    print(f"Educación de la madre: {madre_educacion}")
    print(f"Datos del trabajo del padre: {padre_nombre}, {padre_lugar_trabajo}, {padre_cargo}, {padre_tiempo_laborando}, {padre_domicilio}, {padre_telefono}")
    print(f"Datos del trabajo de la madre: {madre_nombre}, {madre_lugar_trabajo}, {madre_cargo}, {madre_tiempo_laborando}, {madre_domicilio}, {madre_telefono}")
    
    return "Datos recibidos"
    
@app.post("/section11_13")
async def form_section11_13(
    request: Request,
    cuantoshermanos: int = Form(...),
    hermanos_viven: str = Form(...),  
    cuantosviven: int = Form(None), 
    economica12: int = Form(...),
    vivienda: int = Form(...),
    nombre13: str = Form(...),
    edad13: str = Form(...),
    parentesco13: str = Form(...),
    ocupacion13: str = Form(...),
    estudio13: str = Form(...)):
  
    print(f"Cantidad de hermanos: {cuantoshermanos}")
    print(f"Hermanos viven en domicilio: {hermanos_viven}")
    print(f"Cuantos hermanos viven en el domicilio: {cuantosviven}")
    print(f"Dependencia económica: {economica12}")
    print(f"Personas en la vivienda: {vivienda}")
    print(f"Detalles de la persona en vivienda: {nombre13}, {edad13}, {parentesco13}, {ocupacion13}, {estudio13}")

    return {"Datos recibidos correctamente"}


@app.post("/section14_16")
async def process_section14_16(
    request: Request,
    nombre14: str = Form(...),
    nivel14: str = Form(...),
    institucion14: str = Form(...),
    regimen_seguridad_social: str = Form(...),
    otro_regimen_seguridad: str = Form(None),  
    cuantastrabajan: int = Form(...),
    cuantasaportan: int = Form(...),
    ingresomensual: int = Form(...),
    ingresopropio: int = Form(...),
    ingresoconyuge: int = Form(...),
    ingresopadre: int = Form(...),
    ingresomadre: int = Form(...),
    ingresohermanos: int = Form(...),
    otrosingresos: int = Form(...)):

    print(f"Estudios de familiares: Nombre: {nombre14}, Nivel: {nivel14}, Institución: {institucion14}")
    print(f"Régimen de seguridad social: {regimen_seguridad_social}, Otro especificado: {otro_regimen_seguridad}")
    print(f"Ingresos familiares: Trabajan: {cuantastrabajan}, Aportan: {cuantasaportan}, Total Mensual: {ingresomensual}")
    print(f"Ingresos detallados: Propio: {ingresopropio}, Cónyuge: {ingresoconyuge}, Padre: {ingresopadre}, Madre: {ingresomadre}, Hermanos: {ingresohermanos}, Otros: {otrosingresos}")

    return {"message": "Datos recibidos correctamente"}

@app.post("/section17")
async def process_section17(
    request: Request,
    alimentos: int = Form(...),
    renta: int = Form(...),
    despensa: int = Form(...),
    luz: int = Form(...),
    agua: int = Form(...),
    telefono17: int = Form(...),
    transporte17: int = Form(...),
    celular17: int = Form(...),
    cable: int = Form(...),
    internet17: int = Form(...),
    gas17: int = Form(...),
    productoslimpieza: int = Form(...),
    creditoautomovil: int = Form(...),
    tarjetascredito: int = Form(...),
    hipoteca: int = Form(...),
    serviciosdomésticos: int = Form(...),
    ropa: int = Form(...),
    gastosmedicos: int = Form(...),
    gastospersonales: int = Form(...),
    diversiones: int = Form(...),
    vacaciones: int = Form(...),
    colegiatura: int = Form(...),
    colegiaturafamilia: int = Form(...),
    libros: int = Form(...),
    seguros: int = Form(...),
    otros17: int = Form(...)):
  
    print(f"Alimentos: {alimentos}")
    print(f"Renta: {renta}")
    print(f"Despensa: {despensa}")
    print(f"Luz: {luz}")
    print(f"Agua: {agua}")
    print(f"Teléfono: {telefono17}")
    print(f"Transporte: {transporte17}")
    print(f"Celular: {celular17}")
    print(f"Cable: {cable}")
    print(f"Internet: {internet17}")
    print(f"Gas: {gas17}")
    print(f"Productos de limpieza: {productoslimpieza}")
    print(f"Pago crédito automóvil: {creditoautomovil}")
    print(f"Tarjetas de crédito: {tarjetascredito}")
    print(f"Pago de hipoteca: {hipoteca}")
    print(f"Servicios domésticos: {serviciosdomésticos}")
    print(f"Ropa y calzado: {ropa}")
    print(f"Gastos médicos: {gastosmedicos}")
    print(f"Gastos personales: {gastospersonales}")
    print(f"Diversiones y entretenimiento: {diversiones}")
    print(f"Vacaciones: {vacaciones}")
    print(f"Colegiatura: {colegiatura}")
    print(f"Colegiatura otros miembros familia: {colegiaturafamilia}")
    print(f"Libros y materiales: {libros}")
    print(f"Seguros (vida, auto, casa, médico): {seguros}")
    print(f"Otros gastos: {otros17}")
    
    return {"message": "Datos de gastos mensuales recibidos correctamente"}

@app.post("/section18_20")
async def process_section18_20(
    colegiatura18: int = Form(...),
    ropa18: int = Form(...),
    vivienda18: int = Form(...),
    libros18: int = Form(...),
    lavanderia18: int = Form(...),
    transporte18: int = Form(...),
    gastospersonales18: int = Form(...),
    transporteforaneo18: int = Form(...),
    alimentos18: int = Form(...),
    clase_socioeconomica: str = Form(...),
    tipo_vivienda: str = Form(...)):
   
    print(f"Colegiatura: {colegiatura18}, Ropa: {ropa18}, Vivienda: {vivienda18}, Libros: {libros18}, Lavandería: {lavanderia18}")
    print(f"Transporte local: {transporte18}, Gastos personales: {gastospersonales18}, Transporte foráneo: {transporteforaneo18}, Alimentos: {alimentos18}")
    print(f"Clase socioeconómica: {clase_socioeconomica}, Tipo de vivienda: {tipo_vivienda}")
    
    return {"message": "Datos recibidos correctamente"}

@app.post("/section21")
async def process_section21(items: list = Form(...)):
    print("Items seleccionados:")
    for item in items:
        print(item)
    
    return {"message": "Datos recibidos correctamente", "items seleccionados": items}


@app.post("/section22")
async def process_section22(
    marca: str = Form(...),
    modelo: str = Form(...),
    valor_comercial: float = Form(...),
    cantidad_adeuda: float = Form(...),
    plazo: str = Form(...),
    pago_mensual: float = Form(...)):

    print(f"Marca: {marca}, Modelo: {modelo}")
    print(f"Valor Comercial: {valor_comercial}, Cantidad que se Adeuda: {cantidad_adeuda}")
    print(f"Plazo en Meses: {plazo}, Pago Mensual: {pago_mensual}")
    
    return {"message": "Datos del vehículo recibidos correctamente"}


@app.post("/section23_25")
async def process_section23_25(
    zona_vivienda: str = Form(...),
    comunidad_indigena: str = Form(...),
    especifique_comunidad: str = Form(None),  
    discapacidad: str = Form(...),
    especifique_discapacidad: str = Form(None)):

    print(f"Zona de vivienda: {zona_vivienda}")
    print(f"Pertenece a comunidad indígena: {comunidad_indigena}, Especificación: {especifique_comunidad}")
    print(f"Sufre de alguna discapacidad: {discapacidad}, Especificación: {especifique_discapacidad}")
    
    return {"message": "Información recibida correctamente"}
