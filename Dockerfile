# ---------- Etapa 1: Build ----------
FROM node:20-alpine AS builder

# Crear directorio de la app
WORKDIR /app

# Copiar archivos de dependencias
COPY package*.json ./

# Instalar dependencias
RUN npm install

# Copiar todo el código fuente
COPY . .

# Construir el proyecto para producción
RUN npm run build

# ---------- Etapa 2: Runtime ----------
FROM node:20-alpine

# Establecer directorio de trabajo
WORKDIR /app

# Copiar solo lo necesario desde la etapa de build
COPY --from=builder /app/.output ./.output
COPY --from=builder /app/package*.json ./

# Instalar dependencias de producción solamente
RUN npm install --omit=dev

# Exponer el puerto por defecto de Nuxt
EXPOSE 3000

# Comando para ejecutar Nuxt en producción
CMD ["node", ".output/server/index.mjs"]