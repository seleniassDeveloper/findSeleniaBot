import pandas as pd

# Datos para el plan detallado
plan_data_corrected = {
    "Hora": [
        "7:00 AM", "8:00 AM", "9:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM", "2:00 PM", "3:00 PM", "4:00 PM", "5:00 PM", "6:00 PM", "7:00 PM", "8:00 PM", "9:00 PM", "10:00 PM", "11:00 PM"
    ],
    "Lunes & Miércoles": [
        "Gym (Ejercicio de fuerza)", "Ducha & Desayuno (Ayuno Intermitente, solo agua/té)", 
        "Inicio de Trabajo", "Trabajo", "Trabajo", "Trabajo", "Almuerzo: Ensalada de Pollo (150g pollo, 50g aguacate, 100g espinaca, 50g tomate, 1 cda aceite de oliva, limón)", 
        "Trabajo", "Trabajo", "Trabajo", "Trabajo", "Snack: Yogur griego sin azúcar + 10 almendras", 
        "Fin de Trabajo", "Estudio", "Estudio", "Dormir"
    ],
    "Martes & Jueves & Viernes": [
        "Descanso", "Ducha & Inicio de día", "Inicio de Trabajo", "Trabajo", "Trabajo", "Trabajo", 
        "Almuerzo: 120g pollo, 100g arroz integral, 150g verduras al vapor, 1 cda aceite de oliva", 
        "Trabajo", "Trabajo", "Trabajo", "Trabajo", "Snack: Batido de proteína con agua + 10 almendras", 
        "Fin de Trabajo", "Pilates (Viernes) / Cena: 2 huevos revueltos con espinaca y tomate, 1 tostada pan integral, ½ aguacate", 
        "Cena: 120g pollo/pescado + ensalada de hojas verdes", "Dormir"
    ],
    "Sábado": [
        "Gym (Full Body)", "Ducha & Descanso", "Tiempo Libre", "Tiempo Libre", "Tiempo Libre", 
        "Tiempo Libre", "Almuerzo: 120g pollo, 100g arroz integral, 150g verduras al vapor, 1 cda aceite de oliva", 
        "Tiempo Libre", "Tiempo Libre", "Tiempo Libre", "Snack: Batido de proteína con agua + 10 almendras", 
        "Tiempo Libre", "Cena: Ensalada de Pollo (150g pollo, 50g aguacate, 100g espinaca, 50g tomate, 1 cda aceite de oliva, limón)", 
        "Descanso", "Dormir"
    ],
    "Domingo": [
        "Descanso", "Ducha & Estudio", "Estudio", "Tiempo Libre", "Tiempo Libre", "Tiempo Libre", 
        "Almuerzo: Ensalada de Pollo (150g pollo, 50g aguacate, 100g espinaca, 50g tomate, 1 cda aceite de oliva, limón)", 
        "Tiempo Libre", "Tiempo Libre", "Tiempo Libre", "Tiempo Libre", "Snack: Yogur griego sin azúcar + 10 almendras", 
        "Tiempo Libre", "Cena: Ensalada de Pollo (150g pollo, 50g aguacate, 100g espinaca, 50g tomate, 1 cda aceite de oliva, limón)", 
        "Descanso", "Dormir"
    ]
}

# Crear el DataFrame
plan_df_corrected = pd.DataFrame(plan_data_corrected)

# Guardar el archivo Excel
plan_df_corrected.to_excel("Plan_Diario_Detallado.xlsx", index=False)
