model_item=edvr
bs_item=4
fp_item=fp32
run_process_type=MultiP
run_mode=DP
device_num=N1C8

sed -i '/set\ -xe/d' run_benchmark.sh
bash PrepareEnv.sh ${model_item};
<<<<<<< HEAD
bash run_benchmark.sh ${model_item} ${bs_item} ${fp_item} ${run_process_type} ${run_mode} ${device_num} 2>&1;
=======
bash run_benchmark.sh ${model_item} ${bs_item} ${fp_item} ${run_mode} ${device_num} 2>&1;
>>>>>>> upstream/develop
