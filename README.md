# PreSkool - Système de Gestion Scolaire

PreSkool est une application web Django complète pour la gestion d'un établissement scolaire, incluant la gestion des étudiants, enseignants, départements, matières, emplois du temps, examens et congés.

## Fonctionnalités

- **Gestion des utilisateurs** : Rôles Admin, Enseignant, Étudiant avec permissions différenciées.
- **Modules** : Étudiants, Enseignants, Départements, Matières, Emploi du temps, Examens, Congés.
- **Sécurité** : Authentification, autorisation basée sur les rôles, protection CSRF.
- **Interface** : Bootstrap, responsive, avec icônes FontAwesome.
- **Base de données** : SQLite (par défaut), compatible MySQL.

## Installation

### Prérequis

- Python 3.8+
- Git
- Navigateur web

### Étapes

1. **Clonez le dépôt** :
   ```bash
   git clone https://github.com/Oualaaarz/Projet_Python.git
   cd Projet_Python
   ```

2. **Créez un environnement virtuel** :
   ```bash
   python -m venv monenv
   # Sur Windows :
   monenv\Scripts\activate
   # Sur Linux/Mac :
   source monenv/bin/activate
   ```

3. **Installez les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialisez la base de données** :
   ```bash
   python manage.py migrate
   python manage.py loaddata fixtures.json
   ```

5. **Créez les comptes de test** :
   ```bash
   python manage.py shell
   ```
   Dans le shell Python :
   ```python
   from home_auth.models import CustomUser
   from django.contrib.auth.hashers import make_password

   # Admin
   admin = CustomUser.objects.create(
       username='testadmin1@example.com',
       email='testadmin1@example.com',
       first_name='Admin',
       last_name='User',
       is_admin=True,
       is_staff=True,
       is_superuser=True
   )
   admin.password = make_password('Admin@1234')
   admin.save()

   # Teacher
   teacher = CustomUser.objects.create(
       username='testteacher@example.com',
       email='testteacher@example.com',
       first_name='Test',
       last_name='Teacher',
       is_teacher=True
   )
   teacher.password = make_password('Teacher@1234')
   teacher.save()

   # Student
   student = CustomUser.objects.create(
       username='teststudent@example.com',
       email='teststudent@example.com',
       first_name='Test',
       last_name='Student',
       is_student=True
   )
   student.password = make_password('Student@1234')
   student.save()

   exit()
   ```

6. **Lancez le serveur** :
   ```bash
   python manage.py runserver
   ```

7. **Accédez à l'application** :
   Ouvrez http://127.0.0.1:8000 dans votre navigateur.

## Comptes de test

Après création des utilisateurs, utilisez ces comptes :

- **Admin** :
  - Email : testadmin1@example.com
  - Mot de passe : Admin@1234

- **Enseignant** :
  - Email : testteacher@example.com
  - Mot de passe : Teacher@1234

- **Étudiant** :
  - Email : teststudent@example.com
  - Mot de passe : Student@1234

## Structure du projet

- `school/` : Configuration Django principale.
- `home_auth/` : Authentification et utilisateurs personnalisés.
- `student/` : Gestion des étudiants.
- `teacher/` : Gestion des enseignants.
- `department/` : Gestion des départements.
- `subject/` : Gestion des matières.
- `timetable/` : Gestion des emplois du temps.
- `exams/` : Gestion des examens.
- `holidays/` : Gestion des congés.
- `templates/` : Templates HTML.
- `static/` : Fichiers statiques (CSS, JS, images).

## Démonstration vidéo

Regardez la démonstration complète ici : [Lien vers la vidéo](https://www.youtube.com/watch?v=VOTRE_LIEN_ICI)

## Technologies utilisées

- **Backend** : Django 5.1.1
- **Frontend** : HTML, CSS, Bootstrap, FontAwesome
- **Base de données** : SQLite
- **Authentification** : Django Auth avec modèle utilisateur personnalisé

## Contribution

1. Forkez le projet.
2. Créez une branche pour votre fonctionnalité.
3. Commitez vos changements.
4. Poussez vers la branche.
5. Ouvrez une Pull Request.

## Licence

Ce projet est sous licence MIT.