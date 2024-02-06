FROM node:21.6.1-alpine3.19 AS build

# Install dependencies only when needed
RUN apk add --no-cache libc6-compat

# Set the working directory inside the container
WORKDIR /app

COPY package*.json ./

# Use cache mount to speed up install of existing dependencies
RUN --mount=type=cache,target=/app/.npm \
  npm set cache /app/.npm && \
  npm ci

COPY . .

RUN npm run build

FROM build

WORKDIR /app

# Set NODE_ENV
ENV NODE_ENV production

USER node

COPY --from=build /app/public ./public
COPY --from=build --chown=node:node /app/.next/standalone ./
COPY --from=build --chown=node:node /app/.next/static ./.next/static

# Expose the ports needed to access the application
# Doesn't acutally do anything to the image, it is just documenation to the user
EXPOSE 3000

# set hostname to localhost
ENV HOSTNAME "0.0.0.0"

CMD ["node", "server.js"]