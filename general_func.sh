run_cmd() {
    local cmd=$1
    local job_desc=$2
    # local log_file=$3
    local full_cmd="time $cmd"
    echo "$job_desc..."
    echo $full_cmd
    eval $full_cmd
    echo
    echo "--------------------------------------------"
    echo
}
