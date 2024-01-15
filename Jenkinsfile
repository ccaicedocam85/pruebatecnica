pipeline {
    agent any
    
    environment {
        PATH = "/var/lib/jenkins/.local/bin:${env.PATH}"
    }

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
                sh 'pip install -r requirements.txt'  // Instala dependencias
                sh 'pytest tests/'  // Ejecuta pruebas con PyTest
            }
        }
        //Construir la imagen de Docker y subirla a un registro público como Docker Hub.
        stage('Construir Imagen Docker') {
            steps {
                sh 'docker build -t docker push cristec85/prueba:latest .'  // Construye la imagen
                sh 'docker push cristec85/prueba:latest'  // Sube la imagen a Docker Hub
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