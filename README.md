# Tarea Semana 6 - Programación Orientada a Objetos

## Estudiante

Stefany Gallegos

## Descripción

Este proyecto corresponde a la tarea de la Semana 6 de la asignatura Programación Orientada a Objetos.

El sistema representa los productos de un restaurante mediante Programación Orientada a Objetos en Python. Para ello se implementó una clase padre llamada **Producto** y dos clases hijas llamadas **Platillo** y **Bebida**. Además, se creó una clase de servicio denominada **Restaurante**, encargada de administrar los productos registrados.

## Estructura del proyecto

```
restaurante_app/
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── platillo.py
│   └── bebida.py
│
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
│
├── main.py
│
└── README.md
```

## Herencia

La herencia se implementó utilizando la clase padre **Producto**, de la cual heredan las clases **Platillo** y **Bebida**. Esto permite reutilizar atributos y métodos comunes evitando repetir código.

## Encapsulación

Se protegió el atributo **__precio** utilizando encapsulación. El acceso y modificación del precio se realiza mediante los métodos:

- obtener_precio()
- cambiar_precio()

Además, el método cambiar_precio() valida que el precio sea mayor que cero antes de modificarlo.

## Polimorfismo

Las clases Platillo y Bebida sobrescriben el método mostrar_informacion().

Cuando el programa recorre la lista de productos del restaurante, cada objeto responde de forma diferente según su tipo, demostrando el principio de polimorfismo.

## Reflexión

La Programación Orientada a Objetos permite desarrollar programas más organizados, reutilizables y fáciles de mantener. La aplicación de herencia, encapsulación y polimorfismo mejora la calidad del código y facilita futuras modificaciones del sistema.
