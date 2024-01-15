pipeline {
    agent any

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
                //linea de comando para instalar python y pip
                sh 'sudo apt-get install python3.8'
                sh 'pip install -r requirements.txt'  // Instala dependencias
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