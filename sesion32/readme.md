## Comandos utiles

1. Instalar el ORM

```
npm install sequelize
```

2. Inicializar estructura de proyecto

```
npx sequelize-cli init
```

3. Crear la base de datos

```
npx sequelize-cli db:create
```

4. Create un modelo

```
npx sequelize-cli model:generate --name Product --atributes title:string,price:flot,description:string
```

5. Ejecutar migraciones

```
npx sequelize-cli db:migrate
```

