#wget -P  https://www.dropbox.com/sh/6bcsormzzzp60nf/AADSoSwr8-Qmx79sXf8ZziVVa?dl=1 -O ./multi_choice_model
#wget -P https://www.dropbox.com/sh/npd8zmn21az2n48/AAAIczUr0v_dp-OvJCngTVWwa?dl=1 -O ./QA_model
#wget -P  ./multi_choice_model https://www.dropbox.com/sh/6bcsormzzzp60nf/AADSoSwr8-Qmx79sXf8ZziVVa?dl=1 
#wget -P  ./QA_model https://www.dropbox.com/sh/npd8zmn21az2n48/AAAIczUr0v_dp-OvJCngTVWwa?dl=1 

wget  -O multi_choice_model.zip  https://www.dropbox.com/sh/6bcsormzzzp60nf/AADSoSwr8-Qmx79sXf8ZziVVa
wget  -O QA_model.zip https://www.dropbox.com/sh/npd8zmn21az2n48/AAAIczUr0v_dp-OvJCngTVWwa

mkdir ./multi_choice_model
mkdir ./QA_model

unzip ./multi_choice_model.zip -d ./multi_choice_model
unzip ./QA_model -d ./QA_model 
