from django.shortcuts import render

from django.http import HttpResponse


from django.http import HttpResponse

def inicio(request):
    nombre_plataforma = "CoworkSpace"
    descripcion = "Tu espacio ideal para crear, colaborar y crecer."
    capacidad_maxima = 50
    espacios_ocupados = 18
    abierto = True
    servicios = [
        "Escritorios dedicados",
        "Salas de reuniones con proyector",
        "Internet de fibra óptica de alta velocidad",
        "Cafetería y áreas de descanso"
    ]

    espacios_disponibles = capacidad_maxima - espacios_ocupados
    porcentaje_ocupacion = (espacios_ocupados / capacidad_maxima) * 100

    if abierto and espacios_disponibles > 0:
        badge_color = "#10b981"
        estado_texto = f"Abierto • {espacios_disponibles} cupos libres"
    else:
        badge_color = "#ef4444"
        estado_texto = "Cerrado / Sin cupos"

    items_html = "".join([f"<li style='padding: 8px 0; border-bottom: 1px solid #f1f5f9; color: #475569;'>✓ {s}</li>" for s in servicios])

    html = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{nombre_plataforma} | Inicio</title>
    </head>
    <body style="font-family: 'Segoe UI', system-ui, -apple-system, sans-serif; background-color: #f8fafc; margin: 0; padding: 40px 20px; display: flex; justify-content: center; align-items: center; min-height: 80vh;">
        <div style="background: #ffffff; max-width: 650px; width: 100%; padding: 36px; border-radius: 16px; box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05), 0 8px 10px -6px rgba(0, 0, 0, 0.05); border: 1px solid #e2e8f0;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
                <h1 style="margin: 0; font-size: 28px; color: #0f172a; letter-spacing: -0.5px;">🏢 {nombre_plataforma}</h1>
                <span style="background-color: {badge_color}15; color: {badge_color}; padding: 6px 14px; border-radius: 9999px; font-size: 13px; font-weight: 600;">{estado_texto}</span>
            </div>
            
            <p style="color: #64748b; font-size: 16px; line-height: 1.5; margin-bottom: 24px;">{descripcion}</p>
            
            <div style="background-color: #f1f5f9; border-radius: 12px; padding: 18px; margin-bottom: 24px;">
                <div style="display: flex; justify-content: space-between; font-size: 14px; font-weight: 600; color: #334155; margin-bottom: 8px;">
                    <span>Ocupación de salas</span>
                    <span>{porcentaje_ocupacion:.0f}%</span>
                </div>
                <div style="background-color: #cbd5e1; height: 10px; border-radius: 9999px; overflow: hidden;">
                    <div style="background-color: #3b82f6; width: {porcentaje_ocupacion}%; height: 100%; border-radius: 9999px;"></div>
                </div>
            </div>

            <h3 style="font-size: 17px; color: #1e293b; margin-bottom: 12px;">Servicios disponibles</h3>
            <ul style="list-style: none; padding: 0; margin: 0 0 28px 0;">
                {items_html}
            </ul>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)