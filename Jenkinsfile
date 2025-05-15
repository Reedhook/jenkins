pipeline {
    agent any

    stages {
        stage('Build Service 1') {
            steps {
                dir('service1') {
                    sh 'docker-compose build'
                    sh 'docker-compose up -d'
                }
            }
        }

        stage('Build Service 2') {
            steps {
                dir('service2') {
                    sh 'docker-compose build'
                    sh 'docker-compose up -d'
                }
            }
        }

        stage('Start Gateway') {
            steps {
                dir('nginx') {
                    sh 'docker-compose up -d'
                }
            }
        }
    }
}