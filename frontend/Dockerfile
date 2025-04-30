# Usamos una imagen oficial de Node.js
FROM node:20-alpine

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos los archivos necesarios
COPY package*.json ./

# Instalamos las dependencias
RUN npm install

# Copiamos el resto del código
COPY . .

# Construimos la aplicación
RUN npm run build

# Exponemos el puerto 3000 para el servidor de desarrollo
EXPOSE 3000

# Comando para iniciar el servidor
CMD ["npm", "run", "serve"]