from django.shortcuts import render

from Vuelos_BFS import CONEXIONES, buscar_solucion_BFS, obtener_ciudades, reconstruir_ruta


def home(request):
    ciudades = obtener_ciudades(CONEXIONES)
    ruta = None
    error = None

    if request.method == "POST":
        estado_inicial = request.POST.get("estado_inicial", "").strip()
        estado_destino = request.POST.get("estado_destino", "").strip()

        if estado_inicial not in ciudades or estado_destino not in ciudades:
            error = "Selecciona ciudades validas."
        else:
            nodo_solucion = buscar_solucion_BFS(CONEXIONES, estado_inicial, estado_destino)
            if nodo_solucion is None:
                error = "No se encontro una ruta entre esas ciudades."
            else:
                ruta = reconstruir_ruta(nodo_solucion, estado_inicial)

    return render(
        request,
        "vuelos_app/home.html",
        {
            "ciudades": ciudades,
            "ruta": ruta,
            "error": error,
        },
    )
