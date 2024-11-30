
# Guide d’Installation et de Déploiement

## Introduction du Projet de GASNET Clément et BOULET Paul
Ce projet consiste à déployer une application web basée sur Django connectée à une base de données PostgreSQL dans un environnement conteneurisé avec Docker et orchestré avec Kubernetes. Le guide couvre les étapes nécessaires pour construire les conteneurs, configurer les fichiers YAML pour Kubernetes, et effectuer le déploiement.

---

## Structure du Projet

### Racine du projet
- **`Dockerfile`** : Décrit la construction de l'image Docker pour l'application Django.
- **`docker-compose.yaml`** : (Facultatif) Utilisé pour tester l’application en local avec Docker Compose.
- **`manage.py`** : Point d'entrée de l'application Django.
- **`requirements.txt`** : Dépendances Python nécessaires pour l'application.
- **`README.md`** : Documentation du projet.

### Dossier `compteur_app`
- **Code Django** : Contient les fichiers comme `models.py`, `views.py`, `urls.py`.
- **`migrations/`** : Gère les modifications de la structure de la base de données.
- **`static/`** : Fichiers CSS.
- **`templates/`** : Fichiers HTML, par exemple `counter.html`.

### Dossier `compteur_project`
- **Fichiers de configuration de projet Django** :
  - `settings.py` : Configuration principale, incluant la connexion à la base de données.
  - `urls.py` : Routes de l'application.

### Dossier `k8s`
- **Fichiers YAML pour Kubernetes** :
  - `db-secret.yaml` : Stocke les informations sensibles pour la base de données.
  - `deployment-db.yaml` : Création du pod PostgreSQL.
  - `deployment-django.yaml` : Création du pod pour l'application Django.
  - `postgres-pvc.yaml` : Volume persistant pour les données PostgreSQL.
  - `service-db.yaml` : Service interne exposant PostgreSQL.
  - `service-web.yaml` : Service exposant l'application Django.

---

## Prérequis
- Docker et Kubernetes installés.
- Accès à un cluster Kubernetes (ex. Minikube, AKS, GKE, ou EKS).
- Python 3.10+ et `pip` installés (pour les tests locaux).

---

## Instructions d’Installation et de Déploiement

### 1. Construction des Images Docker
1. Naviguez à la racine du projet :
   ```bash
   cd /chemin/vers/le/projet
   ```
2. Construisez l'image Docker pour l'application Django :
   ```bash
   docker build -t django-app:latest .
   ```

### 2. Test Local avec Docker Compose (Facultatif)
1. Lancez les services :
   ```bash
   docker-compose up
   ```
2. Accédez à l'application via `http://localhost:8000`.

### 3. Création et Gestion de Minikube
1. **Démarrez Minikube** :
   Si Minikube n'est pas déjà démarré, lancez-le avec :
   ```bash
   minikube start
   ```

2. **Vérifiez l'état de Minikube** :
   Assurez-vous que Minikube fonctionne correctement :
   ```bash
   minikube status
   ```

3. **Configurez `kubectl` pour utiliser Minikube** :
   Si ce n'est pas déjà configuré, connectez `kubectl` à Minikube :
   ```bash
   kubectl config use-context minikube
   ```

4. **Déployez les ressources Kubernetes** :
   Une fois que Minikube est prêt, appliquez tous les fichiers YAML du dossier `k8s` :
   ```bash
   kubectl apply -f ./k8s/
   ```

5. **Accédez à l'application** :
   Utilisez Minikube pour obtenir l'URL de l'application :
   ```bash
   minikube service django-service
   ```

---

### 5. Validation du Déploiement
1. Vérifiez que les pods sont en cours d’exécution :
   ```bash
   kubectl get pods
   ```
2. Vérifiez que les services sont exposés :
   ```bash
   kubectl get services
   ```
3. Accédez à l'application via l'URL ou l'adresse IP exposée.



## Conclusion
Ce guide fournit les étapes clés pour déployer une application Django conteneurisée avec Kubernetes. En suivant ces instructions, vous pouvez personnaliser et adapter le déploiement à vos besoins. Pour toute question ou problème, consultez la documentation officielle de [Django](https://docs.djangoproject.com/) et [Kubernetes](https://kubernetes.io/).
