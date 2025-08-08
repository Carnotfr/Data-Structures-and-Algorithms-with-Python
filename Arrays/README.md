Was ist ein Array
Ein Array ist eine Sammlung von Elementen gleichen Typs, die kontigu im Speicher liegen und über einen ganzzahligen Index angesprochen werden (in den meisten Sprachen ab 0). Hauptideen:

Indexzugriff ist O(1): du kannst direkt auf A[i] zugreifen.

Speicheradresse von A[i] = Base_address + i * sizeof(element).

Bei festen (statischen) Arrays ist die Länge zur Compile-/Erstellungszeit fix; bei dynamischen Arrays (z. B. Python-list, C mit realloc) kann die Größe wachsen.

