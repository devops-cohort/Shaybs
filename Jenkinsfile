pipeline{
	agent any
	stages{
		stage("Update git repository") {
			steps{sh '''ssh 35.242.162.81  << "BOB"
                sudo su - jenkins
                cd Shaybs
                git checkout development-test
                git pull'''
			}
		}
		stage("Reset Systemd") {
			steps{sh '''ssh 35.242.162.81  << BOB
			sudo su - jenkins
			cd Shaybs
                git checkout development-test
			sudo cp flask-app.service /etc/systemd/system/
                sudo systemctl daemon-reload
                sudo systemctl stop flask-app'''
			}
		}
		stage("Initialising project") {
			steps{
				sh '''ssh 35.242.162.81  << "BOB"
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
		stage("Test") {
			steps{
				sh '''ssh 35.242.162.81  << "BOB"
				cd Shaybs
				git checkout development-test
				install_dir=/opt/flask-app
                sudo chown -R pythonadm:pythonadm ${install_dir}
                sudo su - pythonadm << EOF
                cd ${install_dir}
                source venv/bin/activate
                pytest --cov=application . --cov-report=html
				'''
			}
		}
		stage("Deploy") {
			steps{
				sh '''ssh 35.242.162.81  << "BOB"
				sudo su - jenkins
				cd Shaybs
                git checkout development-test
				sudo systemctl start flask-app'''
			}
		}
	}
}