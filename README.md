# BlindTex
-----------
[![Build Status](https://travis-ci.org/blindtex/blindtex.svg?branch=master)](https://travis-ci.org/blindtex/blindtex) [![Coverage Status](https://coveralls.io/repos/github/blindtex/blindtex/badge.svg?branch=master)](https://coveralls.io/github/blindtex/blindtex?branch=master)

## ¿ En qué creemos ?

El equipo BlindTex cree la posibilidad de eliminar barreras que impiden el acceso al conocimiento científico, de manera que personas con discapacidad visual logren mayor autonomía a nivel personal, académico y laboral. Más información [aquí](http://blindtex.org/)

## ¿ Qué es Blindtex ?

BlindTex es una herramienta de accesibilidad que realiza conversión de ecuaciones escritas en formato latex a lenguaje natural.

## Instalación
```
$ pip3 install blindtex
```

La conversión de usa como se muetra a continuación:
```
$ blindtex -e '\frac{2}{3+4}'
  fracción 2 sobre 3 más 4 finFracción
```

## Testing

```
# run the tests

python3 -m pytest
```
##Licencia
TODO
