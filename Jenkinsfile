pipeline {
    agent {
        kubernetes {
            label 'default'
        }
    }

    environment {
        GIT_BRANCH = 'dev'
        IMAGE_NAME = 'uv-fastapi'
        IMAGE_TAG = env.GIT_COMMIT.take(8)
        DOCKER_REGISTRY = 'https://hub.docker.com'
        DOCKERHUB_USERNAME = 'tiendat1011'
    }

    stages {
        stage('Checkout source') {
            steps{
                checkout scm
            }
        }

        stage('Build') {
            steps {
                container('dind') {
                    sh """
                    docker build --no-cache -t ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG}
                    """
                }
            }
        }

        stage('Registry Credentials') {
            steps {
                container('dind') {
                    withRegistry('https://index.docker.io/v1/', 'docker-hub-access-token') {
                    def app = docker.build("${IMAGE_NAME}:${IMAGE_TAG}")
                    app.push()
                }
            }
        }

        stage('Cleanup Docker image') {
            steps {
                script {
                    sh """
                    docker rmi ${DOCKER_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG}
                    """
                }
            }
        }
    }
}