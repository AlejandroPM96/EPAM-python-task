pipeline {
    agent any

    stages {
        stage('Run gcloud') {
            steps {
                echo 'setting the gcloud build...'
                withCredentials([file(credentialsId: 'GCP_USER', variable: 'GC_KEY')]) {
                    sh("gcloud auth activate-service-account --key-file=${GC_KEY}")
                    sh("gcloud auth configure-docker us-central1-docker.pkg.dev")
                }
            }
        }

        stage('Build') {
            steps {
                echo 'BUilding and pushing'
                script{
                    app = docker.build "us-central1-docker.pkg.dev/terraform-course-349916/testingrepo/python-api"
                    app.push "${env.BUILD_ID}"
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'BUilding and pushing'
                withCredentials([file(credentialsId: 'GCP_USER', variable: 'GC_KEY')]) {
                    sh("gcloud auth activate-service-account --key-file=${GC_KEY}")
                    sh("gcloud run deploy python-assignment --image us-central1-docker.pkg.dev/terraform-course-349916/testingrepo/python-api:${env.BUILD_ID} --region us-central1 --allow-unauthenticated")
                }
            }
        }
    }
}