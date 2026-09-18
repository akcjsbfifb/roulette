# Ruleta

Simulación de un equipo de 6 jugadores en una ruleta europea (números del 0 al 36). Cada uno apuesta a una chance simple distinta (rojo, negro, alto, bajo, impar, par) y usa la misma estrategia de cuaderno: la apuesta es la suma de los extremos de una secuencia que empieza en `1-2-3-4`.

Al terminar 10.000 giros imprime el balance del equipo y un mensaje: ganó, perdió o empató. El resultado cambia en cada corrida. En general el equipo pierde: el 0 no es ni rojo ni negro, ni alto ni bajo, ni par ni impar, así que esa ronda la mesa se queda con las seis apuestas.

```bash
python main.py
```
