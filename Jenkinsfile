node {
    def app

    stage('Clone repository') {
        checkout scm
    }

    stage('Build image') {
        app = docker.build("carlosdelgadillo/sumaa")
    }
    stage('Run Tests and Generate Coverage') {
        steps {
            sh '''
            python -m venv venv
            . venv/bin/activate
            pip install -r requirements.txt
            pytest --cov=app --cov-report=xml --cov-report=html
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

