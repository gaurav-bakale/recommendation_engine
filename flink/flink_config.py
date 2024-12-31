from pyflink.datastream import StreamExecutionEnvironment

def get_flink_env():
    return StreamExecutionEnvironment.get_execution_environment()