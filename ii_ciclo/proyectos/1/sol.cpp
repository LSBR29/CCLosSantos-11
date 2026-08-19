#include <iostream>     // Imprimir y pedir datos
#include <vector>       // Para tener vectores que usamos para guardar películas
#include <string>       // Para manejar string
#include <fstream>      // Para leer archivos
#include <sstream>      // string stream : Para manejar strings

using namespace std;    // Para evitar errores

// Prototipos
void mostrarMenu();
void registrarPelicula();
void mostrarCatalogo();
void buscarPelicula();
void modificarPelicula();
void eliminarPelicula();
void mostrarEstadisticas();
int buscarCodigo(int codigo);
int leerEntero();

struct Pelicula {
    int codigo;
    string nombre;
    string genero;
    int duracion;
    double calificacion;
};

// Vectores
vector<Pelicula> peliculas;

int main() {
    int opcion = 0;

    while (opcion != 7) {
        mostrarMenu();
        opcion = leerEntero();

        switch (opcion) {
            case 1:
                registrarPelicula();
                break;
            case 2:
                mostrarCatalogo();
                break;
            case 3:
                buscarPelicula();
                break;
            case 4:
                modificarPelicula();
                break;
            case 5:
                eliminarPelicula();
                break;
            case 6:
                mostrarEstadisticas();
                break;
            case 7:
                cout << "\nHasta luego.\n";
                break;
            default:
                cout << "\nOpcion invalida.\n";
        }
    }

    return 0;
}

void mostrarMenu() {
    cout << "\n===== Sistema de Gestion de Peliculas =====\n";
    cout << "1. Registrar pelicula\n";
    cout << "2. Mostrar catalogo\n";
    cout << "3. Buscar pelicula\n";
    cout << "4. Modificar pelicula\n";
    cout << "5. Eliminar pelicula\n";
    cout << "6. Mostrar estadisticas\n";
    cout << "7. Salir\n";
    cout << "Seleccione una opcion: ";
}

void registrarPelicula() {
    Pelicula nueva;
    nueva.codigo = -1;
    nueva.nombre = "";
    nueva.genero = "";
    nueva.duracion = -1;
    nueva.calificacion = -1;

    while (nueva.codigo <= 0) {
        cout << "\nCodigo: ";
        cin >> nueva.codigo;
    }

    if (buscarCodigo(nueva.codigo) != -1) {
        cout << "\nEl codigo ya existe.\n";
        return;
    }

    cin.ignore();

    cout << "Nombre: ";
    getline(cin, nueva.nombre);

    cout << "Genero: ";
    getline(cin, nueva.genero);

    while (nueva.duracion <= 0) {
        cout << "Duracion: ";
        cin >> nueva.duracion;
    }

    while (nueva.calificacion < 0 || nueva.calificacion > 10) {
        cout << "Calificacion: ";
        cin >> nueva.calificacion;
    }

    peliculas.push_back(nueva);

    cout << "\nPelicula registrada correctamente.\n";
}

void mostrarCatalogo() {
    if (peliculas.empty()) {
        cout << "\nNo existen peliculas registradas.\n";
        return;
    }

    cout << endl;

    for (int i = 0; i < peliculas.size(); i++) {
        cout << "Codigo: " << peliculas[i].codigo << endl;
        cout << "Nombre: " << peliculas[i].nombre << endl;
        cout << "Genero: " << peliculas[i].genero << endl;
        cout << "Duracion: " << peliculas[i].duracion << endl;
        cout << "Calificacion: " << peliculas[i].calificacion << endl;
        cout << "-----------------------------\n";
    }
}

void buscarPelicula() {
    int codigo;
    cout << "\nCodigo a buscar: ";
    cin >> codigo;

    int posicion = buscarCodigo(codigo);

    if (posicion == -1) {
        cout << "\nLa pelicula no existe.\n";
        return;
    }

    cout << "\nCodigo: " << peliculas[posicion].codigo << endl;
    cout << "Nombre: " << peliculas[posicion].nombre << endl;
    cout << "Genero: " << peliculas[posicion].genero << endl;
    cout << "Duracion: " << peliculas[posicion].duracion << endl;
    cout << "Calificacion: " << peliculas[posicion].calificacion << endl;
}

void modificarPelicula() {
    int codigo;
    cout << "\nCodigo a modificar: ";
    cin >> codigo;

    int posicion = buscarCodigo(codigo);

    if (posicion == -1) {
        cout << "\nLa pelicula no existe.\n";
        return;
    }

    cin.ignore();

    cout << "Nuevo nombre: ";
    getline(cin, peliculas[posicion].nombre);

    cout << "Nuevo genero: ";
    getline(cin, peliculas[posicion].genero);

    cout << "Nueva duracion: ";
    cin >> peliculas[posicion].duracion;
    while (peliculas[posicion].duracion <= 0) {
        cout << "Nueva duracion: ";
        cin >> peliculas[posicion].duracion;
    }

    cout << "Nueva calificacion: ";
    cin >> peliculas[posicion].calificacion;
    while (peliculas[posicion].calificacion < 0 || peliculas[posicion].calificacion > 10) {
        cout << "Nueva calificacion: ";
        cin >> peliculas[posicion].calificacion;
    }

    cout << "\nPelicula modificada correctamente.\n";
}

void eliminarPelicula() {
    int codigo;
    cout << "\nCodigo a eliminar: ";
    cin >> codigo;

    int posicion = buscarCodigo(codigo);

    if (posicion == -1) {
        cout << "\nLa pelicula no existe.\n";
        return;
    }

    peliculas.erase(peliculas.begin() + posicion);
    cout << "\nPelicula eliminada correctamente.\n";
}

void mostrarEstadisticas() {
    if (peliculas.empty()) {
        cout << "\nNo hay peliculas registradas.\n";
        return;
    }

    double suma = 0.0;
    for (int i = 0; i < peliculas.size(); i++) {
        suma += peliculas[i].calificacion;
    }

    double promedio = suma / peliculas.size();

    cout << "\nCantidad de peliculas: " << peliculas.size() << endl;
    cout << "Calificacion promedio: " << promedio << endl;
}

int buscarCodigo(int codigo) {
    for (int i = 0; i < peliculas.size(); i++) {
        if (peliculas[i].codigo == codigo) {
            return i;
        }
    }
    return -1;
}

int leerEntero() {
    int numero;
    cin >> numero;

    while (cin.fail()) {
        cin.clear();
        cin.ignore(1000, '\n');
        cout << "Entrada invalida.\nIntente nuevamente: ";
        cin >> numero;
    }

    return numero;
}