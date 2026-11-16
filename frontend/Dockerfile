# ---------- Stage 1: build ด้วย Node ----------
FROM node:24-alpine AS build
WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci

COPY . .
# ค่าที่ขึ้นต้นด้วย VITE_ จะถูกฝังลงในไฟล์ JS ตอน Build
ARG VITE_API_URL=/api
ENV VITE_API_URL=$VITE_API_URL
RUN npm run build

# ---------- Stage 2: ให้บริการไฟล์ Static ด้วย Nginx ----------
FROM nginx:alpine AS runtime
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80