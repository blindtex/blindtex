

```
docker build -t blindtexapi .
docker run -d --name blindtexapi -p 80:80 blindtexapi
```

```
curl --location --request POST 'http://127.0.0.1/readLatexExpression/' --header 'Content-Type: application/json' --data-raw '{ "expression":"(x^2 + y^2 = z^2) + 89/234" }'
```

# Despliegue del api

Configurar archivos _Procfile, runtime.txt_ y leer referencias
```

git remote add heroku https://git.heroku.com/blindtex-app.git
heroku buildpacks:clear
heroku buildpacks:set https://github.com/timanovsky/subdir-heroku-buildpack
heroku buildpacks:add heroku/python
heroku config:set PROJECT_PATH=blindtexBackendService/api
git push heroku master


curl --location --request POST 'https://blindtex-app.herokuapp.com/readLatexExpression/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "expression":"(x^2 + y^2 = z^2) + 89/234" 
}'
```

Referencias
* https://medium.com/@timanovsky/heroku-buildpack-to-support-deployment-from-subdirectory-e743c2c838dd
* https://github.com/timanovsky/subdir-heroku-buildpack


# Despliegue de app web

Para facilitar el uso de la app web los archivos index.html y app.js se encuentran en los siguientes puntos

index.html: https://github.com/blindtex/blindtex.github.io/blob/master/app.html
app.js: https://github.com/blindtex/blindtex.github.io/blob/master/js/app.js

para que la app sepa dónde debe realizar el llamado del api es necesario setear al variable `{{site.api_app}}` en el siguiente archivo https://github.com/blindtex/blindtex.github.io/blob/master/_config.yml#L15
