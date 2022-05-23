pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script{
                    app = docker.build "us-central1-docker.pkg.dev/terraform-course-349916/testingrepo/python-api:${env.BUILD_ID}"
                }
            }
        }
        stage('Run gcloud') {
            steps {
                echo 'Pushing repo....'
                withCredentials([file(credentialsId: 'key-sa', variable: 'GCP_USER')]) {
                    sh("gcloud auth activate-service-account --key-file=${GCP_USER}")
                    sh("gcloud auth configure-docker us-central1-docker.pkg.dev")
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