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
        withSonarQubeEnv('server-sonar') {
            // Puedes configurar las opciones de SonarQube según sea necesario
            def scannerHome = tool 'SonarQube Scanner'
            sh "${scannerHome}/bin/sonar-scanner"
        }
    }
    
    stage('Trigger ManifestUpdate') {
        echo "hola erdnando como estas"
    }
}

