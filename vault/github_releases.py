import requests

class GitHubReleases:
    def __init__(self, owner, repo, token=None):
        """
        Initialisation de la classe avec les informations du dépôt GitHub.

        :param owner: Le propriétaire du dépôt (nom d'utilisateur ou organisation)
        :param repo: Le nom du dépôt GitHub
        :param token: Un token GitHub pour l'authentification (facultatif)
        """
        self.owner = owner
        self.repo = repo
        self.token = token
        self.base_url = f"https://api.github.com/repos/{owner}/{repo}/tags"

    def _get_headers(self):
        """Retourne les en-têtes de la requête avec l'authentification si nécessaire."""
        headers = {}
        if self.token:
            headers["Authorization"] = f"token {self.token}"
        return headers

    def get_all_releases(self):
        """
        Récupère toutes les releases du dépôt, avec gestion de la pagination.

        :return: Liste de toutes les releases
        """
        releases = []
        url = self.base_url

        while url:
            response = requests.get(url, headers=self._get_headers())
            
            # Vérifier si la requête a réussi
            if response.status_code == 200:
                releases_data = response.json()
                releases.extend(releases_data)
                
                # Vérifier s'il y a une page suivante (utilisation des liens 'next')
                if 'next' in response.links:
                    url = response.links['next']['url']
                else:
                    break
            else:
                print(f"Erreur {response.status_code}: {response.text}")
                break

        return releases

    def display_releases(self):
        """
        Affiche les releases récupérées du dépôt.

        :return: Rien, mais affiche les informations sur les releases dans la console
        """
        releases = self.get_all_releases()

        print(f"Nombre total de releases récupérées : {len(releases)}")
        for release in releases:
            print(f"Version : {release['name']}")
            print(f"Date de publication : {release['published_at']}")
            print(f"URL : {release['html_url']}")
            print("-" * 50)