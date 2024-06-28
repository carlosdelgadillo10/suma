pipeline {
    agent any

    environment {
        SONARQUBE_SCANNER_HOME = tool 'SonarQube Scanner'
    }

    stages {
        stage('Clone repository') {
            steps {
                checkout scm
            }
        }

        stage('Build image') {
            steps {
                script {
                    // Construir la imagen Docker
                    docker.build("carlosdelgadillo/sumaa")
                }
            }
        }

        stage('Push image') {
            steps {
                script {
                    // Empujar la imagen Docker al registro
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                        dockerImage.push("${env.BUILD_NUMBER}")
                    }
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    // Ejecutar el análisis de SonarQube
                    withSonarQubeEnv('SonarQube Server') {
                        sh "${SONARQUBE_SCANNER_HOME}/bin/sonar-scanner"
                    }
                }
            }
        }
    }

    post {
        always {
            // Limpiar imágenes Docker creadas localmente después de la ejecución del pipeline
            cleanWs()
            docker.image("carlosdelgadillo/sumaa").remove()
        }
    }
}
