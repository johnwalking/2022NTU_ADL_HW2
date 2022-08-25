#"${1}": path to the context file.
#"${2}": path to the testing file.
#"${3}": path to the output predictions.
python3.8  test_to_swag.py "${1}"  "${2}"  ./test_swag_rm.csv

python3.8  ./runswag.py --do_predict \
--model_name_or_path ./multi_choice_model/ \
--output_dir ./multi_choice_model/  \
--cache_dir ./ \
--test_file  ./test_swag_rm.csv \
--output_file ./test_output_rm.csv  \
--per_gpu_eval_batch_size=2 \
--per_device_train_batch_size=2 


python3.8 test_mc_to_squad.py "${1}"  "${2}"  ./test_output_rm.csv ./test_squad_rm.csv

python3.8  runqa.py --model_name_or_path ./QA_model \
--do_predict \
--output_dir ./QA_model/  \
--cache_dir ./ \
--test_file  ./test_squad_rm.csv \
--per_gpu_eval_batch_size=2 \
--per_device_train_batch_size=2

rm test_output_rm.csv
rm  test_swag_rm.csv
rm test_squad_rm.csv

python3.8 final_output.py ./QA_model/predict_predictions.json  "${3}" 

rm ./QA_model/predict_predictions.json
