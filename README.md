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

Se puede realizar conversión de equiaciones suministrando un diccionario en formato json. En la carpeta _example_ se encuentra un diccionario de prueba. la conversión con un diccionario personalizado se usa como se muestra a continuación:
```
$ cd examples
$ blindtex -e '\frac{3}{3+x}' -d example_dict.json
  Inicia Fracción 3 Sobre 3 más x Fin Fracción
```

## Testing

```
# run the tests

python3 -m pytest
```
##Licencia
TODO
