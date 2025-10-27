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
        DOCKERHUB_CREDENTIALS = credentials('a2b6705a-b4a4-4e07-80b7-b33fca283e83')
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