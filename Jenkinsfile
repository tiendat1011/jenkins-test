pipeline {
    agent {
           kubernetes {
            inheritFrom 'docker'
            yaml """
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: docker
    image: docker:24.0.7-dind
    securityContext:
      privileged: true
    tty: true
  - name: builder
    image: docker:24.0.7-cli
    command:
    - cat
    tty: true
    volumeMounts:
    - name: dind-storage
      mountPath: /var/lib/docker
  volumes:
  - name: dind-storage
    emptyDir: {}
"""
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
                sh "printenv"
            }
        }

        stage('Build') {
            steps {
                script {
                    sh """
                    docker build --no-cache -t ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG}
                    """
                }
            }
        }

        stage('Push') {
            steps {
                script {
                    sh """
                    docker push ${DOCKER_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG}
                    """
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