pipeline {
    agent {
        kubernetes {
            inheritFrom 'default'
        }
    }

    environment {
        GIT_BRANCH = 'dev'
        IMAGE_NAME = 'uv-fastapi'
        DOCKERHUB_USERNAME = 'tiendat1011'
        DOCKERHUB_CREDENTIALS = credentials('docker-hub-access-token')
        IMAGE_TAG = 'latest'
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
                    echo "${DOCKERHUB_CREDENTIALS_PSW}" | docker login -u "${DOCKERHUB_CREDENTIALS_USR}" --password-stdin
                    docker build --no-cache -t ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG} .
                    docker push ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG}
                    docker logout
                    """
                }
            }
        }

        stage('Cleanup') {
            steps {
                container('dind') {
                    sh """
                    docker rmi ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG} || true
                    """
                }
            }
        }
    }
}