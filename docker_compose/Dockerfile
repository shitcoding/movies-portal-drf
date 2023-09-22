#### Build stage ####
FROM python:3.11-alpine as builder

# Set work directory
WORKDIR /usr/src/app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set up build mode (dev, staging or production)
ARG BUILD_MODE
ENV MODE=${BUILD_MODE}

# Install psycopg2 dependencies
RUN apk update && apk add --no-cache \
  # postgresql-dev \
  # gcc \
  # python3-dev \
  # musl-dev \
  # curl \
  make

COPY . .

# Create wheels for project dependencies
RUN pip install --no-cache-dir --upgrade pip
# Install poetry and create requirements.txt
RUN pip install --no-cache-dir poetry
# Export dependencies to requirements.txt:
# - with dev dependencies if MODE=dev,
# - without dev dependencies if MODE=production
RUN make reqs
# Create wheels
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt


# # Create wheels for project dependencies
# RUN pip install --no-cache-dir --upgrade pip && \
#   # Install poetry and create requirements.txt
#   pip install --no-cache-dir poetry==1.4.2 && \
#   # Export dependencies to requirements.txt:
#   # - with dev dependencies if MODE=dev,
#   # - without dev dependencies if MODE=production
#   make reqs && \
#   # Create wheels
#   pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt


#### Final stage ####
FROM python:3.11-alpine

# Create appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

# Install dependencies
RUN apk update && apk add --no-cache \
  libpq \
  make \
  gettext
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --no-cache-dir /wheels/*

# Copy project files
COPY . $APP_HOME

# Create non-root app user, chown all files to the app user
RUN addgroup -S app && adduser -S app -G app && chown -R app:app $APP_HOME

# Change to the app user
USER app
