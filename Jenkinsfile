node {
    def app

    stage('Clone repository') {
        checkout scm
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
    withSonarQubeEnv('Sonarqube') {
      sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=${suma-fastapi} -Dsonar.projectName=${Suma FastAPI} -Dsonar.branch=${main}  -Dsonar.projectVersion=${1.0} -Dsonar.sources=${./app}. -Dsonar.language=${python}  -Dsonar.python.xunit.reportPath=${pytest-report.xml}" // -Dsonar.python.coverage.reportPaths=${params.COVERAGE}"
    }
  }
    
    stage('Trigger ManifestUpdate') {
        echo "hola erdnando"
    }
}

