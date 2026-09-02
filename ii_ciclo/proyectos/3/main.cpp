#include <iostream>

using namespace std;

// Prototipos
vector<Medicion> leerArchivo();
void mostrarMediciones(...);
void mostrarInformacionPorSensor(...);
void mostrarMayoresTemperaturas(...);

// Función principal
int main() {
    vector<Medicion> mediciones = leerArchivo();

    int opcion = 0;
    while (opcion != 4) {
        cout << "\nANALIZADOR DE SENSORES\n";
        cout << "1. Mostrar mediciones\n";
        cout << "2. Mostrar información por sensor\n";
        cout << "3. Mostrar mayores temperaturas\n";
        cout << "4. Salir\n";
        cout << "Seleccione una opción: ";
        cin >> opcion;

        // Limpiar el salto de línea que queda en el búfer
        cin.ignore();

        switch (opcion) {
            case 1:
                mostrarMediciones(mediciones);
                break;
            case 2:
                mostrarInformacionPorSensor(mediciones);
                break;
            case 3:
                mostrarMayoresTemperaturas(mediciones);
                break;
            case 4:
                cout << "Saliendo del programa..." << endl;
                break;
            default:
                cout << "Opción inválida. Intente nuevamente." << endl;
                break;
        }
    }

    return 0;
}


// Lee el archivo y retorna un vector con las mediciones
vector<Medicion> leerArchivo() {

}

// Muestra todas las mediciones
void mostrarMediciones(const vector<Medicion>& mediciones) {

}   

// Muestra cantidad de sensores diferentes y mediciones por sensor
void mostrarInformacionPorSensor(const vector<Medicion>& mediciones) {

}

// Ordena las mediciones por temperatura y muestra las cinco temperaturas más altas
void mostrarMayoresTemperaturas(vector<Medicion>& mediciones) {

}