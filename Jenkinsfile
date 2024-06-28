node {
    def app

    stage('Clone repository') {
        checkout scm
    }

    stage('Build image') {
        app = docker.build("carlosdelgadillo/sumaa")
    }
    stage('Run Tests and Generate Reports') {
        steps {
            sh '''
            # Crear y activar el entorno virtual
            python -m venv venv
            . venv/bin/activate
            
            # Instalar dependencias
            pip install -r requirements.txt
            
            # Ejecutar pruebas con cobertura
            coverage run -m pytest
            
            # Generar informe XML de cobertura
            coverage xml -o coverage.xml
            
            # Generar informe XML de resultados de pruebas
            pytest --junitxml=pytest-report.xml
            '''
        }
    }

    stage('Push image') {
        docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
            app.push("${env.BUILD_NUMBER}")
        }
    }

    stage('SonarQube Analysis') {
        environment {
            // Reemplaza 'SonarScanner' con el nombre de tu SonarQube Scanner en Jenkins
            SONARQUBE_SCANNER_HOME = tool 'sonar-scanner'
        }
        steps {
            withSonarQubeEnv('SonarQube Server') {
                sh "${SONARQUBE_SCANNER_HOME}/bin/sonar-scanner"
            }
        }
    }
    
    stage('Trigger ManifestUpdate') {
        echo "hola erdnando"
    }
}

