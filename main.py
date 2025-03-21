from Requerimiento1.automatizacion import descargar_citas
from Requerimiento1.arreglar_ieee import procesar_archivos_ieee
from Requerimiento1.unificarArchivos import unificar_filtrar_archivos

def main():

    descargar_citas()  # ---> Descarga las citas de las bases de datos Sage, IEEE y ScienceDirect de manera automatizada
    procesar_archivos_ieee() # ---> Arregla las entradas IEEE en formato BibTeX (Saltos de linea)
    unificar_filtrar_archivos() # ---> Unifica y filtra las citas descargadas de las bases de datos

if __name__ == "__main__":
    main()