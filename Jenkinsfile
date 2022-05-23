pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script{
                    app = docker.build("my build")
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}