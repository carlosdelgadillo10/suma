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
      sh "${scannerHome}/bin/sonar-scanner -sonar.projectKey=${suma-fastapi} -sonar.projectName=${Suma FastAPI} -sonar.branch=${main}  -sonar.projectVersion=${1.0} -sonar.sources=${./app}. -sonar.language=${python}  -sonar.python.xunit.reportPath=${pytest-report.xml}" // -Dsonar.python.coverage.reportPaths=${params.COVERAGE}"
    }
  }
    
    stage('Trigger ManifestUpdate') {
        echo "hola erdnando"
    }
}

