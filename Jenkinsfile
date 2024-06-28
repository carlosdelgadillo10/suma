node {
    def app

    stage('Clone repository') {
        checkout scm
    }

    stage('Build image') {
        app = docker.build("carlosdelgadillo/sumaa")
    }
    stages {
        stage('Run Tests and Generate Reports') {
            steps {
                sh '''
                # Crear el entorno virtual
                python -m venv venv
                
                # Activar el entorno virtual
                . venv/bin/activate
                
                # Instalar dependencias
                pip install --upgrade pip
                pip install -r requirements.txt
                
                # Ejecutar pruebas con cobertura
                venv/bin/coverage run -m pytest
                
                # Generar informe XML de cobertura
                venv/bin/coverage xml -o coverage.xml
                
                # Generar informe XML de resultados de pruebas
                venv/bin/pytest --junitxml=pytest-report.xml
                '''
            }
        }
        stage('Publish Results') {
            steps {
                // Publicar la cobertura de código
                publishCoverage adapters: [coberturaAdapter('coverage.xml')], sourceFileResolver: sourceFiles('NEVER_STORE')
                
                // Publicar los resultados de las pruebas
                junit 'pytest-report.xml'
            }
        }
    }
    post {
        always {
            // Limpiar el entorno
            sh 'rm -rf venv'
        }
    }
}

