#!/bin/bash

echo "��� Criando portfólio Edder Gaddini..."

# Criar index.html
cat > index.html << 'EOF'
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Edder Gaddini - Engenheiro de Software Flutter | Mobile & Full Stack Developer">
    <title>Edder Gaddini | Flutter Engineer</title>
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="https://unpkg.com/aos@2.3.1/dist/aos.css">
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <nav class="navbar" id="navbar">
        <div class="container">
            <a href="#" class="logo">&lt;EdderGaddini/&gt;</a>
            <ul class="nav-menu">
                <li><a href="#about">Sobre</a></li>
                <li><a href="#skills">Skills</a></li>
                <li><a href="#projects">Projetos</a></li>
                <li><a href="#contact" class="btn-nav">Contato</a></li>
            </ul>
        </div>
    </nav>

    <section class="hero">
        <div class="container">
            <p class="greeting">Olá, eu sou</p>
            <h1>Edder <span class="highlight">Gaddini</span></h1>
            <h2>Engenheiro de Software Flutter</h2>
            <p class="description">6+ anos de experiência | 500K+ usuários impactados | Clean Architecture</p>
            <div class="cta-buttons">
                <a href="#projects" class="btn btn-primary">Ver Projetos</a>
                <a href="assets/documents/cv.pdf" class="btn btn-secondary" download>Download CV</a>
            </div>
            <div class="social-links">
                <a href="https://github.com/EdderGaddini" target="_blank"><i class="fab fa-github"></i></a>
                <a href="https://linkedin.com/in/eddergaddini" target="_blank"><i class="fab fa-linkedin"></i></a>
                <a href="mailto:eddergaddini.recruiters@gmail.com"><i class="fas fa-envelope"></i></a>
            </div>
        </div>
    </section>

    <section id="about" class="section">
        <div class="container">
            <h2 data-aos="fade-up"><span class="number">01.</span> Sobre Mim</h2>
            <div class="about-content">
                <div data-aos="fade-right">
                    <p>Engenheiro de Software Sênior com 6+ anos em Flutter/Dart, construindo aplicações mobile que atendem 500K+ usuários.</p>
                    <p>Especialista em Clean Architecture, BLoC Pattern e desenvolvimento multiplataforma.</p>
                </div>
            </div>
        </div>
    </section>

    <section id="skills" class="section section-dark">
        <div class="container">
            <h2 data-aos="fade-up"><span class="number">02.</span> Skills</h2>
            <div class="skills-grid">
                <div class="skill-card" data-aos="fade-up">
                    <i class="fas fa-mobile-alt"></i>
                    <h3>Mobile</h3>
                    <p>Flutter, Dart, Kotlin, Swift</p>
                </div>
                <div class="skill-card" data-aos="fade-up">
                    <i class="fas fa-server"></i>
                    <h3>Backend</h3>
                    <p>Node.js, Java, Spring Boot, Firebase</p>
                </div>
                <div class="skill-card" data-aos="fade-up">
                    <i class="fas fa-cloud"></i>
                    <h3>Cloud</h3>
                    <p>AWS, GCP, Firebase, CI/CD</p>
                </div>
            </div>
        </div>
    </section>

    <section id="projects" class="section">
        <div class="container">
            <h2 data-aos="fade-up"><span class="number">03.</span> Projetos</h2>
            <div id="projects-grid" class="projects-grid"></div>
        </div>
    </section>

    <section id="contact" class="section section-dark">
        <div class="container">
            <div class="contact-content" data-aos="fade-up">
                <h2>Vamos Conversar?</h2>
                <p>Estou sempre aberto a novos projetos e oportunidades.</p>
                <a href="mailto:eddergaddini.recruiters@gmail.com" class="btn btn-primary btn-large">Enviar Email</a>
            </div>
        </div>
    </section>

    <footer>
        <p>© 2025 Edder Gaddini. Feito com ❤️</p>
    </footer>

    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script src="js/projects.js"></script>
    <script src="js/main.js"></script>
</body>
</html>
EOF

echo "✅ index.html criado!"

# Continua com os outros arquivos...
# Vou criar um script que você pode executar

chmod +x setup_portfolio.sh
echo "✅ Script setup criado! Execute: bash setup_portfolio.sh"

