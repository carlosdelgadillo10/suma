node {
    def app

    stage('Clone repository') {
        checkout scm
    }
    stage('Install dependencies') {
        // Instalar dependencias Python
        sh 'pip install -r requirements.txt'
    }

    stage('Run tests and coverage') {
        // Ejecutar pruebas y generar informe de cobertura
        sh 'pytest --cov=./app --cov-report=xml:coverage.xml'
    }

    stage('SonarQube Analysis') {
        withSonarQubeEnv('SonarQube') {
            sh """
            sonar-scanner \
                -Dsonar.projectKey=suma-fastapi \
                -Dsonar.projectName="Suma FastAPI" \
                -Dsonar.projectVersion=1.0 \
                -Dsonar.sources=./app \
                -Dsonar.tests=test_suma.py
                -Dsonar.python.coverage.reportPaths=coverage.xml \
                -Dsonar.python.xunit.reportPath=pytest-report.xml \
                -Dsonar.language=python
            """
        }
    }

    stage('Build image') {
        app = docker.build("carlosdelgadillo/sumaa")
    }

    stage('Push image') {
        docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
            app.push("${env.BUILD_NUMBER}")
        }
    }

    stage('SonarQube Analysis') {
    def scannerHome = tool 'sonar-scanner';
    withSonarQubeEnv() {
      sh "${scannerHome}/bin/sonar-scanner"
    }
  }
    
    stage('Trigger ManifestUpdate') {
        echo "hola erdnando"
    }
}

