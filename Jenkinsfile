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
                withEnv(['GCLOUD_PATH=/usr/lib64/google-cloud-sdk/bin']) {
                    sh '$GCLOUD_PATH/gcloud auth activate-service-account jenkins@terraform-course-349916.iam.gserviceaccount.com --key-file=${GCP_USER} --project=terraform-course-349916'
                    sh '$GCLOUD_PATH/gcloud auth configure-docker us-central1-docker.pkg.dev'
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