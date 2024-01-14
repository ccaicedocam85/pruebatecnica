pipeline {
    agent any

    import jenkins.plugins.git.*

    stages {
        stage('Clonar Repositorio') {
            steps {
                // Clona el repositorio de GitHub
                git branch: 'develop', url: 'https://github.com/ccaicedocam85/pruebatecnica.git'
            }
        }

        stage('Ejecutar Pruebas Unitarias') {
            steps {
                // Ejecuta pruebas unitarias 
                sh 'pytest tests/'  // Ejecuta pruebas con PyTest
            }
        }
    }

    post {
        always {
            // Siempre limpiar y cerrar conexiones, incluso si el build falla
            cleanWs()
        }
    }
}