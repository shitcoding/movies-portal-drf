# Заданиe на 2 спринт
 
1. `docker_compose` — задача про настройку Nginx, Docker и Django.
2. `django_api` — задача про реализацию API для выдачи информации о фильме.

---
## Usage

```sh
git clone https://github.com/shitcoding/new_admin_panel_sprint_2/
cd new_admin_panel_sprint_2
make help

# dev-docker-down                Stop containers and remove volumes in dev mode
# dev-docker-up                  Start containers in dev mode
# django-superuser               Create django superuser
# dotenv                         Create .env files (if they don't exist) from template .env.example files
# dummy-django-superuser         Autocreate test django superuser with predefined login/pass
# help                           Display this help
# prod-docker-down               Stop containers and remove volumes in production mode
# prod-docker-up                 Start containers in production mode

cd movies_admin
make help

# compile-translation            Compile translation
# dummy-superuser                Autocreate test superuser with predefined login/pass
# dummy-superuser-docker         Autocreate test superuser (when running app in Docker)
# help                           Display this help
# install                        Create venv and install app dependencies via poetry (to run app locally)
# makemigrations                 Create new migrations if required
# migrate                        Apply django migrations
# migrate-docker                 Apply django migrations (when running app in Docker)
# run-dev-server                 Run django dev server
# superuser                      Create django superuser
# superuser-docker               Create django superuser (when running app in Docker)
# translation                    Prepare files for translation

```
