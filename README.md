1. Convert test.json/ train.json/ valid.json  to swag dataset foamt

"""
Python3  test_to_swag.py ./data/context.json ./data/test.json  ./multi_choice_data/test_swag.csv
"""

2. Training the multi-choice model based on bert-base-chinese 
 
"""
python3 ./runswag.py \
--model_name_or_path bert-base-chinese  \
--do_train \
--do_eval \
--learning_rate 3e-5 \
--num_train_epochs 3  \
--train_file  '  ./multi_choice_data/train_swag.csv' \
--validation_file '  ./multi_choice_data/valid_swag.csv' \
--output_dir ./multi_choice_model/   \
--per_gpu_eval_batch_size=2 \
--per_device_train_batch_size=2 \
--gradient_accumulation_steps 128 \
"""

parameter introduction:

--model_name_or_path: the directory to trained model or the name in huggingface hub
--learning rate: Learning rate
--num_train_epochs: the number of trainging epoch
--train_file : the path to training file
--validation_file : the path to valid file
--output_dir : where to stor the model checkpoint and other file
--per_gpu_eval_batch_size: the number of batch size
--per_device_train_batch_size: the number of training batch size
--gradient_accumulation_steps: for acceleration

3. Testing the model and output to csv format

"""
python3 ./runswag.py \
--do_predict \
--model_name_or_path ./multi_choice_model/ \
--output_dir ./multi_choice_model/  \
--cache_dir ./ \
--test_file  ./multi_choice_data/test_swag.csv \
--output_file ./test_output.csv  \
--per_gpu_eval_batch_size=2 \
--per_device_train_batch_size=2
"""
--model_name_or_path : the path to trained model
--output_dir : the directory to save output
--test_file : the path to test file
--output_dir : where to stor the model checkpoint and other file
--per_gpu_eval_batch_size: the number of batch size
--per_device_train_batch_size: the number of training batch size

4. convert data to squad format for training QA model
"""
python3 data_to_squad.py ./data/context.json ./data/train.json ./QA_data/train_squad.csv
python3 data_to_squad.py ./data/context.json ./data/valid.json ./QA_data/valid_squad.csv
"""

5. Training QA_model:
"""
python3 runqa.py --model_name_or_path bert-base-chinese  --do_train  --do_eval  --train_file ./QA_data/train_squad.csv  --validation_file  ./QA_data/valid_squad.csv   --per_device_train_batch_size 8  --per_device_eval_batch_size 8 --learning_rate 3e-5  --num_train_epochs 3 --max_seq_length 512 --doc_stride 128  --output_dir ./QA_model --cache_dir ./cache

"""
parameter introduction:

--model_name_or_path: the directory to trained model or the name in huggingface hub
--learning rate: Learning rate
--num_train_epochs: the number of trainging epoch
--train_file : the path to training file
--validation_file : the path to valid file
--output_dir : where to stor the model checkpoint and other file
--per_gpu_eval_batch_size: the number of batch size
--per_device_train_batch_size: the number of training batch size

6. combine the output from multi-choice and context.json to make the test file in SQUAD format
"""
python3 test_mc_to_squad.py ./data/context.json  ./data/test.json  ./test_output.csv   ./QA_data/test_squad.csv
"""

7. Predict the answer but in json foramt:
"""
python3 runqa.py --model_name_or_path ./QA_model \
--do_predict \
--output_dir ./QA_model/  \
--cache_dir ./ \
--test_file  ./QA_data/test_squad.csv \
--per_gpu_eval_batch_size=2 \
--per_device_train_batch_size=2
""" 

8. turn the answer to csv format for upload:
"""
python3 final_output.py ./QA_model/predict_predictions.json  ./final_submit.csv 
"""

9. how to exectute the code
"""
bash download.sh
bash ./run.sh  ./data/context.json  ./data/test.json  ./prediction.csv
"""





















