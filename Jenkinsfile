pipeline{
	agent any
	stages{
		stage("Update git repository") {
			steps{
				sh '''
				ssh 34.89.12.90  << "BOB"
                sudo su - jenkins
                #!/bin/bash
                cd Shaybs
                git checkout development-test
                git pull'''
			}
		}
		stage("Reset Systemd") {
			steps{
				sh '''
				ssh 34.89.12.90  << BOB
				sudo su - jenkins
				cd Shaybs
                git checkout development-test
				# install the service script
                sudo cp flask-app.service /etc/systemd/system/
                # reload the service scripts
                sudo systemctl daemon-reload
                # stop the old service
                sudo systemctl stop flask-app
                # configure python virtual environment and install dependencies'''
			}
		}
		stage("Initialising project") {
			steps{
				sh '''ssh 34.89.12.90  << "BOB"
				sudo su - jenkins
				cd Shaybs
                git checkout development-test
                # configure python virtual environment and install dependencies
                install_dir=/opt/flask-app
                sudo rm -rf ${install_dir}
                sudo mkdir ${install_dir}
                sudo cp -r ./* ${install_dir}
                sudo chown -R pythonadm:pythonadm ${install_dir}
                sudo su - pythonadm << EOF
                cd ${install_dir}
                virtualenv -p python3 venv
                source venv/bin/activate
                pip3 install -r requirements.txt
                '''
			}
		}
		stage("Deploy") {
			steps{
				sh '''ssh 34.89.12.90  << "BOB"
				sudo su - jenkins
				cd Shaybs
                git checkout development-test
				sudo systemctl start flask-app'''
			}
		}
	}
}