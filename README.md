# Projet 10 DA Python Open Classrooms

## Installation


- Clonez le repo :

```
git clone 8astien/P10BC
```

- Créer un environnement virtuel dans le projet :
```
python -m venv env
```

- Activer l'environnement virtuel :
- Linux :
```
source env/bin/activate
```
- Windows :
```
env\Scripts\activate.bat
```

- Installer les packages nécessaires à partir du fichier requirements.txt : :
```
pip install -r requirements.txt
```
- Aller dans le répertoire softdesk et lancer le serveur local :
```
cd softdesk
python manage.py runserver
```

## Administration

Pour accéder à l'interface d'administration de Django, vous devez créer un compte superutilisateur.

- Créer un superuser :
```
python manage.py createsuperuser
```
- Démarrer le serveur de développement :
```
python manage.py runserver
```
- Aller sur http://127.0.0.1:8000/admin et connectez-vous avec les logs que vous venez de créer.

# Flake8

La PEP 8 (Style guide for Python Code) de Python est un ensemble de conventions permettant d’écrire du beau code Python. flake8 est un des outils mis à disposition par la communauté pour aider à valider son code Python au regard de la PEP 8.
- Fichier de config : tox.ini
- Génération de rapport :
```
flake8
```
Vous pouvez accéder au détail du rapport dans le dossier flake-report.

# Endpoints de l'API

### Utilisateurs

- **Créer un compte :**
  - `POST /api/sign-up/`

- **Se connecter :**
  - `POST /api/login/`

- **Gestion des tokens :**
  - `POST /api/token/` (Obtenir un nouveau token)
  - `POST /api/token/refresh/` (Rafraîchir le token d'accès)

- **Gestion des utilisateurs :**
  - `GET /api/users/` (Lister tous les utilisateurs)
  - `GET /api/users/{user_id}/` (Récupérer un utilisateur spécifique)
  - `PATCH /api/users/{user_id}/` (Mettre à jour un utilisateur spécifique)
  - `DELETE /api/users/{user_id}/` (Supprimer un utilisateur spécifique)
  - `GET /api/users/{user_id}/projects/{project_id}/issues/` (Lister tous les issues assignés à un utilisateur pour un projet spécifique)

### Projets

- **Gestion des projets :**
  - `POST /api/projects/` (Créer un nouveau projet)
  - `GET /api/projects/` (Lister tous les projets)
  - `GET /api/projects/{project_id}/` (Récupérer un projet spécifique)
  - `PATCH /api/projects/{project_id}/` (Mettre à jour un projet spécifique)
  - `DELETE /api/projects/{project_id}/` (Supprimer un projet spécifique)

- **Gestion des contributeurs :**
  - `PATCH /api/projects/{project_id}/add-contributor/` (Ajouter un contributeur à un projet)
  - `PATCH /api/projects/{project_id}/delete-contributor/` (Supprimer un contributeur d'un projet)

### Issues

- **Gestion des issues :**
  - `POST /api/projects/{project_id}/issues/` (Créer un nouvel issue pour un projet)
  - `GET /api/projects/{project_id}/issues/` (Lister tous les issues pour un projet)
  - `GET /api/projects/{project_id}/issues/{issue_id}/` (Récupérer un issue spécifique pour un projet)
  - `PATCH /api/projects/{project_id}/issues/{issue_id}/change-status/` (Changer le statut d'un issue)
  - `PATCH /api/projects/{project_id}/issues/{issue_id}/assign-contributor/` (Assigner un contributeur à un issue)
  - `DELETE /api/projects/{project_id}/issues/{issue_id}/` (Supprimer un issue pour un projet)

### Commentaires

- **Gestion des commentaires :**
  - `POST /api/issues/{issue_id}/comments/` (Créer un nouveau commentaire pour un issue)
  - `GET /api/issues/{issue_id}/comments/` (Lister tous les commentaires pour un issue)
  - `GET /api/issues/{issue_id}/comments/{comment_id}/` (Récupérer un commentaire spécifique pour un issue)
  - `PATCH /api/issues/{issue_id}/comments/{comment_id}/` (Mettre à jour un commentaire spécifique pour un issue)
  - `DELETE /api/issues/{issue_id}/comments/{comment_id}/` (Supprimer un commentaire spécifique pour un issue)
