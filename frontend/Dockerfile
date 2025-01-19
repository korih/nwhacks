# Step 1: Use Node.js official image
FROM node:22 AS build

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy package.json and package-lock.json to install dependencies
COPY package*.json ./

# Step 4: Install dependencies
RUN npm install --legacy-peer-deps

# Step 5: Copy the rest of the application files
COPY . .

# Step 6: Build the application for production
RUN npm run build

# Step 7: Create a new stage for serving the app with a lightweight server
FROM nginx:alpine

# Step 8: Copy the build files from the previous stage to Nginx's default folder
COPY --from=build /app/dist /usr/share/nginx/html

# Step 9: Expose the port the app will run on
EXPOSE 80

# Step 10: Run Nginx to serve the built app
CMD ["nginx", "-g", "daemon off;"]

