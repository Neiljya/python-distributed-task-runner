import os
import multiprocessing
import subprocess
import queue
import time
import shutil

# BuildServer: distributes Python tasks/scripts -> collects results -> parallelizes post-task processes
class BuildServer:
    def __init__(self, source_dir, output_dir, num_workers):
        self.source_dir = source_dir
        self.output_dir = output_dir
        self.num_workers = num_workers
        self.task_queue = multiprocessing.Queue()
        self.result_queue = multiprocessing.Queue()

    # Start worker processes to handle execution and post-processing
    def start_workers(self):
        workers = []
        p = multiprocessing.Process(target=execute_files, args=(self.source_dir, self.output_dir, self.result_queue))
        workers.append(p)
        p.start()

        for i in range(self.num_workers):
            p = multiprocessing.Process(target=post_task_processing, args=(self.task_queue, self.result_queue, self.output_dir))
            workers.append(p)
            p.start()

        # Wait for all workers to finish
        for worker in workers:
            worker.join()

        print('All workers finished')

    def collect_results(self):
        while not self.result_queue.empty():
            result = self.result_queue.get()
            print(result)

# Function to execute all Python files in the source directory
def execute_files(source_dir, output_dir, result_queue):
    try:
        # Execute all Python files
        python_files = [f for f in os.listdir(source_dir) if f.endswith('.py')]

        for python_file in python_files:
            start_time = time.time()

            execute_command = f"python {os.path.join(source_dir, python_file)}"
            subprocess.run(execute_command, shell=True, check=True)

            execution_time = time.time() - start_time

            result_queue.put(f"Execution Success: {python_file}, Time: {execution_time:.2f}s")
    except subprocess.CalledProcessError as e:
        result_queue.put(f"Execution Failed: {str(e)}")

# Handle post-task processes in parallel
def post_task_processing(task_queue, result_queue, output_dir):
    while True:
        try:
            task = task_queue.get_nowait()

            if task == "package":
                package(output_dir, "result.zip")
                result_queue.put(f"Packaging Successful")
            else:
                result_queue.put(f"Unknown task: {task}")
        except queue.Empty:
            break

# Zips all output files
def package(output_dir, final_zip):
    try:
        shutil.make_archive(final_zip.replace('.zip', ''), 'zip', output_dir)
        print(f"Packaged into {final_zip}")
    except Exception as e:
        print(f"Packaging Failed: {str(e)}")

if __name__ == "__main__":

    source_dir = "./python_source"
    output_dir = "./python_output"
    zip_name = "result.zip"

    # Record start time
    start_time = time.time()

    # Setting up a BuildServer with 2 workers
    build_server = BuildServer(source_dir, output_dir, num_workers=2)

    build_server.start_workers()
    build_server.task_queue.put("package")
    build_server.collect_results()

    # Measure execution time
    execution_time = time.time() - start_time
    print(f"Execution Time: {execution_time:.2f}s")

    # Record packaging start time
    packaging_start_time = time.time()

    # Perform packaging
    package(output_dir, zip_name)

    # Measure packaging time
    packaging_time = time.time() - packaging_start_time
    print(f"Packaging Time: {packaging_time:.2f}s")

    # Total time
    total_time = time.time() - start_time
    print(f"Total Execution Time: {total_time:.2f}s")
