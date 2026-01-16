#!/usr/bin/env python3
"""
GitHub Tier Calculator
Calcula o tier do usuário baseado em commits anuais e atualiza o README.md
"""

import os
import re
import sys
from datetime import datetime, timedelta
from typing import Dict, Tuple

try:
    import requests
except ImportError:
    print("❌ requests não instalado. Instalando...")
    os.system(f"{sys.executable} -m pip install requests")
    import requests


class TierCalculator:
    """Calcula tier baseado em estatísticas do GitHub"""
    
    # Tiers e suas necessidades (commits por ano)
    TIERS = [
        ("S+", "🔥", "Elite", 2500),
        ("S", "⭐", "Master", 1000),
        ("A+", "💎", "Diamond", 500),
        ("A", "💎", "Platinum", 250),
        ("B+", "🥇", "Gold", 100),
        ("B", "🥈", "Silver", 50),
        ("C+", "🥉", "Bronze", 25),
        ("C", "🌱", "Iniciante", 0),
    ]
    
    def __init__(self, username: str, token: str = None):
        self.username = username
        self.token = token
        self.headers = {"Authorization": f"token {token}"} if token else {}
        
    def get_commits_last_year(self) -> int:
        """Busca total de commits do último ano"""
        try:
            one_year_ago = (datetime.now() - timedelta(days=365)).isoformat()
            
            # Busca eventos de commit do usuário
            url = f"https://api.github.com/users/{self.username}/events"
            all_commits = 0
            page = 1
            
            while page <= 10:  # Limita a 10 páginas para evitar rate limit
                response = requests.get(
                    f"{url}?page={page}&per_page=100",
                    headers=self.headers,
                    timeout=10
                )
                
                if response.status_code != 200:
                    print(f"⚠️  Aviso: Status {response.status_code} ao buscar eventos")
                    break
                    
                events = response.json()
                if not events:
                    break
                
                # Conta pushes do último ano
                for event in events:
                    if event.get("type") == "PushEvent":
                        event_date = datetime.strptime(
                            event["created_at"], 
                            "%Y-%m-%dT%H:%M:%SZ"
                        )
                        if event_date.isoformat() >= one_year_ago:
                            commits = event.get("payload", {}).get("commits", [])
                            all_commits += len(commits)
                
                page += 1
            
            # Adiciona estatísticas dos repos do usuário
            repos_url = f"https://api.github.com/users/{self.username}/repos"
            response = requests.get(repos_url, headers=self.headers, timeout=10)
            
            if response.status_code == 200:
                repos = response.json()
                for repo in repos:
                    # Pula forks
                    if repo.get("fork"):
                        continue
                    
                    # Busca commits do repo
                    commits_url = f"https://api.github.com/repos/{self.username}/{repo['name']}/commits"
                    params = {
                        "author": self.username,
                        "since": one_year_ago,
                        "per_page": 1
                    }
                    
                    commit_response = requests.get(
                        commits_url, 
                        headers=self.headers,
                        params=params,
                        timeout=10
                    )
                    
                    if commit_response.status_code == 200:
                        # GitHub retorna header com total de commits
                        link_header = commit_response.headers.get("Link", "")
                        if "last" in link_header:
                            # Extrai número da última página
                            match = re.search(r'page=(\d+)>; rel="last"', link_header)
                            if match:
                                all_commits += int(match.group(1))
            
            return all_commits
            
        except Exception as e:
            print(f"❌ Erro ao buscar commits: {e}")
            return 0
    
    def get_github_stats(self) -> Dict[str, int]:
        """Busca estatísticas gerais do GitHub"""
        try:
            url = f"https://api.github.com/users/{self.username}"
            response = requests.get(url, headers=self.headers, timeout=10)
            
            if response.status_code != 200:
                print(f"❌ Erro ao buscar stats: {response.status_code}")
                return {}
            
            data = response.json()
            
            # Busca stars totais
            repos_url = f"https://api.github.com/users/{self.username}/repos"
            repos_response = requests.get(repos_url, headers=self.headers, timeout=10)
            total_stars = 0
            
            if repos_response.status_code == 200:
                repos = repos_response.json()
                total_stars = sum(repo.get("stargazers_count", 0) for repo in repos)
            
            return {
                "public_repos": data.get("public_repos", 0),
                "followers": data.get("followers", 0),
                "total_stars": total_stars,
            }
            
        except Exception as e:
            print(f"❌ Erro ao buscar stats gerais: {e}")
            return {}
    
    def calculate_tier(self, commits: int) -> Tuple[str, str, str]:
        """
        Calcula o tier baseado no número de commits
        Retorna: (tier, emoji, nome)
        """
        for tier_name, emoji, tier_label, min_commits in self.TIERS:
            if commits >= min_commits:
                return tier_name, emoji, tier_label
        
        return "C", "🌱", "Iniciante"
    
    def update_readme(self, commits: int, stats: Dict[str, int]):
        """Atualiza o README.md com as estatísticas"""
        readme_path = "README.md"
        
        if not os.path.exists(readme_path):
            print(f"❌ {readme_path} não encontrado!")
            return False
        
        try:
            with open(readme_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Calcula tier
            tier_name, emoji, tier_label = self.calculate_tier(commits)
            
            # Prepara nova seção de stats
            new_stats = f"""<div align="center">

### 📊 Stats do Ano

| Métrica | Valor |
|---------|-------|
| 📝 Total de Commits | {commits:,} |
| ⭐ Stars Recebidas | {stats.get('total_stars', 0)} |
| 📦 Repositórios Públicos | {stats.get('public_repos', 0)} |
| 👥 Seguidores | {stats.get('followers', 0)} |

### 🎖️ Sistema de Tiers

```
🔥 S+  → Elite      (2500+ commits/ano)
⭐ S   → Master     (1000+ commits/ano)
💎 A+  → Diamond    (500+ commits/ano)
💎 A   → Platinum   (250+ commits/ano)
🥇 B+  → Gold       (100+ commits/ano)
🥈 B   → Silver     (50+ commits/ano)
🥉 C+  → Bronze     (25+ commits/ano)
🌱 C   → Iniciante  (0+ commits/ano)
```

**Tier Atual:** {emoji} {tier_name} ({tier_label})

</div>"""
            
            # Substitui seção entre os comentários
            pattern = r"<!-- TIER_STATS_START -->.*?<!-- TIER_STATS_END -->"
            replacement = f"<!-- TIER_STATS_START -->\n{new_stats}\n<!-- TIER_STATS_END -->"
            
            new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
            
            # Atualiza badges no topo
            tier_badge = f"![Tier](https://img.shields.io/badge/Tier-{tier_name.replace('+', '%2B')}-FF0000?style=for-the-badge&logo=github&logoColor=white)"
            commits_badge = f"![Commits](https://img.shields.io/badge/Commits-{commits:,}-blue?style=for-the-badge&logo=git)"
            
            new_content = re.sub(
                r"!\[Tier\]\(.*?\)",
                tier_badge,
                new_content,
                count=1
            )
            new_content = re.sub(
                r"!\[Commits\]\(.*?\)",
                commits_badge,
                new_content,
                count=1
            )
            
            # Salva arquivo
            with open(readme_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            
            print(f"✅ README atualizado!")
            print(f"   Tier: {emoji} {tier_name} ({tier_label})")
            print(f"   Commits: {commits:,}")
            print(f"   Stars: {stats.get('total_stars', 0)}")
            
            return True
            
        except Exception as e:
            print(f"❌ Erro ao atualizar README: {e}")
            return False


def main():
    """Função principal"""
    username = os.getenv("GITHUB_REPOSITORY", "").split("/")[0]
    
    if not username:
        username = "EdderGaddini"
        print(f"⚠️  GITHUB_REPOSITORY não definido, usando: {username}")
    
    token = os.getenv("GITHUB_TOKEN")
    
    if not token:
        print("⚠️  GITHUB_TOKEN não definido. Limitado a 60 requisições/hora.")
    
    print(f"🔍 Calculando tier para @{username}...")
    
    calculator = TierCalculator(username, token)
    
    # Busca dados
    print("📊 Buscando commits do último ano...")
    commits = calculator.get_commits_last_year()
    
    print("📈 Buscando estatísticas gerais...")
    stats = calculator.get_github_stats()
    
    # Atualiza README
    print("📝 Atualizando README...")
    calculator.update_readme(commits, stats)
    
    print("\n✨ Processo concluído!")


if __name__ == "__main__":
    main()
