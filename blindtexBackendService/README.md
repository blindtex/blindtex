

```
docker build -t blindtexapi .
docker run -d --name blindtexapi -p 80:80 blindtexapi
```

```
curl --location --request POST 'http://127.0.0.1/readLatexExpression/' --header 'Content-Type: application/json' --data-raw '{ "expression":"(x^2 + y^2 = z^2) + 89/234" }'
```
