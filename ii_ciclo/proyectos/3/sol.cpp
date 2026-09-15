#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

// Estructura para almacenar una medición
struct Medicion {
    string sensor;
    double temperatura;
    double voltaje;
};

// Prototipos
vector<Medicion> leerArchivo();
void mostrarMediciones(const vector<Medicion>& mediciones);
void mostrarInformacionPorSensor(const vector<Medicion>& mediciones);
bool compararTemperaturaDesc(const Medicion& a, const Medicion& b);
void mostrarMayoresTemperaturas(const vector<Medicion>& mediciones);

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
    vector<Medicion> mediciones;
    ifstream archivo("sensores.txt");

    if (!archivo.is_open()) {
        cout << "Error: No se pudo abrir el archivo sensores.txt" << endl;
        return mediciones;   // vector vacío
    }

    string linea;
    while (getline(archivo, linea)) {
        stringstream ss(linea);
        string sensor;
        string tempStr;
        string voltStr;

        getline(ss, sensor, ',');
        getline(ss, tempStr, ',');
        getline(ss, voltStr, ',');

        // Convertir a números
        double temperatura = stod(tempStr);
        double voltaje = stod(voltStr);

        Medicion m;
        m.sensor = sensor;
        m.temperatura = temperatura;
        m.voltaje = voltaje;

        mediciones.push_back(m);
    }

    archivo.close();
    return mediciones;
}

// Muestra todas las mediciones
void mostrarMediciones(const vector<Medicion>& mediciones) {
    if (mediciones.empty()) {
        cout << "No hay mediciones cargadas." << endl;
        return;
    }

    cout << "\nMEDICIONES\n" << endl;
    for (int i = 0; i < mediciones.size(); i++) {
        cout << "Sensor: " << mediciones[i].sensor << endl;
        cout << "Temperatura: " << mediciones[i].temperatura << " °C" << endl;
        cout << "Voltaje: " << mediciones[i].voltaje << " V" << endl;
        cout << "-----------------------------" << endl;
    }
}

// Muestra cantidad de sensores diferentes y mediciones por sensor
void mostrarInformacionPorSensor(const vector<Medicion>& mediciones) {
    if (mediciones.empty()) {
        cout << "No hay mediciones cargadas." << endl;
        return;
    }

    // set para sensores únicos
    set<string> sensoresUnicos;
    // map para contar mediciones por sensor
    map<string, int> conteo;

    for (int i = 0; i < mediciones.size(); i++) {
        string s = mediciones[i].sensor;
        sensoresUnicos.insert(s);
        conteo[s]++;   // si no existe, map lo crea con 0 y luego incrementa
    }

    cout << "\nSENSORES REGISTRADOS" << endl;
    cout << "\nCantidad de sensores: " << sensoresUnicos.size() << endl;

    cout << "\nMEDICIONES POR SENSOR" << endl;
    // map mantiene las claves ordenadas automáticamente
    for (map<string, int>::iterator it = conteo.begin(); it != conteo.end(); ++it) {
        cout << it->first << ": " << it->second << endl;
    }
}

// Función comparadora para ordenar de mayor a menor temperatura
bool compararTemperaturaDesc(const Medicion& a, const Medicion& b) {
    return a.temperatura > b.temperatura;   // mayor primero
}

// Ordena las mediciones por temperatura y muestra las cinco temperaturas más altas
void mostrarMayoresTemperaturas(vector<Medicion>& mediciones) {
    if (mediciones.empty()) {
        cout << "No hay mediciones cargadas." << endl;
        return;
    }

    // Ordenar copia para no modificar el vector original
    vector<Medicion> copia = mediciones;
    sort(copia.begin(), copia.end(), compararTemperaturaDesc);

    cout << "\nMAYORES TEMPERATURAS" << endl;
    for (int i = 0; i < 5; i++) {
        cout << i + 1 << ". " << copia[i].sensor << " - " << copia[i].temperatura << " °C" << endl;
    }
}